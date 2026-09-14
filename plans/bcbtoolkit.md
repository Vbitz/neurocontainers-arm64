# bcbtoolkit: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Upstream documents bundled FSL, track_vis and native libraries. The bundled amd64 Java runtime is replaceable; it is not the fundamental obstacle. TrackVis is distributed as a binary product, and the required FSL subset also needs native builds.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bcbtoolkit/build.yaml).
- Base image expression: `ubuntu:18.04`.
- Declared download inputs: `bcbtoolkit_archive`, `run_disco_sh`, `tractotron_cli_sh`, `hcp_atlas_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/120). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [chrisfoulon/BCBToolKit upstream documentation](https://github.com/chrisfoulon/BCBToolKit/blob/master/README.md).
- [data-others/atlas upstream documentation](https://github.com/data-others/atlas/blob/main/README.md).
- [data-others/atlas release hcp1065](https://github.com/data-others/atlas/releases/tag/hcp1065).

## Plan and acceptance criteria

Separate the Java GUI from bundled executables without dropping features. Obtain an authorized ARM build/source route for required TrackVis tools and build the FSL subset. Exercise disconnectome and tractotron output, plus the GUI and tract visualization paths.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bcbtoolkit/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/120#issuecomment-5651343130).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
