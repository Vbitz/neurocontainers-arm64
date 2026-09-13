# prequal: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

PreQual publishes its pipeline/container sources, but the recipe assembles legacy Python environments, C3D/FSL/ANTs/FreeSurfer and MCR paths. Some eddy options explicitly require GPU, while ordinary CPU processing exists. The exact required native/runtime stages determine the blocker.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/prequal/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `mrtrix3 3.0.3`, `fsl 6.0.4`, `convert3d 1.0.0`, `ants 2.4.3`, `miniconda py38_23.11.0-2`, `miniconda py38_23.11.0-2`.
- Declared download inputs: `prequal_source`, `freesurfer_tar`, `matlab_runtime_installer`, `scilpy_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/227). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MASILab/PreQual upstream documentation](https://github.com/MASILab/PreQual/blob/master/README.md).
- [MASILab/PreQual release v1.1.0](https://github.com/MASILab/PreQual/releases/tag/v1.1.0).
- [scilus/scilpy upstream documentation](https://github.com/scilus/scilpy/blob/master/README.md).
- [scilus/scilpy pyproject.toml](https://github.com/scilus/scilpy/blob/master/pyproject.toml).
- [scilus/scilpy setup.py](https://github.com/scilus/scilpy/blob/master/setup.py).
- [scilus/scilpy release 2.3.0](https://github.com/scilus/scilpy/releases/tag/2.3.0).

## Plan and acceptance criteria

Map every tested mode to its dependencies, including Synb0 and MATLAB executables. Resolve CPU-native tools without deleting GPU or MCR-dependent advertised functionality. Validate diffusion QC, corrected images and reports; preserve resource requirements for Synb0.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/prequal/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
