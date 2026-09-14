# exploreasl: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.11.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

ExploreASL source is available, but this recipe invokes a compiled standalone application through MCR v97. Linux ARM MATLAB Runtime is not available in the documented platform matrix. Rebuilding the shell wrapper cannot solve that requirement.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/exploreasl/build.yaml).
- Base image expression: `exploreasl/xasl:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/143). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `exploreasl/xasl:1.11.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [ExploreASL/ExploreASL upstream documentation](https://github.com/ExploreASL/ExploreASL/blob/main/README.md).
- [ExploreASL/ExploreASL release v1.11.0](https://github.com/ExploreASL/ExploreASL/releases/tag/v1.11.0).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/exploreasl/xasl/manifests/1.11.0).

## Plan and acceptance criteria

Record the standalone/runtime pair and revisit an upstream-supported Linux ARM execution route. Require an actual ASL analysis and CBF output comparison before marking the container supported.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/exploreasl/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/143#issuecomment-5651347712).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
