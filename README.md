# NeuroContainers ARM64

Build and test one ARM64 container at a time while expanding
[NeuroContainers](https://github.com/neurodesk/neurocontainers) support.
Recipes and their tests live in [Vbitz/neurocontainers](https://github.com/Vbitz/neurocontainers),
included here as a pinned submodule. This repository owns the manual Actions workflow.

The [recipe coverage tracker](https://github.com/Vbitz/neurocontainers-arm64/issues/2)
lists every recipe. Checkboxes indicate declared ARM64 support; linked container
issues hold actual build/test evidence.

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

After committing recipe changes and updating the submodule pin, regenerate the
checklist from the fork's architecture resolver. This includes named variants
and links the latest available ARM64 release JSON and existing container result issues.
Release links require explicit ARM64 metadata and are pinned to the source revision.
The tracker is a snapshot, not
automatically updated by builds; checkboxes do not imply verified runtime support.

```sh
gh issue list -R Vbitz/neurocontainers-arm64 --state all \
  --label arm64-container --limit 1000 --json body,url > /tmp/arm64-issues.json
uv run --project neurocontainers --frozen python scripts/tracking_issue.py \
  --issues-json /tmp/arm64-issues.json > /tmp/arm64-tracker.md
gh issue edit 2 -R Vbitz/neurocontainers-arm64 --body-file /tmp/arm64-tracker.md
```

This replaces the tracker body; keep investigation notes in comments or the
individual container issues.

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
