# vmtk: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.5.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The inspected Conda package metadata has no linux-aarch64 files, but VMTK has public CMake source and documented ITK/VTK superbuild options. Thus the installer/package channel is blocked, while ordinary native source compilation remains a possible route.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/vmtk/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `miniforge_installer`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/240). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [vmtk/vmtk upstream documentation](https://github.com/vmtk/vmtk/blob/master/README.md).
- [vmtk/vmtk CMakeLists.txt](https://github.com/vmtk/vmtk/blob/master/CMakeLists.txt).
- [vmtk/vmtk pyproject.toml](https://github.com/vmtk/vmtk/blob/master/pyproject.toml).
- [vmtk/vmtk setup.py](https://github.com/vmtk/vmtk/blob/master/setup.py).
- [vmtk/vmtk release v1.5.0](https://github.com/vmtk/vmtk/releases/tag/v1.5.0).
- [conda-forge/miniforge upstream documentation](https://github.com/conda-forge/miniforge/blob/main/README.md).
- [conda-forge/miniforge release 26.7.2-0](https://github.com/conda-forge/miniforge/releases/tag/26.7.2-0).
- [Conda-forge VMTK package inventory](https://api.anaconda.org/package/conda-forge/vmtk).

## Plan and acceptance criteria

Build v1.5.0 against supported native ITK/VTK/Python versions, preserving wrapped C++ classes and GUI tools. Evaluate current wheel-building work only with version compatibility established. Test surface extraction and centerline generation, not just imports.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/vmtk/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
