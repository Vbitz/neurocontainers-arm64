# brainvisa: ARM64 research plan

Researched: 2026-09-13. Recipe version: `6.0.38`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The recipe resolves BrainVISA from a linux-64 channel. BrainVISA has public source and a dedicated CMake build system; the channel selection is a packaging gap. AIMS/Anatomist/Soma and their Qt/Python/native dependencies must be built as a consistent stack.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/brainvisa/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda py312_25.5.1-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/187). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [brainvisa/brainvisa-cmake upstream documentation](https://github.com/brainvisa/brainvisa-cmake/blob/master/README.md).
- [brainvisa/brainvisa-cmake CMakeLists.txt](https://github.com/brainvisa/brainvisa-cmake/blob/master/CMakeLists.txt).
- [ARM channel probe (404 on research date)](https://brainvisa.info/neuro-forge/linux-aarch64/repodata.json).

## Plan and acceptance criteria

Check the actual ARM channel contents for the pinned package set, then evaluate BrainVISA's documented source build. Preserve AIMS image/mesh operations and Anatomist rendering. Record an exact missing package or compiler error before calling it an upstream architecture blocker.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/brainvisa/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
