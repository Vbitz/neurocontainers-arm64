# mgltools: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.5.7.post2`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The official 1.5.7 downloads are Intel Linux distributions. Upstream describes reusable Python/C++ components, so it would be inaccurate to call all MGLTools source unavailable. The legacy Python 2/native extension stack and separately distributed MSMS payload need complete source/build coverage.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mgltools/build.yaml).
- Base image expression: `centos:7`.
- Declared download inputs: `491`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/153). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Official downloads](https://ccsb.scripps.edu/mgltools/downloads/).
- [Upstream component description](https://ccsb.scripps.edu/mgltools/).

## Plan and acceptance criteria

Inventory binary extensions and MSMS in the exact archive, identify corresponding released sources and permissions, then assess a native legacy build. Revisit if all essential components have a supported route; test molecular loading, preparation and surface functions together.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mgltools/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/153#issuecomment-5651349717).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
