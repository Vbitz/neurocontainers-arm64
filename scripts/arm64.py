"""Build and test one fork recipe; run from the neurocontainers checkout."""

import argparse
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys

import yaml


def run(*args, log=None):
    print('+', ' '.join(map(str, args)), flush=True)
    if log is None:
        subprocess.run(list(map(str, args)), check=True)
        return
    with Path(log).open('w') as output:
        process = subprocess.Popen(
            list(map(str, args)), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True,
        )
        for line in process.stdout:
            print(line, end='', flush=True)
            output.write(line)
        if process.wait():
            raise subprocess.CalledProcessError(process.returncode, args)


def prepare(recipe, variant, results):
    if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', recipe):
        raise ValueError('Choose one recipe directory name, without paths or commas')
    if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', variant):
        raise ValueError('Invalid variant name')
    # Use the same identity and architecture resolution as upstream candidates.
    sys.path.insert(0, str(Path.cwd()))
    from tools.one_pr_release import inspect_recipe

    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    info = inspect_recipe(recipe, sha, variant)
    if info['architecture'] != 'aarch64':
        raise ValueError('The selected variant must resolve to aarch64')
    suite = yaml.safe_load(Path(f'recipes/{recipe}/fulltest.yaml').read_text())
    if not suite.get('tests'):
        raise ValueError('A non-empty fulltest.yaml is required')
    if suite.get('name') != recipe or str(suite.get('version')) != info['version']:
        raise ValueError('fulltest.yaml name/version must match the recipe')
    info['source_sha'] = sha
    info['source_repository'] = 'Vbitz/neurocontainers'
    results.mkdir(parents=True, exist_ok=True)
    (results / 'metadata.json').write_text(json.dumps(info, indent=2) + '\n')
    shutil.copy2(f'recipes/{recipe}/fulltest.yaml', results / 'fulltest.yaml')
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
            output.write(f"container={info['container']}\n")
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write(
                f"Building **{info['container']}:{info['version']}** on native ARM64.\n\n"
                f"Source: [Vbitz/neurocontainers@{sha[:12]}]"
                f"(https://github.com/Vbitz/neurocontainers/commit/{sha})\n\n"
                'Deploy checks and the recipe fulltest suite test the new SIF.\n'
            )
    return info


def build(info, results):
    if platform.system() != 'Linux' or platform.machine() not in ('aarch64', 'arm64'):
        raise RuntimeError('Build and tests require a native Linux ARM64 host')
    recipe, variant = info['recipe'], info['variant']
    build_dir = Path('build') / info['container']
    run(sys.executable, '-m', 'builder', 'stage', recipe, '--variant', variant,
        '--architecture', 'aarch64', '--recreate', '--download', log=results / 'stage.log')
    dockerfile = build_dir / f"{info['container']}_{info['version']}.Dockerfile"
    shutil.copy2(dockerfile, results / 'Dockerfile')
    contexts = subprocess.check_output([
        sys.executable, '-m', 'builder', 'staged-context-args', str(build_dir),
    ]).decode().rstrip('\0').split('\0')
    run('docker', 'buildx', 'build', build_dir, '--platform', 'linux/arm64',
        '--load', '--progress', 'plain', '--file', dockerfile,
        '--tag', info['candidate_tag'], '--build-context',
        f'neurocontainer-cache={build_dir}/cache',
        *[arg for arg in contexts if arg], log=results / 'build.log')
    image = json.loads(subprocess.check_output([
        'docker', 'image', 'inspect', info['candidate_tag'],
    ]))[0]
    if image['Architecture'] != 'arm64' or image['Os'] != 'linux':
        raise RuntimeError('Built image is not Linux ARM64')
    info['docker_image_id'] = image['Id']
    (results / 'metadata.json').write_text(json.dumps(info, indent=2) + '\n')
    archive = results / info['docker_archive']
    run('docker', 'save', info['candidate_tag'], '--output', archive)
    run('apptainer', 'build', results / info['sif'],
        f'docker-archive://{archive}', log=results / 'apptainer.log')
    archive.unlink()  # Keep the SIF, avoiding a second large artifact on disk.


def test(info, results):
    run(sys.executable, '-m', 'workflows.release_test_runner',
        '--recipe', info['recipe'], '--version', info['version'],
        '--release-file', results / f"{info['version']}.json",
        '--candidate-container', results / info['sif'],
        '--runtime', 'apptainer',
        '--test-config', f"recipes/{info['recipe']}/fulltest.yaml",
        '--results-path', results / 'test-results.json',
        '--output-dir', results / 'test-output', '--repo-root', '.', '--verbose',
        log=results / 'test.log')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['prepare', 'build', 'test'])
    parser.add_argument('--recipe', default=os.environ.get('RECIPE', ''))
    parser.add_argument('--variant', default=os.environ.get('VARIANT', 'arm64'))
    parser.add_argument('--results', type=Path, default=Path('../results'))
    args = parser.parse_args()
    results = args.results.resolve()
    if args.phase == 'prepare':
        prepare(args.recipe, args.variant, results)
    else:
        info = json.loads((results / 'metadata.json').read_text())
        {'build': build, 'test': test}[args.phase](info, results)


if __name__ == '__main__':
    main()
