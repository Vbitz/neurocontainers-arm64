# fetalsegmentation: ARM64 research plan

Researched: 2026-09-13. Recipe version: `20241116`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The pinned image packages an automated fetal segmentation stack. SVRTK/auto-proc sources are public, and the general_auto_amd tag documents the distributed packaging choice. It does not prove every component is intrinsically tied to Intel.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fetalsegmentation/build.yaml).
- Base image expression: `fetalsvrtk/segmentation:general_auto_amd@{{ context.base_image_digest }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/198). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `fetalsvrtk/segmentation:general_auto_amd@sha256:d0b3e19f7dd0b3d01fef6a41464487b5c127867646b5238c4eee79b02eecc268`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [SVRTK/SVRTK upstream documentation](https://github.com/SVRTK/SVRTK/blob/master/README.md).
- [SVRTK/SVRTK CMakeLists.txt](https://github.com/SVRTK/SVRTK/blob/master/CMakeLists.txt).
- [SVRTK/auto-proc-svrtk upstream documentation](https://github.com/SVRTK/auto-proc-svrtk/blob/main/README.md).
- [Registry manifest inspected](https://registry-1.docker.io/v2/fetalsvrtk/segmentation/manifests/sha256:d0b3e19f7dd0b3d01fef6a41464487b5c127867646b5238c4eee79b02eecc268).

## Plan and acceptance criteria

Inspect the exact image's source and segmentation-model environment, including MIRTK utilities and inference device selection. Recreate supported components natively and validate the automated segmentation output; identify any mandatory GPU or unavailable dependency precisely.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fetalsegmentation/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
