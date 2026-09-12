const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { test } = require('node:test');
const report = require('../scripts/report.cjs');

test('reports failures, reuses the container issue, and deduplicates attempts', async () => {
  const original = process.cwd();
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'arm64-report-'));
  const issues = [], comments = [];
  try {
    process.chdir(temp);
    fs.mkdirSync('results');
    fs.writeFileSync('results/metadata.json', JSON.stringify({
      source_sha: 'a'.repeat(40), version: '1.0',
    }));
    fs.writeFileSync('results/test-results.json', JSON.stringify({
      total_tests: 3, passed: 2, failed: 1, skipped: 0,
      test_results: [{ name: 'runtime check', status: 'failed' }],
    }));
    Object.assign(process.env, {
      RECIPE: 'example', VARIANT: 'arm64', CONTAINER: 'example_arm64',
      BUILD_RESULT: 'failure', BUILD_OUTCOME: 'success', TEST_OUTCOME: 'failure',
      GITHUB_RUN_ATTEMPT: '1',
    });
    const github = {
      rest: {
        actions: { listWorkflowRunArtifacts: 'artifacts', listJobsForWorkflowRunAttempt: 'jobs' },
        issues: {
          listForRepo: 'issues', listComments: 'comments',
          createLabel: async () => {},
          create: async args => {
            const issue = { ...args, number: 1, html_url: 'https://example.com/issues/1' };
            issues.push(issue); return { data: issue };
          },
          update: async args => Object.assign(issues[0], args),
          createComment: async args => comments.push(args),
        },
      },
      paginate: async endpoint => ({
        artifacts: [{ name: 'arm64-reports-123-1', id: 7 }],
        jobs: [{ name: 'build', html_url: 'https://example.com/logs' }],
        issues, comments,
      })[endpoint],
    };
    const context = { repo: { owner: 'Vbitz', repo: 'neurocontainers-arm64' }, runId: 123 };
    const core = { summary: { addLink() { return this; }, async write() {} } };
    await report({ github, context, core });
    await report({ github, context, core });
    assert.equal(issues.length, 1);
    assert.equal(comments.length, 1);
    assert.match(comments[0].body, /2 passed/);
    assert.match(comments[0].body, /runtime check/);
    assert.match(comments[0].body, /artifacts\/7/);
    assert.match(comments[0].body, /Deploy checks and fulltest \| failure/);
    process.env.GITHUB_RUN_ATTEMPT = '2';
    process.env.BUILD_OUTCOME = 'failure';
    process.env.TEST_OUTCOME = 'skipped';
    fs.rmSync('results', { recursive: true });
    await report({ github, context, core });
    assert.equal(issues.length, 1);
    assert.equal(comments.length, 2);
    assert.match(comments[1].body, /Deploy checks and fulltest \| not run/);
    assert.match(comments[1].body, /Source metadata was unavailable/);
  } finally {
    process.chdir(original);
    fs.rmSync(temp, { recursive: true });
  }
});
