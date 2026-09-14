# brainstorm: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.211130.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

Brainstorm source is public, but the recipe runs a compiled 2020a MATLAB Runtime distribution. The missing Linux ARM runtime is the fundamental dependency for this standalone packaging, rather than the Brainstorm scripts themselves.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/brainstorm/build.yaml).
- Base image expression: `ubuntu:18.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `brainstorm3_211130_mcr2020a_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/125). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [brainstorm-tools/brainstorm3 upstream documentation](https://github.com/brainstorm-tools/brainstorm3/blob/master/README.md).
- [brainstorm-tools/brainstorm3 release 3.260601](https://github.com/brainstorm-tools/brainstorm3/releases/tag/3.260601).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Keep the compiled application and runtime paired. Revisit a native standalone release or documented compatible interpreter route; validate electrophysiology import and a real analysis/export as well as GUI startup.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/brainstorm/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/125#issuecomment-5651344115).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
