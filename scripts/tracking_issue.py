"""Render the recipe checklist from the checked-out fork (no GitHub writes)."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]


def render(checkout, issues):
    sys.path.insert(0, str(checkout))
    from builder.variants import concrete_variant_specs

    sha = subprocess.check_output(
        ['git', '-C', str(checkout), 'rev-parse', 'HEAD'], text=True,
    ).strip()
    if subprocess.check_output(
        ['git', '-C', str(checkout), 'status', '--porcelain', '--', 'recipes'],
        text=True,
    ).strip():
        raise RuntimeError('Commit recipe changes before generating a revision-based tracker')
    links = {}
    for issue in issues:
        match = re.search(r'<!-- arm64-container:([^:]+):([^ ]+) -->', issue.get('body') or '')
        if match:
            recipe, variant = map(unquote, match.groups())
            links.setdefault(recipe, []).append((variant, issue['url']))
    entries = []
    supported = 0
    for recipe_file in sorted((checkout / 'recipes').glob('*/build.yaml')):
        recipe = recipe_file.parent.name
        data = yaml.safe_load(recipe_file.read_text())
        variants = [spec['variant'] for spec in concrete_variant_specs(data)
                    if spec['architecture'] == 'aarch64']
        supported += bool(variants)
        line = f"- [{'x' if variants else ' '}] `{recipe}`"
        if variants and variants != ['arm64']:
            line += ' — ARM64 variants: ' + ', '.join(f'`{v}`' for v in variants)
        if not recipe_file.with_name('fulltest.yaml').is_file():
            line += ' — missing fulltest.yaml'
        if recipe in links:
            line += ' — ' + ', '.join(
                f'[{variant} results]({url})' for variant, url in sorted(links[recipe])
            )
        entries.append(line)
    if not entries:
        raise RuntimeError('No recipes found')
    return (
        '<!-- arm64-recipe-tracker -->\n'
        '# ARM64 recipe coverage\n\n'
        f'**{supported} / {len(entries)} recipes declare ARM64 support; '
        f'{len(entries) - supported} do not.**\n\n'
        f'Source: [Vbitz/neurocontainers@{sha[:12]}]'
        f'(https://github.com/Vbitz/neurocontainers/tree/{sha}/recipes).\n\n'
        'Checked means the recipe declares at least one `aarch64` variant, '
        'using the builder’s architecture resolver. It does **not** mean its '
        'ARM64 build and runtime tests have passed. Unchecked means no declared '
        'ARM64 variant, not that porting is impossible.\n\n'
        'Build/test evidence lives in the linked per-container issues; '
        '[all result issues](https://github.com/Vbitz/neurocontainers-arm64/issues?q=is%3Aissue+label%3Aarm64-container). '
        'Each run records its own source revision. `workshopdemo` is only a '
        'pipeline check.\n\n'
        'This is a snapshot of every `recipes/*/build.yaml`, including demo and '
        'infrastructure recipes. Refresh from the pinned fork after recipe updates; '
        'see the repository README. Parsing/resolution errors stop generation '
        'rather than silently omitting recipes.\n\n'
        '## All recipes\n\n' + '\n'.join(entries) + '\n'
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--issues-json', type=Path, help='gh issue list JSON including body and url')
    args = parser.parse_args()
    issues = json.loads(args.issues_json.read_text()) if args.issues_json else []
    print(render(ROOT / 'neurocontainers', issues), end='')
