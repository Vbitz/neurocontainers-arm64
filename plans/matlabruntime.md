# matlabruntime: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2025b`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The recipe supplies MATLAB Runtime R2025b and explicitly requires glnxa64 library trees. The vendor platform matrix does not supply a matching Linux ARM runtime. This is a proprietary runtime distribution blocker, not a source compilation task.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/matlabruntime/build.yaml).
- Base image expression: `containers.mathworks.com/matlab-runtime:r{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/209). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Wait for a vendor Linux ARM runtime matching the compiled applications to be supported. Verify an actual compiled MATLAB application when that changes; ARM runtime directory stubs or Mac libraries cannot satisfy the requirement.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/matlabruntime/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/209#issuecomment-5651533575).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
