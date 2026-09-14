# bidsappbrainsuite: ARM64 research plan

Researched: 2026-09-13. Recipe version: `23a`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The BIDS wrapper source exists but uses a precompiled parent image. This recipe explicitly loads BrainSuiteMCR glnxa64 libraries. A native build of some BrainSuite C++ tools would not replace the compiled MATLAB pipeline required by the wrapper.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsappbrainsuite/build.yaml).
- Base image expression: `bids/brainsuite:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/101). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/brainsuite:v23a`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/BrainSuite upstream documentation](https://github.com/bids-apps/BrainSuite/blob/master/README.md).
- [bids-apps/BrainSuite Dockerfile](https://github.com/bids-apps/BrainSuite/blob/master/Dockerfile).
- [bids-apps/BrainSuite release v23a](https://github.com/bids-apps/BrainSuite/releases/tag/v23a).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/brainsuite/manifests/v23a).

## Plan and acceptance criteria

Document the parent-image and MCR versions. Revisit when the complete standalone BrainSuite pipeline has a Linux ARM runtime or an officially supported equivalent execution mode; validate BIDS processing and dashboard outputs together.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsappbrainsuite/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/101#issuecomment-5651280407).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
