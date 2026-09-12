"""Render the recipe checklist from the checked-out fork (no GitHub writes)."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]


def latest_arm64_release(directories):
    from builder.release_artifact import read_release_metadata, ReleaseArtifactError

    releases = []
    for directory in directories:
        for path in sorted(directory.glob('*.json')):
            data = json.loads(path.read_text())
            architecture = data.get('architecture')
            if architecture:
                arm64 = architecture in ('aarch64', 'arm64')
            else:
                apps = list((data.get('apps') or {}).values())
                arm64 = bool(apps) and all(
                    isinstance(app, dict) and app.get('architecture') in ('aarch64', 'arm64')
                    for app in apps
                )
            if not arm64:
                continue
            try:
                date, _ = read_release_metadata(path)
            except ReleaseArtifactError:
                continue
            releases.append((date, path.stem, path))
    return max(releases) if releases else None


def render(checkout, issues):
    sys.path.insert(0, str(checkout))
    from builder.variants import concrete_variant_specs

    sha = subprocess.check_output(
        ['git', '-C', str(checkout), 'rev-parse', 'HEAD'], text=True,
    ).strip()
    if subprocess.check_output(
        ['git', '-C', str(checkout), 'status', '--porcelain', '--', 'recipes', 'releases'],
        text=True,
    ).strip():
        raise RuntimeError('Commit recipe/release changes before generating a revision-based tracker')
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
        specs = concrete_variant_specs(data)
        variants = [spec['variant'] for spec in specs
                    if spec['architecture'] == 'aarch64']
        supported += bool(variants)
        line = f"- [{'x' if variants else ' '}] `{recipe}`"
        if variants and variants != ['arm64']:
            line += ' — ARM64 variants: ' + ', '.join(f'`{v}`' for v in variants)
        if not recipe_file.with_name('fulltest.yaml').is_file():
            line += ' — missing fulltest.yaml'
        containers = {recipe, f'{recipe}_arm64', *(spec['name'] for spec in specs)}
        release = latest_arm64_release(
            [checkout / 'releases' / container for container in sorted(containers)]
        )
        if release:
            _, version, path = release
            relative = quote(path.relative_to(checkout).as_posix(), safe='/')
            line += (
                f' — [ARM64 release JSON ({version})]'
                f'(https://github.com/Vbitz/neurocontainers/blob/{sha}/{relative})'
            )
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
        'Release JSON links point only to the latest **ARM64** metadata, including '
        'legacy releases stored in the base recipe directory. Architecture must '
        'be explicitly ARM64 in the release metadata. '
        'Selection uses the builder’s newest-build-date ordering (version string '
        'breaks ties). Links are pinned to the source commit above; absence means '
        'no valid ARM64 release metadata was found. A historical release does not '
        'prove that the current recipe passes its ARM64 tests.\n\n'
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
