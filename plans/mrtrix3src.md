# mrtrix3src: ARM64 research plan

Researched: 2026-09-13. Recipe version: `latest`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The recipe already builds MRtrix source at a commit but starts from an old FSL image and adds ANTs. Its architecture restriction comes from the inherited/native dependency stack, not absence of MRtrix source.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mrtrix3src/build.yaml).
- Base image expression: `vnmd/fsl_6.0.5.1:20221016`.
- Builder templates: `ants 2.3.4`.
- Declared download inputs: `mrtrix3_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/216). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `vnmd/fsl_6.0.5.1:20221016`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MRtrix3/mrtrix3 upstream documentation](https://github.com/MRtrix3/mrtrix3/blob/master/README.md).
- [MRtrix3/mrtrix3 Dockerfile](https://github.com/MRtrix3/mrtrix3/blob/master/Dockerfile).
- [MRtrix3/mrtrix3 release nightly-dev](https://github.com/MRtrix3/mrtrix3/releases/tag/nightly-dev).
- [Registry manifest inspected](https://registry-1.docker.io/v2/vnmd/fsl_6.0.5.1/manifests/20221016).

## Plan and acceptance criteria

Replace the inherited image with a matching native FSL environment and retain the exact MRtrix source commit and ANTs functionality. Validate image conversion and tractography plus scripts invoking external tools.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mrtrix3src/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/216#issuecomment-5651534926).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Implementation disposition — 2026-09-14

Preflight stopped before a candidate because the recipe inherits an x86 FSL base and downloads `acpcdetect_V2.1_LinuxCentOS6.7`, an embedded native prerequisite with no ARM64 payload. Building MRtrix3 itself from source would not satisfy the container's required external tool. This is recorded as `blocked-prerequisite` in [issue #216](https://github.com/Vbitz/neurocontainers-arm64/issues/216#issuecomment-5651534926). Revisit when ARM64 FSL/base and acpcdetect releases exist, or the upstream recipe removes that required x86-only prerequisite.
