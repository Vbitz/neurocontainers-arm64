# slicersalt: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

SlicerSALT is source available from Kitware and documents Linux CMake builds. The pinned archive is amd64. Its Slicer superbuild and shape-analysis extensions require a consistent native build; this is a large dependency task rather than a binary-only product.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/slicersalt/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `download`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/166). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Upstream source/build guide](https://slicersalt.readthedocs.io/en/latest/build.html).

## Plan and acceptance criteria

Use the 3.0.0 source and matching Slicer dependencies, rebuilding all SALT extensions for the same ABI. Validate representative shape-processing output and GUI operation; do not substitute a plain Slicer container.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/slicersalt/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/166#issuecomment-5651352267).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
