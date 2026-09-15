# NeuroContainers ARM64

Build and test one ARM64 container at a time while expanding
[NeuroContainers](https://github.com/neurodesk/neurocontainers) support.
Recipes and their tests live in [Vbitz/neurocontainers](https://github.com/Vbitz/neurocontainers),
included here as a pinned submodule. This repository owns the manual Actions workflow.

The [recipe coverage tracker](https://github.com/Vbitz/neurocontainers-arm64/issues/2)
lists every recipe in a table with native ARM64 build results, full test results,
plan feasibility, and evidence links. Summary counts appear below the table.

## Build a container

Open [Build and test one ARM64 container](https://github.com/Vbitz/neurocontainers-arm64/actions/workflows/build-arm64.yml)
and select **Run workflow**, or run:

```sh
gh workflow run build-arm64.yml -R Vbitz/neurocontainers-arm64 \
  -f recipe=dcm2niix
```

- `recipe`: one directory under `neurocontainers/recipes`. `workshopdemo` is a
  small pipeline check; it does not establish support for a scientific tool.
- `neurocontainers_ref`: optional branch, tag, or commit in **Vbitz/neurocontainers**.
  Blank uses this repository's committed submodule revision. The resolved SHA
  is recorded in the run summary and `metadata.json`.
- `variant`: defaults to `arm64`. Named alternatives such as `gpu_arm64` are
  accepted only when the recipe declares them and they resolve to `aarch64`.
  The runner has no GPU.
- `upload_image`: retain the built Apptainer SIF for seven days; defaults to true.

The workflow runs on GitHub's native `ubuntu-24.04-arm` runner. It stages and
builds with `--platform linux/arm64`, verifies the image architecture, converts
that exact local Docker image to SIF, and runs the upstream deploy checks and
the recipe's **fulltest.yaml** against it. Missing/empty suites, mismatched
suite versions, unsupported architectures, and failed builds/tests fail the run.
No existing published container is substituted. Logs and JSON test reports are
retained for 14 days, including on failure. Images are artifacts, not registry releases.

Only manual dispatch starts builds: there are no push, PR, or scheduled triggers.
The build job needs no registry credentials and has a read-only GitHub token.
A separate reporting job has permission to maintain one `arm64-container` issue
per recipe/variant. Every finished run updates its latest result and adds a
history comment with build/test outcomes, test counts, source commit, and links
to the run, logs, and artifacts. Setup/build failures are reported too, with
tests shown as not run. Re-running a job does not duplicate an existing result
for the same run attempt. Builds for the same recipe/variant are serialized;
GitHub may replace an older pending dispatch if several are queued at once.
Large builds may exceed the hosted runner's disk/memory capacity or the six-hour
job limit; treat those as infrastructure failures when assessing ARM64 support.

## Develop recipes in the fork

```sh
git clone --recurse-submodules https://github.com/Vbitz/neurocontainers-arm64.git
cd neurocontainers-arm64
uv sync --project neurocontainers --frozen
git -C neurocontainers switch -c arm64/my-tool
```

Read [the recipe development guide](neurocontainers/AGENTS.md). Make recipe and
`fulltest.yaml` changes inside the submodule, validate them there, then commit
and push to the fork:

```sh
git -C neurocontainers add recipes/my-tool
git -C neurocontainers commit -m "Support ARM64 builds and runtime tests for my-tool"
git -C neurocontainers push -u origin arm64/my-tool
gh workflow run build-arm64.yml -R Vbitz/neurocontainers-arm64 \
  -f recipe=my-tool -f neurocontainers_ref=arm64/my-tool
```

After verifying the run, pin the tested recipe revision here:

```sh
git add neurocontainers
git commit -m "Pin tested ARM64 recipe updates"
git push
```

Keep build orchestration changes here and recipe/test/builder changes in the
fork so contributions can later be proposed upstream. Add `aarch64` to a recipe
while developing the port, but regard support as verified only after the actual
ARM64 build and meaningful runtime tests pass.

## Fork CI policy

GitHub Actions is **disabled at repository level** on Vbitz/neurocontainers.
Upstream workflow files remain intact for syncing and upstream contributions.
This also disables any newly added workflows there. Check the setting with:

```sh
gh api repos/Vbitz/neurocontainers/actions/permissions
# Expected: "enabled": false
```

If restoring this setup later:

```sh
gh api --method PUT repos/Vbitz/neurocontainers/actions/permissions -F enabled=false
```

## Refresh the coverage tracker

The Python script fetches all `build-arm64.yml` runs, all `arm64-container` issues
(including closed issues), and their full comment history. It recovers job-step
outcomes for attempts missing a report. It reads the recipe inventory from the
committed submodule pin and research assessments from committed `plans/*.md`, so
an agent's checked-out candidate does not change the inventory. It requires only
Python's standard library and an authenticated `gh` CLI.

```sh
# Generate the table and update issue #2 in one command.
python3 scripts/tracking_issue.py --write

# Preview and save the GitHub evidence for repeatable offline review.
python3 scripts/tracking_issue.py --snapshot /tmp/arm64-evidence.json \
  --output /tmp/arm64-tracker.md
python3 scripts/tracking_issue.py --from-snapshot /tmp/arm64-evidence.json \
  --output /tmp/arm64-tracker.md
```

Without `--write`, the script only generates Markdown (stdout or `--output`).
With `--write`, it replaces the tracker body and verifies the update by reading it
back; comments are preserved. The issue must have the coverage tracker marker.
Saved snapshots include the documentation revision and accepted recipe pin's
parent revision, so offline replay uses the same inventory and plans.

Build/test columns use the latest completed attempt per recipe/variant and link
active runs and earlier fully passing results separately. A test success requires
a positive count, no failures and no skips; missing counts remain unknown. A
setup failure is not evidence that the application cannot build. Results describe
the linked tested commit, not a published release or automatic verification of
the current accepted pin. Plan assessments distinguish plausible routes,
unresolved dependencies and prerequisites; they do not infer impossibility from
an absent ARM64 declaration. New assessment wording must be added explicitly to
the script's mapping. The tracker is a snapshot and is not updated by builds.

## Check the orchestration locally

```sh
uv run --project neurocontainers --frozen python -m unittest discover -s tests
node --test tests/report.test.cjs
actionlint
cd neurocontainers
uv run --frozen python ../scripts/arm64.py prepare --recipe workshopdemo
# The next two commands need a native Linux ARM64 host with Docker Buildx,
# Apptainer, DataLad (in the Python environment), and git-annex installed.
uv run --frozen python ../scripts/arm64.py build
uv run --frozen python ../scripts/arm64.py test
```
