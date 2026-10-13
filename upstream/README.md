# Upstream ARM64 retesting

The 2026-10-12 assignment covers the exact **129 recipe/variants** that had fully
passing native ARM64 evidence at the historical accepted source
`e74050df0e4881833ae5d8d82b4e0ef287a14179`.

The user subsequently excluded ARM64 work for all OpenRecon recipes. Upstream's
`uses_openrecon` classification identifies **17 exclusions**, leaving **112
containers in the active goal**, each requiring its own upstream PR. The frozen
129-entry inventory is retained for auditability; exclusions are recorded as
`excluded-by-user` and do not count as verified or merged.

[queue.json](queue.json) freezes that inventory and records each container's
historical source/run/counts, current upstream review, candidate branch/SHA,
investigation deadline, attempts, native run, upstream PR, CI result and merge.
Historical success does not count as a retest of current upstream.
An independently revised and merged upstream PR can have newer source than its
root-workflow native run. Record that distinction as `root_current_source_gap`
and retain both sets of evidence; the earlier run does not verify the revised
source. Merged PR counts do not resolve such gaps or outstanding runtime followups.

The fork's `main` follows upstream by normal fast-forward pushes; the latest
synchronized SHA is recorded in `queue.json` under `last_fork_main_sync`. Existing
accepted port branches and the top-level accepted gitlink are preserved while
focused candidates are tested.
There are 80 recipes with fork changes and 49 without fork recipe changes.
Of those 49, upstream removed ARM64 declarations from five OpenRecon recipes;
those five are excluded by the user's scope correction. The other 44 still
declare ARM64.
All 129 current recipe paths exist. Of the 80 port patches, 45 apply directly,
21 more merge automatically against current upstream, and 14 require manual
reconciliation. These counts describe preparation, not verified builds.

Each in-scope container progresses through recipe review, local validation, native ARM64
Docker/SIF/deploy/fulltest verification, its own upstream PR,
upstream candidate tests for every declared variant, and merge. Review recipes
without fork changes for individually justified fixes or test improvements;
do not manufacture empty PRs or mark their upstream testing complete without
evidence. The user explicitly requires one PR per container; never combine
containers in a PR.

Fulltest-only PRs do not change image inputs. Supporting
[PR #3490](https://github.com/neurodesk/neurocontainers/pull/3490) now requires
Recipes CI verification of every declared variant for those PRs, using newly
built Docker images and SIFs. The required release gate checks those runtime
results while retaining the existing release plan: verification-only builds do
not publish images or release metadata. Inspect the actual reports and source
commit before merging each recipe PR.

Supporting [PR #3497](https://github.com/neurodesk/neurocontainers/pull/3497)
keeps current recipe suites out of the historical-release test workflow. Explicit
release JSON changes still select their release tests. Its summary handles both
single-artifact extraction into the destination root and multiple-artifact
subdirectories, while missing reports and failed tests still fail the gate.
For runtime verification, record the actual tested PR merge source separately
from the head SHA and verify its candidate parent and complete recipe tree.
A fulltest-only merge requires no new image publication or release metadata.

The user explicitly authorized upstream PRs and merges for this assignment.
Fork Actions remains disabled. The upstream `Container release gate` and
`Code quality` checks must pass, and actual container reports must have positive
test counts, zero failures and zero skips before merging. Do not invoke release
promotion or edit generated release metadata.

Keep at most four builds active, accounting for the upstream PR matrix as well
as local repository Actions. Never dispatch concurrent duplicates. Resume from
the recorded run/PR before starting another attempt. Per-recipe budgets remain
six total container build attempts and twelve hours, including the root ARM64
build and both architecture jobs in each upstream matrix. Upstream retries and
integration attempts also consume that budget; separate architecture counters
do not enlarge it.

On 2026-10-13, the user authorized **seven total builds for Code only**. Its
original attempts and deadline remain in force. The per-recipe
`max_build_attempts` and `build_budget_authorization` fields record this exception;
the default remains six for every other recipe.

Durable investigation notes belong in each linked `arm64-container` issue's
comments. `PLAN.md` records checkpoints. Coverage issue #2 continues to report
its own accepted architecture inventory and latest build evidence; its historic
129 total is separate from completion of this upstream submission queue.

Local checkout protection: upstream instruction files differ from the historical
checkout. They were read from git without changing any on-disk `AGENTS.md`.
The submodule index marks both instruction paths skip-worktree; preserve those
protections. Do not stage the working candidate gitlink as an accepted update.

Release metadata is tracked separately from native verification and PR merge.
[release-metadata-audit.json](release-metadata-audit.json) records trusted
promotion runs, the committed metadata paths and build dates, and comparisons
against promotion previews. ARM64 named variants use
`releases/<recipe>_arm64/<version>.json`, with explicit architecture and source
recipe fields. A merged recipe remains pending publication until promotion has
finished and the committed JSON matches the tested candidate. Automatic upstream
promotion is observed; generated release JSONs are never edited manually.

[inventory-release-metadata-audit.json](inventory-release-metadata-audit.json)
adds a read-only check of current-version ARM64 metadata across all112 in-scope
recipes at its recorded upstream commit. It distinguishes pending ARM64 ports,
missing current-version metadata and explicit named-variant metadata. Application
identity checks include the recipe's declared GUI launchers, matching
`builder/release.py`; build dates must agree across app entries. Metadata presence
is separate from exact-source runtime proof, publication manifests and public
artifact checks in the per-merge audit. Test-only PRs do not fill pre-existing
publication gaps or create a release candidate.

Per-command outcomes are reviewed alongside suite totals. Existing
`ignore_exit_code` settings can make a suite report success despite a crash or
missing capability. [runtime-exit-audit.json](runtime-exit-audit.json) records the
cached-report review, intentional negative cases, and required followups.
Unexpected nonzero exits require correction or a concrete blocker; documented
negative cases must assert their actual exit code and diagnostic. Prior merged
PR/source/publication evidence is retained in `prior_submissions` when a focused
followup is needed. Original attempt counts and deadlines persist. Publication
proof remains attached to its original image source; a test-only followup does
not create a new release.
