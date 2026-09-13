# hmri: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The source hMRI toolbox exists, but the recipe uses a standalone archive and R2023b glnxa64 runtime. A matching Linux ARM MATLAB Runtime is not provided by the documented vendor platform matrix.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/hmri/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `matlabmcr 2023b`.
- Declared download inputs: `standalone_hmri_toolbox_tarball`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/146). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [hMRI-group/hMRI-toolbox upstream documentation](https://github.com/hMRI-group/hMRI-toolbox/blob/master/README.md).
- [hMRI-group/hMRI-toolbox release v1.0.0](https://github.com/hMRI-group/hMRI-toolbox/releases/tag/v1.0.0).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Retain the current standalone/runtime dependency as the blocker. Revisit with a supported native execution mode and validate quantitative parameter maps using the same processing settings and reference data.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/hmri/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
