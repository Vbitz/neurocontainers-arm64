# rstudio: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2023.12.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

RStudio is open source and includes build instructions. The recipe downloads old amd64 desktop and server packages. Both binaries and their bundled Electron/C++ dependencies need ARM builds; R itself and changing the .deb filename are insufficient.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/rstudio/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `rstudio_2023_12_1_402_amd64_deb`, `rstudio_server_2023_12_1_402_amd64_deb`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/230). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [rstudio/rstudio upstream documentation](https://github.com/rstudio/rstudio/blob/main/README.md).
- [rstudio/rstudio CMakeLists.txt](https://github.com/rstudio/rstudio/blob/main/CMakeLists.txt).
- [rstudio/rstudio package.json](https://github.com/rstudio/rstudio/blob/main/package.json).

## Plan and acceptance criteria

Inspect release-matched INSTALL and dependency scripts for both desktop and server targets. Use published ARM assets where available only with a deliberate version update; otherwise build the same source. Validate R session execution through both interfaces.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/rstudio/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/230#issuecomment-5651537447).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Current vendor download audit — 2026-09-15

Posit's current documentation lists ARM64 support for newer RStudio Server/Workbench deployments on Ubuntu 24/26 and RHEL 10, but current RStudio Desktop Linux downloads remain `amd64`. This recipe requires both the pinned 2023.12.1 Desktop and Server debs, so newer server support does not provide a complete ARM64 route. The blocker and revisit condition are recorded in [issue #230](https://github.com/Vbitz/neurocontainers-arm64/issues/230#issuecomment-5665695051); do not attempt a partial server-only container.
