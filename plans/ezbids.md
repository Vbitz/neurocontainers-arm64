# ezbids: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The application has a public Node-based Dockerfile. Its recipe additionally bundles ROBEX and selected FSL binaries, which need native builds or upstream assets. An x86 ROBEX archive is an obstacle but does not by itself establish that source is unavailable.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/ezbids/build.yaml).
- Base image expression: `neurodebian:nd20.04-non-free`.
- Declared download inputs: `ezbids_source_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/141). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [openneuropet/ezbids_docker upstream documentation](https://github.com/openneuropet/ezbids_docker/blob/master/README.md).
- [openneuropet/ezbids_docker Dockerfile](https://github.com/openneuropet/ezbids_docker/blob/master/Dockerfile).
- [openneuropet/ezbids_docker package.json](https://github.com/openneuropet/ezbids_docker/blob/master/package.json).
- [dlevitas/FSL_binaries upstream documentation](https://github.com/dlevitas/FSL_binaries/blob/main/README.md).

## Plan and acceptance criteria

Map the exact preprocessing/de-identification commands to ROBEX/FSL sources and release versions. Rebuild those tools, preserve the Node service and validate a small DICOM-to-BIDS workflow, including the existing defacing behavior.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/ezbids/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/141#issuecomment-5651347320).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
