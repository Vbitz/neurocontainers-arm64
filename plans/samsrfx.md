# samsrfx: ARM64 research plan

Researched: 2026-09-13. Recipe version: `v10.004`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

SamSrf X source exists, but this recipe deploys its MATLAB-compiled standalone. The missing matching Linux ARM runtime blocks that deployment; source availability alone does not supply MATLAB toolboxes and compiled runtime behavior.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/samsrfx/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `samsrf_v10_004_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/178). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [samsrf/samsrf upstream documentation](https://github.com/samsrf/samsrf/blob/master/ReadMe.md).
- [samsrf/samsrf release v10.3](https://github.com/samsrf/samsrf/releases/tag/v10.3).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Record the standalone/MCR pairing. Revisit an upstream native route and validate receptive-field fitting with the same optimization settings and expected outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/samsrfx/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
