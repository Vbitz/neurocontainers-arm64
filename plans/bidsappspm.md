# bidsappspm: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.20`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The source BIDS wrapper packages compiled SPM12. The matching proprietary MATLAB Runtime has an Intel Linux target, and no Linux ARM runtime is established. Rebuilding the wrapper does not recompile or replace SPM's standalone runtime.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsappspm/build.yaml).
- Base image expression: `bids/spm:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/104). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/spm:v0.0.20`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/SPM upstream documentation](https://github.com/bids-apps/SPM/blob/master/README.md).
- [bids-apps/SPM Dockerfile](https://github.com/bids-apps/SPM/blob/master/Dockerfile).
- [bids-apps/SPM release v0.0.21](https://github.com/bids-apps/SPM/releases/tag/v0.0.21).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/spm/manifests/v0.0.20).

## Plan and acceptance criteria

Record the SPM revision and matching MCR release, then wait for a native runtime/application pair or an upstream-supported source execution route preserving the standalone behavior. Test a real SPM BIDS analysis if that prerequisite changes.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsappspm/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/104#issuecomment-5651281006).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
