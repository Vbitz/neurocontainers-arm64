# ashs: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

ASHS source exists, including a CMake build. The distributed fastashs archive bundles ANTs, label fusion, BET, C3D and Qhull executables; previous payload inspection found Intel binaries. The old blanket binary-only assessment omitted the source route.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/ashs/build.yaml).
- Base image expression: `ubuntu:16.04`.
- Declared download inputs: `archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/183). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pyushkevich/ashs upstream documentation](https://github.com/pyushkevich/ashs/blob/master/README.md).
- [pyushkevich/ashs CMakeLists.txt](https://github.com/pyushkevich/ashs/blob/master/CMakeLists.txt).

## Plan and acceptance criteria

Map each bundled executable to its source/version, build the available projects with native libraries, and preserve the atlas data. Validate hippocampal subfield labels on a small atlas/subject fixture; unavailable source for any essential bundled tool would be a specific blocker.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/ashs/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
