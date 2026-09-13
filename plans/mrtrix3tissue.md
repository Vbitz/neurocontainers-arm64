# mrtrix3tissue: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.2.9`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

MRtrix3Tissue publishes the exact 3Tissue_v5.2.9 source. The recipe inherits an old Intel FSL container; that packaging is the immediate obstacle. Replacing MRtrix3Tissue with standard MRtrix would lose the intended three-tissue methods.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mrtrix3tissue/build.yaml).
- Base image expression: `ghcr.io/neurodesk/caid/fsl_6.0.3:20200905`.
- Builder templates: `mrtrix3 3Tissue_v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/217). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `ghcr.io/neurodesk/caid/fsl_6.0.3:20200905`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [3Tissue/MRtrix3Tissue upstream documentation](https://github.com/3Tissue/MRtrix3Tissue/blob/master/README.md).
- [3Tissue/MRtrix3Tissue release 3Tissue_v5.2.9](https://github.com/3Tissue/MRtrix3Tissue/releases/tag/3Tissue_v5.2.9).
- [Registry manifest inspected](https://ghcr.io/v2/neurodesk/caid/fsl_6.0.3/manifests/20200905).

## Plan and acceptance criteria

Build the same fork/release using its documented procedure on a native FSL-capable base. Validate the specialized three-tissue CSD commands and outputs, retaining external preprocessing requirements.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mrtrix3tissue/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
