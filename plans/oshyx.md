# oshyx: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.4`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

OSHy-X publishes the Python segmentation source and atlas workflow but documents execution inside its container. The inherited image contains ANTs, Python and Julia. The missing ARM image is a distribution barrier; the matching source/runtime composition needs reconstruction.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/oshyx/build.yaml).
- Base image expression: `jerync/oshyx_0.4:{{ context.base_image_tag }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/224). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `jerync/oshyx_0.4:20220614`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Cadaei-Yuvxvs/OSHy-X upstream documentation](https://github.com/Cadaei-Yuvxvs/OSHy-X/blob/main/README.md).
- [Cadaei-Yuvxvs/OSHy-X release 0.4](https://github.com/Cadaei-Yuvxvs/OSHy-X/releases/tag/0.4).
- [Registry manifest inspected](https://registry-1.docker.io/v2/jerync/oshyx_0.4/manifests/20220614).

## Plan and acceptance criteria

Recover the 0.4 container build instructions and native ANTs/Julia dependencies, preserving atlas files and settings. Validate hypothalamus/fornix labels, volumes and registration output; document any unavailable exact prerequisite rather than assuming Python is architecture-specific.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/oshyx/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
