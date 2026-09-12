# ARM64 container porting workflow

## Objective and scope

Increase the number of NeuroContainers recipes that build and pass meaningful
runtime tests on native Linux ARM64. Prefer many small, maintainable recipe
fixes over a deep port of one difficult dependency. The user starts the Luna
agent separately; do not start another agent, delegate, or change models.

This workflow is intended to run unattended for one to two weeks.
Work autonomously within the user's active goal. A blocked recipe is a recorded
outcome: move to the next eligible recipe rather than ending the overall task.
Do not claim the overall goal is complete while eligible work remains. Follow
the host's goal lifecycle rules; this file does not override them. Respect any
user-specified priority or budget over the defaults below.

## Non-negotiable rules

- **Never modify `AGENTS.md` during the porting run.** This applies to every file
  named `AGENTS.md` in this repository, the submodule, and any worktree. Reading
  is required where applicable. Do not create, edit, overwrite, delete, rename,
  format, stage, commit, or indirectly modify one with a script or generator.
  Do not undo pre-existing user changes to it. Do not change these instructions
  to relax a budget or bypass a stopping rule. Only a new explicit user request
  to edit the instructions permits changes.
- `PLAN.md` is allowed for a durable local work queue and handoff notes. Preserve
  any existing user content. GitHub issues remain the record of build evidence
  and blockers; mirror essential progress there.
- Recipe, fulltest, and necessary shared builder fixes belong in
  `neurocontainers/`, whose origin must be `Vbitz/neurocontainers`. Read
  `neurocontainers/AGENTS.md` and applicable nested instructions before editing.
  Orchestration and documentation belong in this top-level repository.
- Keep Actions disabled at repository level on **Vbitz/neurocontainers**. Do
  not remove its upstream workflows or enable CI there. Never push to
  `neurodesk/neurocontainers` or open upstream PRs as part of this workflow.
- Use this repository's `build-arm64.yml`, native `ubuntu-24.04-arm`, and
  `linux/arm64`. No QEMU/x86 emulation, `--ignore-architectures`, substituted
  published images, or skipped test gates as evidence of ARM64 success.
- Do not port third-party libraries, write ARM assembly/intrinsics, redesign
  dependency build systems, or maintain private compiler/runtime forks.
- Preserve scientific functionality, existing x86_64 support, and test rigor.
  Do not replace a tool with a different implementation to obtain a green run.
- Never edit generated release JSONs or claim that a tested build is a published
  release. This workflow builds candidates and artifacts; registry publishing
  and release promotion are outside this task.
- Preserve unrelated user changes. Do not force-push, reset destructively, or
  stage whole repositories with `git add .` or `git add -A`.

## Start or resume

1. Inspect status, branches, and remotes in both repositories. Read `README.md`
   and this file. Check existing runs before dispatching anything new.
2. Verify fork Actions remains disabled:

   ```sh
   gh api repos/Vbitz/neurocontainers/actions/permissions
   ```

   Expect `"enabled": false`. If it has been enabled, restore the authorized
   setting before pushing recipe work:

   ```sh
   gh api --method PUT repos/Vbitz/neurocontainers/actions/permissions -F enabled=false
   ```

