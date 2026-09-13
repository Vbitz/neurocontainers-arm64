# lashis: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

LASHiS publishes a native-install path. Its ASHS, C3D, ANTs and FSL dependencies, including legacy bundled ASHS executables, are the real porting work. The Python workflow is not established as ARM-incompatible.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/lashis/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `ants 2.6.2`, `fsl 6.0.7.16`, `convert3d 1.0.0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/204). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [thomshaw92/LASHiS upstream documentation](https://github.com/thomshaw92/LASHiS/blob/master/README.md).
- [thomshaw92/LASHiS Dockerfile](https://github.com/thomshaw92/LASHiS/blob/master/Dockerfile).
- [thomshaw92/LASHiS pyproject.toml](https://github.com/thomshaw92/LASHiS/blob/master/pyproject.toml).
- [thomshaw92/LASHiS release v1.2](https://github.com/thomshaw92/LASHiS/releases/tag/v1.2).
- [pyushkevich/ashs upstream documentation](https://github.com/pyushkevich/ashs/blob/master/README.md).
- [pyushkevich/ashs CMakeLists.txt](https://github.com/pyushkevich/ashs/blob/master/CMakeLists.txt).

## Plan and acceptance criteria

Resolve each executable/version through the corresponding source plan, preserving the atlas and longitudinal workflow. Run a small longitudinal subfield segmentation and verify label outputs; do not silently replace ASHS with a different method.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/lashis/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
