# aidamri: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

AIDAmri is Python with source available. The container bundles FSL 5.0.11 and DSI Studio binaries, while NiftyReg already builds from source. Upstream still documents amd64 container assumptions. The complete pinned dependency set, rather than Python, is the obstacle.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/aidamri/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `miniconda 4.7.12.1`.
- Declared download inputs: `aidamri_tar`, `niftyreg_tar`, `fsl_tar`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/119). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Aswendt-Lab/AIDAmri upstream documentation](https://github.com/Aswendt-Lab/AIDAmri/blob/master/README.md).
- [Aswendt-Lab/AIDAmri Dockerfile](https://github.com/Aswendt-Lab/AIDAmri/blob/master/Dockerfile).
- [Aswendt-Lab/AIDAmri requirements.txt](https://github.com/Aswendt-Lab/AIDAmri/blob/master/requirements.txt).
- [Aswendt-Lab/AIDAmri release v3.0](https://github.com/Aswendt-Lab/AIDAmri/releases/tag/v3.0).
- [KCL-BMEIS/niftyreg upstream documentation](https://github.com/KCL-BMEIS/niftyreg/blob/master/README.md).
- [KCL-BMEIS/niftyreg CMakeLists.txt](https://github.com/KCL-BMEIS/niftyreg/blob/master/CMakeLists.txt).
- [KCL-BMEIS/niftyreg release v2.0.0](https://github.com/KCL-BMEIS/niftyreg/releases/tag/v2.0.0).

## Plan and acceptance criteria

Inventory the invoked FSL and DSI commands. Compile the same NiftyReg revision, establish ARM builds of the other dependencies, and compare rodent registration and tractography outputs. A newer DSI release is a possible migration, not evidence for the old bundled executable.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/aidamri/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
