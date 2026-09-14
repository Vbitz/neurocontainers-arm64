# conn: ARM64 research plan

Researched: 2026-09-13. Recipe version: `22a`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The pinned conn22a_glnxa64 archive is a compiled MATLAB application. CONN source exists and requires SPM/MATLAB, so there is no native Linux ARM runtime route established for this standalone distribution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/conn/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `conn22a_glnxa64_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/131). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [alfnie/conn upstream documentation](https://github.com/alfnie/conn/blob/master/readme.txt).
- [alfnie/conn release v25b](https://github.com/alfnie/conn/releases/tag/v25b).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Track CONN, SPM and MCR as one compatibility unit. Revisit upon an upstream-supported Linux ARM execution mode and validate an actual connectivity calculation and GUI workflow.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/conn/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/131#issuecomment-5651345334).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
