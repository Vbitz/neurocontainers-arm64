# ilastik: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.4.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Ilastik documents source and experimental Conda installation. Its binary distribution bundles a specialized native stack, including image-processing libraries and GUI dependencies. Lack of an ARM installer does not establish a fundamental source limitation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/ilastik/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `ilastik_1_4_0_Linux_tar_bz2`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/147). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [ilastik/ilastik upstream documentation](https://github.com/ilastik/ilastik/blob/main/Readme.md).
- [ilastik/ilastik pyproject.toml](https://github.com/ilastik/ilastik/blob/main/pyproject.toml).
- [ilastik/ilastik release 1.5.0a1](https://github.com/ilastik/ilastik/releases/tag/1.5.0a1).

## Plan and acceptance criteria

Inspect the release-1.4 environment and channels for each compiled dependency, especially VIGRA/lazyflow dependencies and Qt. Rebuild only through supported configurations. Test pixel classification and exported probability maps with a small saved project.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/ilastik/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