3. Read [coverage issue #2](https://github.com/Vbitz/neurocontainers-arm64/issues/2)
   and relevant `arm64-container` issues. Read comments as well as issue bodies.
   The reporter replaces per-container issue bodies on each run; durable human
   or agent notes belong in comments.
4. Read `PLAN.md` if present, reconcile it with actual branch/run/issue state,
   and update the work queue without overwriting user-written objectives. Record
   the current top-level commit and pinned submodule SHA. Install the
   existing locked environment with `uv sync --project neurocontainers --frozen`.
   Do not refresh dependency versions as a routine setup step.
5. Resume the last in-progress recipe/run from its issue. Do not repeat a
   blocked attempt unless new evidence changes the reason it was blocked.

The coverage checkboxes mean **declared ARM64 support**, not verified support.
An ARM64 release JSON link is historical evidence, not proof that the current
recipe works. Confirm current behavior using the exact tested fork commit.

## Select work

- First establish which already-declared ARM64 recipes actually pass. Prefer
  small CLI tools, existing ARM64 packages, and recipes with focused tests.
- Then port recipes with official ARM64 binaries, multi-architecture base
  images, conda-forge packages, Python wheels, or documented portable builds.
- Inspect the recipe, downloads, base image, templates, deploy entries, and
  fulltest before spending runner time. Look for x86-only URLs, wheel tags,
  conda subdirs, hardcoded CPU flags, proprietary installers, and GPU requirements.
- Use official upstream release/build documentation to check compatibility.
  Do not guess a download URL, checksum, package version, or supported platform.
- Leave GPU-only, unavailable licensed software, abandoned native dependencies,
  and known deep compiler ports for a blocked report or later human review.
  A runnable CPU variant can be considered if the tool officially supports it.
- Keep up to **four recipes/builds in progress concurrently**. This is parallel
  recipe work by the user-started agent, not permission to spawn subagents. Use
  another ready recipe while builds wait. Start smaller if disk, API limits,
  runner availability, or reliable bookkeeping requires it.
- Never run two attempts of the same recipe/variant concurrently. Do not queue
  the entire inventory or enqueue speculative retries. Refill available slots
  after reviewing completed results and posting their outcomes.

## Per-recipe loop

### 1. Establish a clean baseline

Inspect its existing issue and runs. Record the recipe, variant, baseline SHA,
known ARM64 evidence, and proposed change. Start a recipe branch from the
**current top-level pinned submodule commit**, which includes previous accepted
ports. Do not start every port from stale fork `main` and lose earlier successes.

Use the existing **single `neurocontainers/` checkout**, with one branch per
recipe. Make local edits, validations, commits, and branch switches sequentially.
Parallelism comes from GitHub Actions: each dispatched build independently checks
out its immutable candidate SHA, so switching local branches cannot change it.
Do not create worktrees by default. They are only useful if simultaneous local
editing/building is later requested.

Before switching branches, finish or safely commit your current edits and ensure
no local process is still reading that checkout. Never stash or discard unrelated
user changes. From the top-level checkout, with the submodule clean:

```sh
recipe=dcm2niix  # Replace with one actual recipe directory name.
base_sha=$(git rev-parse HEAD:neurocontainers)
git -C neurocontainers switch -c "arm64/$recipe" "$base_sha"
```

After pushing and dispatching this recipe's exact SHA, record its branch and run
ID, then use the same checkout for another recipe while the remote build runs.
When a result arrives, switch back to its recorded branch before making a fix.
The top-level working tree will show a changed submodule pointer during candidate
work; stage that pointer only during the explicit acceptance step.

If that branch already exists, inspect and resume it or choose a new descriptive
branch name; do not overwrite it. Record the baseline SHA in the issue notes.

### 2. Make the smallest plausible port

Prefer architecture-conditional changes that preserve the x86_64 path:

- Select a published ARM64 asset and pin its version/checksum as appropriate.
- Use an upstream-supported ARM64 package or multi-architecture base image.
- Correct a package name, install a documented build dependency, or use a
  documented portable/generic CPU build flag.
- Build pinned upstream source only if upstream supports ARM64 or a portable
  build and the change is ordinary recipe configuration.

Add `aarch64` to the recipe while developing the candidate. Keep unsupported
experimental declarations off the accepted top-level pin. Follow the recipe
rules for declared downloads and `get_file`, explicit versions, deployment,
icons, update policies, and writable runtime locations.

Keep `fulltest.yaml` name/version aligned with `build.yaml`. Preserve existing
functional assertions. Add a small real operation with an output assertion
where existing tests only check file presence or help text. Do not mask failures
with `|| true`, indiscriminate `ignore_exit_code`, deleting failing tests, or
loosening numerical tolerances without a documented scientific justification.
A legitimately unusual exit code may be asserted alongside meaningful output.

### 3. Validate, commit, and push the candidate

Run the applicable validation required by the submodule guide. At minimum,
validate the edited recipe and generate its ARM64 Dockerfile. Regenerate the
x86_64 variant as well when the recipe supports it; inspect that changes have
not broken its configuration. Generation alone is not runtime verification.

Example from `neurocontainers/`:

```sh
uv run --frozen python builder/validation.py "recipes/$recipe/build.yaml"
uv run --frozen python -m builder generate "$recipe" --architecture aarch64 --variant arm64 --recreate
```

For shared builder changes, run relevant builder tests and required broader
checks. Record pre-existing unrelated validation failures instead of expanding
this port into an unrelated cleanup project.

Review `git diff` and the explicit staged file list. Ensure no `AGENTS.md` is
included. Commit only the intended recipe/test files to the fork branch, then
push it to the fork. Do not update the top-level submodule pointer yet.

### 4. Dispatch the exact commit and wait for the result

From the top-level checkout:

```sh
candidate_sha=$(git -C neurocontainers rev-parse HEAD)
gh workflow run build-arm64.yml -R Vbitz/neurocontainers-arm64 \
  -f recipe="$recipe" -f variant=arm64 \
  -f neurocontainers_ref="$candidate_sha" -f upload_image=false
```

Use the actual declared selector for a named ARM64 variant. The runner has no
GPU. Default to `upload_image=false` for exploratory work; reports are still
retained. Enable image retention only when useful for debugging or requested.

Find the dispatched run with `gh run list`, inspect its inputs/source metadata,
and save its URL/ID. Do not assume the newest run belongs to you when other runs
exist. Monitor the build and report jobs with `gh run view`. Avoid rapid polling;
use roughly 30–60 second intervals and provide useful progress updates. Do not
cancel a healthy build because compilation takes time; normal builds may run
for an hour or longer, up to the existing job timeout.

A successful port requires all of the following:

- The intended candidate SHA was built on native ARM64.
- Docker build, architecture verification, and SIF conversion succeeded.
- Deploy checks and the fulltest suite passed against that newly built SIF.
- The per-container issue contains outcomes, test counts, source SHA, and
  working run/log/artifact links. Review skips; a skipped essential capability
  is not verified functionality.

If reporting fails after testing, recover the evidence from the run and repair
or retry reporting; do not rebuild a successful image just to post a comment.

### 5. Diagnose failures with a strict budget

Read the first actionable error and surrounding log, not just the final
`make`/`ninja` exit code. Classify the failure before changing anything.

**Per recipe, per investigation:** allow up to **12 hours elapsed**, including
queue/build waits, with at most **six build attempts**. Start the clock when the
recipe first enters active investigation. Track separate clocks for parallel
recipes. At the limit, stop new edits and dispatches, record the outcome, and
move on. Let a healthy already-running job finish within its configured timeout,
then record its result; do not start another attempt.

Budgets persist across turns, restarts, and integration retries. Record the
start timestamp, deadline, attempts, current run ID, and next action in the
issue and `PLAN.md`. Do not reset a budget by renaming the branch or making
cosmetic edits. Twelve hours is an upper bound, not a target: stop immediately
when the next step would require an upstream library port. Spend at most
30 minutes classifying an individual native dependency compilation failure;
allow no more than two documented configuration/upstream-release fixes for
that dependency before recording it as blocked.

- **Recipe/configuration:** a wrong asset, missing documented system package,
  compiler selection, or supported build option may justify a targeted retry.
- **Upstream library/compiler port:** unsupported intrinsics, assembly, JIT,
  ABI/endian assumptions, unsupported architecture guards, or cascading native
  dependency compile failures are a stopping condition. Record the dependency,
  version, and first error, then move on. Do not investigate that dependency's
  internals or write compatibility patches. A directly applicable, released
  upstream fix or documented ARM64 flag may be tried within the same budget;
  speculative patch chains and dependency-version roulette are prohibited.
- **Infrastructure/data:** disk full, OOM, unavailable downloads/test data,
  registry throttling, or runner failures do not prove the application cannot
  run on ARM64. Allow at most one unchanged retry for a clearly transient
  failure, counted within the six-attempt limit. Persistent resource failures
  need an infrastructure-blocked report, not smaller or disabled tests.
- **Runtime/scientific:** a crash, missing required feature, wrong output, or
  essential skipped test is a failed port until correctly fixed and retested.
- **License/GPU/external access:** record the unavailable prerequisite. Never
  bypass access controls or replace a required capability with a stub.

Every retry needs a written hypothesis and evidence explaining why the change
addresses the observed error. Stop early if the next step is deep library work,
regardless of unused budget. Revisit only with a concrete upstream fix, changed
infrastructure, or an explicit new instruction from the user.

### 6. Record the outcome and preserve accepted work

Use the one `arm64-container` issue per recipe/variant. Search before creating
one. The workflow creates it after a dispatch; create one yourself only when
preflight blocks a recipe before a run exists. Use the existing title/label and
marker convention so later automation reuses it:

```text
Title: [ARM64] RECIPE (arm64)
Label: arm64-container
Body marker: <!-- arm64-container:RECIPE:arm64 -->
```

Put investigation notes in an issue **comment**, with:

- Outcome: verified, blocked-upstream, blocked-infrastructure,
  blocked-prerequisite, failed-runtime, or in-progress.
- Baseline/candidate SHA, fork branch, recipe version, and variant.
- Run links, build/test outcomes and counts, and first actionable error.
- Changes attempted, attempt count, start/deadline timestamps, elapsed time, and next action.
- For blocked work, the concrete condition that would justify revisiting it.

Use a body file for multiline `gh issue comment` text. Keep concise failure
excerpts in the comment because artifacts expire. Never put notes only in the
reporter's overwritten issue body. Keep `PLAN.md` synchronized with issue links
and run IDs so a restarted agent can resume without rediscovering work.

**Verified:** ensure the successful candidate is pushed to the fork. Integrate
accepted work **serially**, using the current accepted pin as the base. If the
candidate descends from it, advance to the tested candidate. If another parallel
port has advanced the pin, cherry-pick only this recipe's intended commits onto
the new accepted base in a clean integration branch. Never replace the pin with
an older divergent branch and lose accepted ports.

Resolve routine recipe conflicts carefully. Revalidate and dispatch the exact
integrated commit for this recipe before accepting it; do not present an earlier
candidate's green run as verification of a different commit. Shared builder or
template changes require identifying and retesting affected accepted recipes;
defer a broad change if that exceeds the available scope/budget. Integration
retries count toward the recipe budget.

Once the integrated candidate passes, push it to the fork, then commit and push
the top-level submodule pointer. Record the accepted SHA and verification run.
New recipe branches start from this accepted pointer; existing candidate branches
keep their recorded baselines until integration. Never modify `AGENTS.md` while resolving conflicts.

**Blocked/failed:** preserve useful committed experiments on their fork branch
and document them. Do not pin the failed candidate here. After accounting for
local changes, switch the checkout to the latest accepted pin or the next
recipe's branch. Keep the failed branch available for inspection. Do not restore
an old top-level pin that predates other accepted ports. Never discard user
edits. An untested shared builder change must not ride along with the next port.

After an accepted pin, refresh coverage issue #2 using the documented
`scripts/tracking_issue.py` commands in `README.md`. Checkboxes remain based on
architecture declarations, and release links remain ARM64-only. Do not invent
release metadata or tick checkboxes manually to represent successful testing.

## Session checkpoints and completion

Before switching recipes or ending a session, leave a concise issue comment
with the current state and remaining action. Confirm there are no unaccounted
running jobs, unpushed intended commits, or accidentally changed submodule pins.
Keep every `AGENTS.md` untouched. Update `PLAN.md` with the queue and checkpoint,
including the checked-out branch, queued/active recipe branches, baseline and
candidate SHAs, run/issue URLs,
per-recipe deadlines and attempts, accepted integration SHA, and next actions.
Checkpoint after every dispatch, completed run, blocked decision, and accepted
pin. Prefer incremental updates over rewriting the user's plan.

For the week-long run, revisit the queue at least daily: reconcile completed
runs, recover failed reporting, verify fork CI remains disabled, and identify
blocked dependencies shared by several recipes. Record one reusable blocker
explanation and link affected issues instead of repeating the same investigation.
Do not repeatedly poll known-blocked work or manufacture retries to fill slots.
If a goal continuation resumes with a partial checkpoint, inspect actual GitHub
and git state before acting; never redispatch solely because memory is missing.

Summarize verified recipes, blocked recipes with reasons, active run URLs, and
the next candidate. Continue to other eligible work after a recipe is blocked.
When the requested inventory has been assessed, report remaining blockers
honestly; do not equate “attempted everything” with “all containers work.”

For changes to this repository's orchestration, use:

```sh
uv run --project neurocontainers --frozen python -m unittest discover -s tests
node --test tests/report.test.cjs
actionlint
```
