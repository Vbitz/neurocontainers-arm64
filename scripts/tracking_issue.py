"""Generate ARM64 coverage from all workflow runs, issue reports and porting plans.

Read-only by default; --write updates issue #2. Requires Python and authenticated gh.
"""

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parents[1]
REPO = 'Vbitz/neurocontainers-arm64'
STATUS_LABELS = {
    'Yes': '✅', 'No': '❌', 'Skips': '⚠️ Skips',
    'Not run': '➖ Not run', 'Cancelled': '⏹️ Cancelled', 'Unknown': '❓ Unknown',
}
CONTAINER = re.compile(r'<!-- arm64-container:([^:]+):([^ ]+) -->')
RUN = re.compile(r'<!-- arm64-run:(\d+):(\d+) -->')
TITLE = re.compile(r'^ARM64 (.+) \(([^()]+)\)$')
COUNTS = re.compile(r'Tests: \*\*(\d+) passed\*\*, \*\*(\d+) failed\*\*, '
                    r'\*\*(\d+) skipped\*\*, (\d+) total')
ASSESSMENTS = {
    'Plausible recipe-level port; no fundamental blocker established': 'Plausible',
    'A recipe-level ARM route is now plausible; no fundamental blocker is established': 'Plausible',
    'Complete dependency stack unresolved': 'Unresolved',
    'Native dependency or legacy environment needs a supported build route': 'Unresolved',
    'Concrete prior build failure; not a general architecture prohibition': 'Unresolved',
    'GPU capability or supported CPU-mode prerequisite': 'Conditional',
    'Required vendor runtime/standalone execution path unavailable': 'Blocked prerequisite',
    'Binary distribution; no public source-build route found': 'No route found',
    'Different operating-system application port required': 'Outside scope',
}
OUTCOME = re.compile(
    r'^Outcome:\s*(blocked-upstream|blocked-infrastructure|blocked-prerequisite|failed-runtime|in-progress|verified)\b',
    re.M | re.I)


def command(*args):
    return subprocess.check_output(args, text=True)


def api_pages(endpoint, key=None):
    pages = json.loads(command('gh', 'api', '--paginate', '--slurp', endpoint))
    items = [item for page in pages for item in (page[key] if key else page)]
    if key and pages and len(items) < pages[0]['total_count']:
        raise RuntimeError(f'Incomplete GitHub pagination for {endpoint}')
    return items


def documents(issue):
    yield issue
    comments = issue.get('comments', [])
    if isinstance(comments, dict):
        comments = comments['nodes']
    yield from comments


def parse_report(body):
    marker = RUN.search(body)
    if not marker:
        return None
    checks = dict(re.findall(r'^\| ([^|]+?) \| ([^|]+?) \|\s*$', body, re.M))
    counts = COUNTS.search(body)
    sha = re.search(r'https://github.com/Vbitz/neurocontainers/commit/([0-9a-f]{40})', body)
    return {'run_id': int(marker[1]), 'attempt': int(marker[2]),
            'build': checks.get('ARM64 Docker build and SIF conversion', 'unknown'),
            'test': checks.get('Deploy checks and fulltest', 'unknown'),
            'counts': tuple(map(int, counts.groups())) if counts else None,
            'sha': sha[1] if sha else None}


def report_index(issues):
    reports = {}
    for issue in issues:
        identity = CONTAINER.search(issue.get('body') or '')
        if not identity:
            continue
        key = tuple(map(unquote, identity.groups()))
        for doc in documents(issue):
            report = parse_report(doc.get('body') or '')
            if report:
                report['identity'] = key
                report['url'] = doc.get('html_url') or doc.get('url')
                reports[report['run_id'], report['attempt']] = report
    return reports


