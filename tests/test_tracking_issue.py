"""Coverage classification must not turn missing evidence or skips into passes."""

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('tracking_issue', ROOT / 'scripts/tracking_issue.py')
tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracker)


def report(run=10, attempt=1, build='success', test='success', counts=(4, 0, 0, 4)):
    text = (f'<!-- arm64-run:{run}:{attempt} -->\n'
            f'| ARM64 Docker build and SIF conversion | {build} |\n'
            f'| Deploy checks and fulltest | {test} |\n')
    if counts is not None:
        text += (f'Tests: **{counts[0]} passed**, **{counts[1]} failed**, '
                 f'**{counts[2]} skipped**, {counts[3]} total.\n')
    return text


def issue(body, comments=(), variant='arm64'):
    return {'number': 7, 'html_url': 'https://example.org/issues/7',
            'body': f'<!-- arm64-container:tool:{variant} -->\n' + body,
            'comments': [{'body': text} for text in comments]}


def run(number, status='completed', attempt=1):
    return {'id': number, 'display_title': 'ARM64 tool (arm64)',
            'status': status, 'run_attempt': attempt, 'html_url': f'https://example.org/runs/{number}'}


class CoverageTests(unittest.TestCase):
    def test_success_requires_counts_and_no_skips(self):
        for counts, expected in [(None, 'Unknown'), ((0, 0, 0, 0), 'Unknown'),
                                 ((4, 0, 0, 5), 'Unknown'), ((4, 0, 1, 5), 'Skips'),
                                 ((4, 1, 0, 5), 'No'), ((4, 0, 0, 4), 'Yes')]:
            with self.subTest(counts=counts):
                self.assertEqual(tracker.statuses(tracker.parse_report(report(counts=counts)))[1], expected)

    def test_job_failure_does_not_hide_build_success(self):
        parsed = tracker.parse_report(report(test='failure', counts=(3, 1, 0, 4)))
        self.assertEqual(tracker.statuses(parsed), ('Yes', 'No'))
        parsed = tracker.parse_report(report(build='not run', test='not run', counts=None))
        self.assertEqual(tracker.statuses(parsed), ('Not run', 'Not run'))

    def test_history_dedup_and_latest_failure(self):
        data = {'issues': [issue(report(11, build='failure', test='not run', counts=None),
                                [report(10), report(10)])], 'runs': [run(10), run(11)]}
        row = tracker.make_rows(['tool'], {}, data)[0]
        self.assertEqual(len(row['history']), 2)
        self.assertEqual((row['build'], row['test']), ('No', 'Not run'))
        self.assertEqual(row['history'][0]['run_id'], 10)

    def test_active_run_preserves_previous_result(self):
        data = {'issues': [issue(report())], 'runs': [run(10), run(11, 'in_progress')]}
        row = tracker.make_rows(['tool'], {}, data)[0]
        self.assertEqual(row['test'], 'Yes')
        self.assertEqual(row['active'][0]['id'], 11)

    def test_missing_latest_report_does_not_reuse_green_result(self):
        data = {'issues': [issue(report())], 'runs': [run(10, attempt=2)]}
        row = tracker.make_rows(['tool'], {}, data)[0]
        self.assertEqual(row['test'], 'Unknown')

    def test_variants_and_preflight_plans_are_separate(self):
        data = {'issues': [issue(report()), issue('', variant='gpu_arm64')], 'runs': []}
        rows = tracker.make_rows(['tool', 'unbuilt'], {'unbuilt': {'status': 'Unresolved'}}, data)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]['test'], 'Yes')
        self.assertEqual(rows[1]['test'], 'Not run')
        self.assertEqual(rows[2]['feasibility'], 'Unresolved')

    def test_recovered_jobs_need_native_label_and_counts(self):
        record = {'attempt': 1, 'jobs': [{'name': 'build', 'labels': ['ubuntu-24.04-arm'],
                  'steps': [{'name': 'Build ARM64 image and convert to SIF', 'conclusion': 'success'},
                            {'name': 'Run deploy checks and fulltest', 'conclusion': 'success'}]}]}
        parsed = tracker.recover_report(record, run(10))
        self.assertEqual(tracker.statuses(parsed), ('Yes', 'Unknown'))
        record['jobs'][0]['labels'] = ['ubuntu-24.04']
        self.assertEqual(tracker.statuses(tracker.recover_report(record, run(10))), ('Unknown', 'Unknown'))

    def test_pagination_refuses_partial_workflow_history(self):
        with patch.object(tracker, 'command', return_value='[{"total_count": 2, "workflow_runs": [{}]}]'):
            with self.assertRaisesRegex(RuntimeError, 'Incomplete'):
                tracker.api_pages('endpoint', 'workflow_runs')

    def test_startup_failure_identity_from_unique_issue_reference(self):
        failed = run(10)
        failed['display_title'] = 'Build and test one ARM64 container'
        notes = [issue('', ['Startup failure: https://github.com/a/b/actions/runs/10'])]
        identity = tracker.run_identity(failed, notes)
        self.assertEqual(identity, ('tool', 'arm64'))
        recovered = tracker.recover_report({'attempt': 1, 'jobs': []}, failed, identity)
        self.assertEqual(tracker.statuses(recovered), ('Not run', 'Not run'))
        notes.append(issue('', ['https://github.com/a/b/actions/runs/10'], variant='gpu_arm64'))
        self.assertIsNone(tracker.run_identity(failed, notes))

    def test_later_investigation_outcome_is_linked(self):
        record = issue('', ['Outcome: in-progress', 'Outcome: blocked-upstream'])
        record['comments'][0].update(created_at='2026-09-13', html_url='https://example.org/old')
        record['comments'][1].update(created_at='2026-09-14', html_url='https://example.org/new')
        self.assertEqual(tracker.last_outcome(record), ('blocked-upstream', 'https://example.org/new'))

    def test_render_counts_and_escapes_table(self):
        data = {'repo': tracker.REPO, 'collected_at': 'now', 'issues': [issue(report())], 'runs': [run(10)]}
        with patch.object(tracker, 'inventory', return_value=('a' * 40, ['tool', 'unbuilt'])), \
                patch.object(tracker, 'load_plans', return_value={}):
            markdown = tracker.render(ROOT, 'b' * 40, data)
        self.assertIn('| ✅ | 1 | 1 |', markdown)
        self.assertIn('| ➖ Not run | 1 | 1 |', markdown)
        self.assertIn('| Not assessed | 1 |', markdown)
        self.assertEqual(tracker.cell('a|b\nc'), 'a&#124;b c')


if __name__ == '__main__':
    unittest.main()
