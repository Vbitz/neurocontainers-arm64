# bidsapppymvpa: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.2`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The BIDS application and Dockerfile are public. Its old image and legacy Python/PyMVPA scientific environment require reconstruction; an amd64-only manifest alone is not a fundamental blocker. Native compiled Python dependencies and external FSL tools need explicit resolution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsapppymvpa/build.yaml).
- Base image expression: `bids/pymvpa:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/103). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/pymvpa:v2.0.2`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/PyMVPA upstream documentation](https://github.com/bids-apps/PyMVPA/blob/master/README.md).
- [bids-apps/PyMVPA Dockerfile](https://github.com/bids-apps/PyMVPA/blob/master/Dockerfile).
- [bids-apps/PyMVPA release v4.0.3](https://github.com/bids-apps/PyMVPA/releases/tag/v4.0.3).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/pymvpa/manifests/v2.0.2).

## Plan and acceptance criteria

Inspect the v2.0.2 Dockerfile and Python lock rather than adopting current v4 defaults. Build its scientific dependencies natively or document the first unsupported exact version. Validate a small decoding/permutation analysis with expected results.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsapppymvpa/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/103#issuecomment-5651280810).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
