# bidsappmrtrix3connectome: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.6.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The MRtrix connectome pipeline is available as source and can run outside its container. The image assembles MRtrix, FreeSurfer and FSL. Its missing ARM image does not establish an intrinsic MRtrix limitation; preprocessing and parcellation dependencies are the unresolved work.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsappmrtrix3connectome/build.yaml).
- Base image expression: `bids/mrtrix3_connectome:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/102). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/mrtrix3_connectome:0.6.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/MRtrix3_connectome upstream documentation](https://github.com/bids-apps/MRtrix3_connectome/blob/master/README.md).
- [bids-apps/MRtrix3_connectome Dockerfile](https://github.com/bids-apps/MRtrix3_connectome/blob/master/Dockerfile).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/mrtrix3_connectome/manifests/0.6.0).

## Plan and acceptance criteria

Rebuild the pinned pipeline from its Dockerfile using native MRtrix, FSL and FreeSurfer. Preserve CPU processing and all advertised parcellations; compare a small generated connectome and group-analysis outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsappmrtrix3connectome/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/102#issuecomment-5651280602).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
