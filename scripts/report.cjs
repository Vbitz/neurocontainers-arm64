// Runs in a separate job: recipe execution never receives the issues token.
const fs = require('node:fs');

function readJson(path) {
  try { return JSON.parse(fs.readFileSync(path, 'utf8')); }
  catch { return {}; }
}

module.exports = async function report({ github, context, core }) {
  const { owner, repo } = context.repo;
  const env = process.env;
  const runId = context.runId;
  const attempt = env.GITHUB_RUN_ATTEMPT || '1';
  const base = `https://github.com/${owner}/${repo}`;
  const runUrl = `${base}/actions/runs/${runId}/attempts/${attempt}`;
  const metadata = readJson('results/metadata.json');
  const results = readJson('results/test-results.json');
  const recipe = env.RECIPE;
  const variant = env.VARIANT;
  // Keep the same issue even if validation fails before an identity is resolved.
  const title = `[ARM64] ${recipe} (${variant})`.slice(0, 256);
  const marker = `<!-- arm64-container:${encodeURIComponent(recipe)}:${encodeURIComponent(variant)} -->`;
  const resultMarker = `<!-- arm64-run:${runId}:${attempt} -->`;
  const artifacts = await github.paginate(github.rest.actions.listWorkflowRunArtifacts,
    { owner, repo, run_id: runId, per_page: 100 });
  const jobs = await github.paginate(github.rest.actions.listJobsForWorkflowRunAttempt,
    { owner, repo, run_id: runId, attempt_number: Number(attempt), per_page: 100 });
  const buildJob = jobs.find(job => job.name === 'build');
  const status = value => value && value !== 'skipped' ? value : 'not run';
  let body = `${resultMarker}\n### Run ${runId}, attempt ${attempt}\n\n` +
    `Container: **${env.CONTAINER || `${recipe} (${variant})`}**\n\n` +
    '| Check | Result |\n| --- | --- |\n' +
    `| Build job | ${status(env.BUILD_RESULT)} |\n` +
    `| ARM64 Docker build and SIF conversion | ${status(env.BUILD_OUTCOME)} |\n` +
    `| Deploy checks and fulltest | ${status(env.TEST_OUTCOME)} |\n\n`;
  if (results.total_tests !== undefined) {
    body += `Tests: **${results.passed || 0} passed**, **${results.failed || 0} failed**, ` +
      `**${results.skipped || 0} skipped**, ${results.total_tests} total.\n\n`;
  }
  const failures = (results.test_results || []).filter(test =>
    test.status === 'failed' || test.status === 'error');
  if (failures.length) {
    body += 'Failed checks:\n\n' + failures.slice(0, 20).map(test =>
      `- ${String(test.name || test.test_name || 'Unnamed check').replace(/[\r\n]/g, ' ')}`
    ).join('\n') + '\n\n';
  }
  if (metadata.source_sha) {
    body += `Source: [Vbitz/neurocontainers@${metadata.source_sha.slice(0, 12)}]` +
      `(https://github.com/Vbitz/neurocontainers/commit/${metadata.source_sha})` +
      `; version: ${metadata.version}.\n\n`;
  } else {
    body += `Requested fork ref: ${env.SOURCE_REF || 'committed submodule revision'}. ` +
      'Source metadata was unavailable; see setup/validation logs.\n\n';
  }
  body += `[Workflow run](${runUrl}) · [Logs](${buildJob?.html_url || runUrl})\n\n`;
  const currentArtifacts = artifacts.filter(a => a.name.endsWith(`-${runId}-${attempt}`));
  body += currentArtifacts.length ? currentArtifacts.map(a =>
    `- [${a.name}](${base}/actions/runs/${runId}/artifacts/${a.id})` +
    (a.expired ? ' (expired)' : '')).join('\n') : 'No artifacts were produced.';
  body += '\n\nReports expire after 14 days; SIF artifacts after 7 days. ' +
    'A retained image from a failed run has not passed validation.\n';
  try {
    await github.rest.issues.createLabel({ owner, repo, name: 'arm64-container',
      color: '1d76db', description: 'ARM64 container build and test history' });
  } catch (error) { if (error.status !== 422) throw error; }
  const issues = await github.paginate(github.rest.issues.listForRepo,
    { owner, repo, state: 'all', labels: 'arm64-container', per_page: 100 });
  let issue = issues.find(issue => !issue.pull_request && issue.body?.includes(marker));
  const issueBody = `${marker}\nBuild and test history for **${recipe} / ${variant}**. ` +
    'Each completed dispatch posts a result below.\n\nLatest reported result:\n\n' + body;
  if (!issue) {
    ({ data: issue } = await github.rest.issues.create({ owner, repo, title,
      labels: ['arm64-container'], body: issueBody }));
  } else {
    await github.rest.issues.update({ owner, repo, issue_number: issue.number,
      body: issueBody });
  }
  const comments = await github.paginate(github.rest.issues.listComments,
    { owner, repo, issue_number: issue.number, per_page: 100 });
  if (!comments.some(comment => comment.body?.includes(resultMarker))) {
    await github.rest.issues.createComment({ owner, repo, issue_number: issue.number, body });
  }
  await core.summary.addLink('Container build and test issue', issue.html_url).write();
};
