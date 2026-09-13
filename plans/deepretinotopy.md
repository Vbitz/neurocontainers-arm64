# deepretinotopy: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.19`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Upstream explicitly describes CPU inference as well as GPU use. The recipe's FreeSurfer base and compiled PyTorch Geometric wheels are the obstacles. CUDA packaging does not prove that the scientific model is GPU-only.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/deepretinotopy/build.yaml).
- Base image expression: `ghcr.io/neurodesk/freesurfer_7.3.2:20230216`.
- Builder templates: `miniconda latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/193). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `ghcr.io/neurodesk/freesurfer_7.3.2:20230216`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [felenitaribeiro/deepRetinotopy_TheToolbox upstream documentation](https://github.com/felenitaribeiro/deepRetinotopy_TheToolbox/blob/main/README.md).
- [felenitaribeiro/deepRetinotopy_TheToolbox environment.yml](https://github.com/felenitaribeiro/deepRetinotopy_TheToolbox/blob/main/environment.yml).
- [felenitaribeiro/deepRetinotopy_TheToolbox release v1.0.19](https://github.com/felenitaribeiro/deepRetinotopy_TheToolbox/releases/tag/v1.0.19).
- [Registry manifest inspected](https://ghcr.io/v2/neurodesk/freesurfer_7.3.2/manifests/20230216).

## Plan and acceptance criteria

Build the pinned CPU-capable inference stack, retaining FreeSurfer and Workbench preprocessing and matching PyG extension versions. Validate native-surface predictions and resampling; record any exact unsupported extension instead of rejecting all CPU execution.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/deepretinotopy/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