def run_identity(run, issues):
    match = TITLE.fullmatch(run['display_title'])
    if match:
        return tuple(match.groups())
    # Startup failures can have a generic workflow title and no jobs. Recover
    # identity only when the exact run URL occurs in exactly one container issue.
    identities = set()
    reference = re.compile(r'/actions/runs/' + str(run['id']) + r'(?!\d)')
    for issue in issues:
        marker = CONTAINER.search(issue.get('body') or '')
        if marker and any(reference.search(doc.get('body') or '') for doc in documents(issue)):
            identities.add(tuple(map(unquote, marker.groups())))
    return next(iter(identities)) if len(identities) == 1 else None


def last_outcome(issue):
    notes = []
    for doc in documents(issue):
        match = OUTCOME.search(doc.get('body') or '')
        if match:
            notes.append((doc.get('created_at') or doc.get('createdAt') or '',
                          match[1].lower(), doc.get('html_url') or doc.get('url')))
    return max(notes, key=lambda item: item[0])[1:] if notes else None


def collect(repo):
    """Read closed issues, all comments and all workflow runs, without list caps."""
    base = f'repos/{repo}'
    requests = [(f'{base}/issues?state=all&labels=arm64-container&per_page=100', None),
                (f'{base}/issues/comments?per_page=100', None),
                (f'{base}/actions/workflows/build-arm64.yml/runs?per_page=100', 'workflow_runs')]
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(api_pages, endpoint, key) for endpoint, key in requests]
        issues, comments, runs = [future.result() for future in futures]
    issues = [issue for issue in issues if 'pull_request' not in issue]
    by_number = {issue['number']: issue for issue in issues}
    for issue in issues:
        issue['comments'] = []
    for comment in comments:
        number = int(comment['issue_url'].rsplit('/', 1)[1])
        if number in by_number:
            by_number[number]['comments'].append(comment)
    reports = report_index(issues)
    missing = [(run, attempt) for run in runs if run['status'] == 'completed'
               for attempt in range(1, run.get('run_attempt', 1) + 1)
               if (run['id'], attempt) not in reports]
    print(f'Fetched {len(issues)} issues and {len(runs)} runs; '
          f'checking {len(missing)} unreported attempts.', file=sys.stderr)

    def recover(item):
        run, attempt = item
        jobs = api_pages(f'{base}/actions/runs/{run["id"]}/attempts/{attempt}/jobs?per_page=100', 'jobs')
        return {'run_id': run['id'], 'attempt': attempt, 'jobs': jobs}

    with ThreadPoolExecutor(max_workers=4) as pool:
        recovered = list(pool.map(recover, missing))
    return {'repo': repo, 'collected_at': datetime.now(timezone.utc).isoformat(),
            'issues': issues, 'runs': runs, 'recovered': recovered}


def recover_report(record, run, identity=None):
    job = next((j for j in record['jobs'] if j['name'] == 'build'), {})
    steps = {step['name']: step.get('conclusion') for step in job.get('steps', [])}
    # Job success alone cannot prove a native build, nor zero skipped tests.
    native = 'ubuntu-24.04-arm' in job.get('labels', [])
    unavailable = 'not run' if not record['jobs'] else 'unknown'
    return {'run_id': run['id'], 'attempt': record['attempt'],
            'identity': identity or tuple(TITLE.fullmatch(run['display_title']).groups()),
            'build': steps.get('Build ARM64 image and convert to SIF', 'not run') if native else unavailable,
            'test': steps.get('Run deploy checks and fulltest', 'not run') if native else unavailable,
            'counts': None, 'sha': None, 'url': job.get('html_url') or run['html_url']}


def statuses(report):
    if report is None:
        return 'Not run', 'Not run'
    build = {'success': 'Yes', 'failure': 'No', 'cancelled': 'Cancelled',
             'skipped': 'Not run', 'not run': 'Not run'}.get(report['build'], 'Unknown')
    test = {'failure': 'No', 'cancelled': 'Cancelled', 'skipped': 'Not run',
            'not run': 'Not run'}.get(report['test'], 'Unknown')
    if report['test'] == 'success' and report['counts']:
        passed, failed, skipped, total = report['counts']
        if failed:
            test = 'No'
        elif skipped:
            test = 'Skips'
        elif total > 0 and passed == total and build == 'Yes':
            test = 'Yes'
    return build, test


