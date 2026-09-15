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
