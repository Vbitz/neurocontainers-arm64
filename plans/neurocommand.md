# neurocommand: ARM64 research plan

Researched: 2026-09-15. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The only identified architecture-specific input is the x86 Apptainer package. A candidate preserves the x86 package and builds the same Apptainer 1.4.4 release from source on ARM64 with the official Go AArch64 toolchain and documented non-setuid configuration. Native verification was blocked by workflow startup/API failures before a job ran, so the route remains unproven.

## Pinned recipe and evidence

- [Recipe at accepted source `04970417e995`](https://github.com/Vbitz/neurocontainers/blob/04970417e995232706f4ce85ddf4db23c79d4f25/recipes/neurocommand/build.yaml).
- [Apptainer upstream](https://github.com/apptainer/apptainer).
- Prepared candidate `438050de3f8e251edf8a6f8ae454e15731e15984` on the `arm64/neurocommand` branch.
- First dispatch [run 34749429556](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34749429556) ended in `startup_failure`; the permitted retry returned HTTP 500 without creating a run.

## Plan and acceptance boundary

Replay the candidate's intended recipe commit onto the current accepted pin and dispatch it now that later native workflow runs demonstrate the dispatch path is healthy. Require Docker build, architecture verification, SIF conversion, deploy checks and the complete existing fulltest. If the source build reaches a real Apptainer portability error, record that first actionable upstream blocker; do not claim ARM64 support from the earlier setup failures.

## Implementation and retry — 2026-09-15

The current-pin candidate `d374656887d77c959e710b8a773f7b37925bb41b` reached
the ARM64 Apptainer build successfully in [run 34928349450](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34928349450),
then stopped in the Miniconda template because the ARM Conda `datalad` package
requires `git-annex`, which is absent from the Linux AArch64 Conda channel.
The image already installs native Ubuntu `git-annex`, so this is a targeted
recipe packaging issue. Candidate `e74050df0e4881833ae5d8d82b4e0ef287a14179`
keeps the x86_64 Conda path and installs ARM64 Datalad from PyPI after removing
it from the ARM Conda solve. Validation and both architecture generations pass.

This is attempt 2/6 in the reopened window. Require a new native build, SIF,
deploy checks and the complete fulltest before accepting the route.