def load_plans(root, revision):
    plans = {}
    paths = command('git', '-C', str(root), 'ls-tree', '-r', '--name-only', revision, '--', 'plans').splitlines()
    for path in paths:
        if not path.endswith('.md') or path.endswith('/README.md'):
            continue
        content = command('git', '-C', str(root), 'show', f'{revision}:{path}')
        match = re.search(r'\*\*Assessment: (.+?)\.?\*\*', content)
        if not match:
            raise ValueError(f'Missing Assessment in {path}')
        assessment = match[1].rstrip('.')
        if assessment not in ASSESSMENTS:
            raise ValueError(f'Unrecognized Assessment in {path}: {assessment}')
        plans[Path(path).stem] = {'status': ASSESSMENTS[assessment], 'path': path}
    return plans


def inventory(root, revision):
    pin = command('git', '-C', str(root), 'rev-parse', f'{revision}:neurocontainers').strip()
    paths = command('git', '-C', str(root / 'neurocontainers'), 'ls-tree', '-r', '--name-only', pin,
                    '--', 'recipes').splitlines()
    recipes = sorted(Path(path).parts[1] for path in paths
                     if len(Path(path).parts) == 3 and path.endswith('/build.yaml'))
    if not recipes:
        raise RuntimeError('No recipes found at accepted pin')
    return pin, recipes


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')


def make_rows(recipes, plans, snapshot):
    reports = report_index(snapshot['issues'])
    runs = {run['id']: run for run in snapshot['runs']}
    for record in snapshot.get('recovered', []):
        run = runs[record['run_id']]
        identity = run_identity(run, snapshot['issues'])
        if identity:
            reports[run['id'], record['attempt']] = recover_report(record, run, identity)
    grouped, issues, run_groups = defaultdict(list), defaultdict(list), defaultdict(list)
    for issue in snapshot['issues']:
        identity = CONTAINER.search(issue.get('body') or '')
        if identity:
            issues[tuple(map(unquote, identity.groups()))].append(issue)
    for report in reports.values():
        grouped[report['identity']].append(report)
    for run in runs.values():
        identity = run_identity(run, snapshot['issues'])
        if identity:
            run_groups[identity].append(run)
    keys = set(issues) | set(grouped) | set(run_groups)
    for recipe in recipes:
        if not any(key[0] == recipe for key in keys):
            keys.add((recipe, 'arm64'))
    rows = []
    for recipe, variant in sorted(keys):
        key = (recipe, variant)
        history = sorted(grouped[key], key=lambda r: (r['run_id'], r['attempt']))
        report = history[-1] if history else None
        build, test = statuses(report)
        current_runs = sorted(run_groups[key], key=lambda r: r['id'])
        active = [r for r in current_runs if r['status'] != 'completed']
        completed = [r for r in current_runs if r['status'] == 'completed']
        if completed:
            latest = completed[-1]
            latest_key = latest['id'], latest.get('run_attempt', 1)
            if report is None or latest_key > (report['run_id'], report['attempt']):
                report = None
                build = test = 'Unknown'
        plan = plans.get(recipe)
        feasibility = 'Verified' if test == 'Yes' else plan['status'] if plan else 'Not assessed'
        rows.append({'recipe': recipe, 'variant': variant, 'build': build, 'test': test,
                     'feasibility': feasibility, 'plan': plan, 'report': report,
                     'history': history, 'issues': issues[key], 'active': active,
                     'runs': current_runs})
    return rows


