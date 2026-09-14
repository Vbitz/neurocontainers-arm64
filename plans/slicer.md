# slicer: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.10.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Slicer source and a documented superbuild exist. Its Linux amd64 package and bundled MONAILabel extension cannot be reused on ARM. Upstream warns that extensions must match a developer build's ABI; building Slicer alone does not preserve the full container.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/slicer/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py310_25.5.1-0`.
- Declared download inputs: `download`, `download_1`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/231). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Slicer/Slicer upstream documentation](https://github.com/Slicer/Slicer/blob/main/README.md).
- [Slicer/Slicer CMakeLists.txt](https://github.com/Slicer/Slicer/blob/main/CMakeLists.txt).
- [Slicer/Slicer release docs-resources](https://github.com/Slicer/Slicer/releases/tag/docs-resources).
- [Upstream superbuild and extension ABI guidance](https://github.com/Slicer/Slicer/blob/main/Docs/developer_guide/build_instructions/overview.md).

## Plan and acceptance criteria

Build the exact Slicer revision and all included extensions together using release-matched Qt/VTK/ITK/Python dependencies. Verify MONAILabel device requirements, image I/O, rendering and a real extension operation. Record an actual dependency failure rather than assuming a superbuild is a forbidden library port.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/slicer/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/231#issuecomment-5651537651).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
