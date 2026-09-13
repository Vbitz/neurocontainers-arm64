# connectomeworkbench: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.1.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Workbench itself documents a CMake/Qt source build. The recipe additionally installs FreeSurfer 7.1.1 and selects a particular NeuroDebian package revision. The full container's dependency/package availability is unresolved; Workbench is not binary-only.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/connectomeworkbench/build.yaml).
- Base image expression: `neurodebian:bookworm-non-free`.
- Builder templates: `freesurfer 7.1.1`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/132). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Washington-University/workbench upstream documentation](https://github.com/Washington-University/workbench/blob/master/README).
- [Washington-University/workbench release v2.2.1](https://github.com/Washington-University/workbench/releases/tag/v2.2.1).

## Plan and acceptance criteria

Check the exact apt version on ARM and, if absent, build the corresponding Workbench source with Qt and OSMesa. Establish native FreeSurfer for the included functionality. Test CIFTI/GIFTI operations and scene rendering with the existing suite.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/connectomeworkbench/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