def render(root, revision, snapshot):
    pin, recipes = inventory(root, revision)
    rows = make_rows(recipes, load_plans(root, revision), snapshot)
    base = f'https://github.com/{snapshot["repo"]}'
    lines = [
        '<!-- arm64-recipe-tracker -->', '# ARM64 container build and test coverage', '',
        f'Snapshot: {snapshot["collected_at"]}. Inventory: '
        f'[accepted fork `{pin[:12]}`](https://github.com/Vbitz/neurocontainers/tree/{pin}/recipes). '
        f'Plans: [source `{revision[:12]}`]({base}/tree/{revision}/plans).', '',
        'One row per recipe/variant, including unbuilt recipes and historical variants. '
        'The variant is `arm64` unless another selector is shown. '
        '**Build** means the native ARM64 Docker build, architecture check and SIF conversion succeeded. '
        '**All tests** requires deploy/fulltest success, a positive test count, zero failures and zero skips. '
        '✅ = passed; ❌ = failed; ⚠️ = skipped tests; ➖ = not run; ⏹️ = cancelled; '
        '❓ = insufficient evidence. Not run includes preflight/setup failures.', '',
        'Results use the **latest completed attempt** for each variant across all workflow history and '
        'durable issue reports. Active attempts are linked separately; earlier successes remain historical '
        'evidence. Results apply to the linked tested candidate, not automatically to the current accepted pin '
        'or a published release. Test counts are passed/failed/skipped.', '',
        '**Plan feasibility** is the plan’s explicit research assessment when tests are not fully passing: '
        'Plausible = a recipe-level route identified; Unresolved = more dependency/build research required; '
        'Conditional = GPU or supported CPU prerequisites; Blocked prerequisite = required vendor runtime unavailable; '
        'No route found = no public source-build route found; Outside scope = an OS application port required. '
        'These are scoped assessments, not proof of impossibility. Evidence links for unverified variants '
        'include the latest explicit investigation outcome when available; that note may predate the research '
        'assessment. Verified means build and all tests passed. Not assessed means no research plan exists.', '',
        '`workshopdemo` is a pipeline check; demo/infrastructure recipes remain in the inventory.', '',
        '| Container / variant | Builds ARM64? | Passes all ARM64 tests? | Plan feasibility if unverified | Evidence |',
        '| --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        report = row['report']
        evidence = []
        for issue in row['issues']:
            label, url = f'#{issue["number"]}', issue.get('html_url') or issue.get('url')
            outcome = last_outcome(issue) if row['test'] != 'Yes' else None
            if outcome:
                label += ' ' + outcome[0]
                url = outcome[1] or url
            evidence.append(f'[{label}]({url})')
        if report:
            url = f'{base}/actions/runs/{report["run_id"]}/attempts/{report["attempt"]}'
            label = 'latest'
            if report['counts']:
                label += ' ' + '/'.join(map(str, report['counts'][:3]))
            evidence.append(f'[{label}]({url})')
        previous = [r for r in row['history'] if statuses(r)[1] == 'Yes' and r is not report]
        if row['test'] != 'Yes' and previous:
            old = previous[-1]
            evidence.append(f'[earlier pass]({base}/actions/runs/{old["run_id"]}/attempts/{old["attempt"]})')
        for run in row['active']:
            evidence.append(f'[{run["status"]}]({run["html_url"]})')
        plan = row['feasibility']
        if plan == 'Verified':
            plan = '✅ Verified'
        elif row['plan']:
            plan = f'[{plan}]({base}/blob/{revision[:12]}/{quote(row["plan"]["path"])})'
        name = f'`{row["recipe"]}`'
        if row['variant'] != 'arm64':
            name += f' / `{row["variant"]}`'
        values = [name, STATUS_LABELS[row['build']], STATUS_LABELS[row['test']], plan,
                  ' · '.join(evidence) or '—']
        lines.append('| ' + ' | '.join(map(cell, values)) + ' |')
    lines += ['', '## Summary', '',
              f'- Recipes at accepted pin: **{len(recipes)}**. Table rows (recipe/variant): **{len(rows)}**.',
              f'- Workflow runs reviewed: **{len(snapshot["runs"])}**; '
              f'attempts: **{sum(r.get("run_attempt", 1) for r in snapshot["runs"])}**; '
              f'active runs: **{sum(len(r["active"]) for r in rows)}**.',
              f'- Variants with any historical fully passing report: '
              f'**{sum(any(statuses(h)[1] == "Yes" for h in r["history"]) for r in rows)}**.', '',
              'Counts below use the latest completed evidence; each build/test column totals the table rows.', '',
              '| Latest result | ARM64 build | All ARM64 tests |', '| --- | ---: | ---: |']
    builds, tests = Counter(r['build'] for r in rows), Counter(r['test'] for r in rows)
    for status in ('Yes', 'No', 'Skips', 'Not run', 'Cancelled', 'Unknown'):
        lines.append(f'| {STATUS_LABELS[status]} | {builds[status]} | {tests[status]} |')
    lines += ['', 'Plan assessments below exclude fully passing variants.', '',
              '| Feasibility of unverified variants | Count |', '| --- | ---: |']
    feasibility = Counter(r['feasibility'] for r in rows if r['test'] != 'Yes')
    for status in (*dict.fromkeys(ASSESSMENTS.values()), 'Not assessed'):
        lines.append(f'| {status} | {feasibility[status]} |')
    unknown = [r for r in snapshot['runs'] if not run_identity(r, snapshot['issues'])]
    if unknown:
        lines += ['', f'**Runs without an identifiable recipe: {len(unknown)}.**', '']
        lines += [f'- [{r["id"]}]({r["html_url"]}): {cell(r["display_title"])}' for r in unknown]
    lines += ['', 'Regenerate with `python scripts/tracking_issue.py --write` (authenticated `gh` required).', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default=REPO)
    parser.add_argument('--issue', type=int, default=2)
    parser.add_argument('--output', type=Path, help='Also save the generated Markdown')
    parser.add_argument('--snapshot', type=Path, help='Save fetched evidence as JSON for offline replay')
    parser.add_argument('--from-snapshot', type=Path, help='Read saved evidence instead of fetching GitHub')
    parser.add_argument('--write', action='store_true', help='Replace the issue body; comments are preserved')
    args = parser.parse_args()
    snapshot = json.loads(args.from_snapshot.read_text()) if args.from_snapshot else collect(args.repo)
    revision = snapshot.setdefault('revision', command('git', '-C', str(ROOT), 'rev-parse', 'HEAD').strip())
    if snapshot['repo'] != args.repo:
        parser.error('Snapshot repository does not match --repo')
    if args.snapshot:
        args.snapshot.write_text(json.dumps(snapshot, indent=2) + '\n')
    markdown = render(ROOT, revision, snapshot)
    if len(markdown) > 65536:
        raise RuntimeError(f'Generated issue body exceeds GitHub limit: {len(markdown)} characters')
    if args.output:
        args.output.write_text(markdown)
    if args.write:
        body = json.loads(command('gh', 'issue', 'view', str(args.issue), '-R', args.repo, '--json', 'body'))['body']
        if '<!-- arm64-recipe-tracker -->' not in body:
            raise RuntimeError('Target issue is missing coverage tracker marker; refusing replacement')
        with tempfile.TemporaryDirectory(prefix='arm64-tracker-') as directory:
            path = Path(directory) / 'issue.md'
            path.write_text(markdown)
            subprocess.run(['gh', 'issue', 'edit', str(args.issue), '-R', args.repo,
                            '--body-file', str(path)], check=True)
        actual = json.loads(command('gh', 'issue', 'view', str(args.issue), '-R', args.repo, '--json', 'body'))['body']
        if actual != markdown:
            raise RuntimeError('Issue readback differs from generated Markdown')
        print(f'Updated and verified https://github.com/{args.repo}/issues/{args.issue}', file=sys.stderr)
    elif not args.output:
        print(markdown, end='')


if __name__ == '__main__':
    main()
