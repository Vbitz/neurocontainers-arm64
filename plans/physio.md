# physio: ARM64 research plan

Researched: 2026-09-13. Recipe version: `r2021a`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

TAPAS/PhysIO source is MATLAB code, while this recipe uses a compiled standalone and glnxa64 runtime paths. The proprietary Linux ARM runtime is unavailable for the deployed package. New TAPAS repository locations do not remove that requirement.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/physio/build.yaml).
- Base image expression: `ubuntu:16.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `spm12r8224_physioR2021a_standalone_MCRv99_MatlabR2020b_Linux_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/177). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [translationalneuromodeling/tapas upstream documentation](https://github.com/translationalneuromodeling/tapas/blob/master/README.md).
- [translationalneuromodeling/tapas release v6.1.0](https://github.com/translationalneuromodeling/tapas/releases/tag/v6.1.0).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Record the standalone release and runtime version. Revisit a supported native execution mode and validate physiological-noise regressor generation with the same inputs and output assertions.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/physio/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/177#issuecomment-5651354307).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
