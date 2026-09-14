# spm25: ARM64 research plan

Researched: 2026-09-13. Recipe version: `25.01.02`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The recipe inherits the SPM MATLAB-based container. Upstream supplies source and Apple Silicon standalone packages, but the Linux standalone/runtime target remains Intel. Neither an ARM Mac download nor recompiling the wrapper supplies the required Linux runtime.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/spm25/build.yaml).
- Base image expression: `ghcr.io/spm/spm-docker:docker-matlab-{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/175). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `ghcr.io/spm/spm-docker:docker-matlab-25.01.02`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [spm/spm upstream documentation](https://github.com/spm/spm/blob/main/README.md).
- [spm/spm release 26.01.rc1](https://github.com/spm/spm/releases/tag/26.01.rc1).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://ghcr.io/v2/spm/spm-docker/manifests/docker-matlab-25.01.02).

## Plan and acceptance criteria

Track the exact 25.01.02 source/container and MCR pairing. Revisit a native Linux ARM standalone release or documented fully compatible execution mode, then validate a real SPM workflow.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/spm25/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/175#issuecomment-5651353961).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
