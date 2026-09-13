# braid: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

BRAID documents installation from Python source and lists external preprocessing tools. Its FSL, MRtrix, C3D and ANTs versions need native builds. There is no demonstrated ARM-specific failure in the BRAID model itself.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/braid/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `fsl 6.0.4`, `mrtrix3 3.0.3`, `convert3d 1.0.0`, `ants 2.3.4`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/185). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MASILab/BRAID upstream documentation](https://github.com/MASILab/BRAID/blob/main/README.md).
- [MASILab/BRAID pyproject.toml](https://github.com/MASILab/BRAID/blob/main/pyproject.toml).

## Plan and acceptance criteria

Resolve and test those four dependencies first, retaining the model weights and preprocessing parameters. Run the complete diffusion preprocessing and age-prediction path, comparing numerical outputs rather than just importing torch.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/braid/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
