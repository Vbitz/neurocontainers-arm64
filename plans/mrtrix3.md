# mrtrix3: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.0.8`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

MRtrix documents a portable C++ source build. This recipe adds FSL, ANTs and FreeSurfer, so verifying MRtrix alone would not verify the full container. The missing dependency assembly is the issue; an x86 binary recipe is not an intrinsic MRtrix blocker.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mrtrix3/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `fsl 6.0.7.18`, `mrtrix3 {{ context.version }}`, `ants 2.4.3`, `freesurfer 7.4.1`.
- Declared download inputs: `acpcdetect_V2_1_LinuxCentOS6_7_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/243). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MRtrix3/mrtrix3 upstream documentation](https://github.com/MRtrix3/mrtrix3/blob/master/README.md).
- [MRtrix3/mrtrix3 Dockerfile](https://github.com/MRtrix3/mrtrix3/blob/master/Dockerfile).
- [MRtrix3/mrtrix3 release nightly-dev](https://github.com/MRtrix3/mrtrix3/releases/tag/nightly-dev).

## Plan and acceptance criteria

Build the pinned MRtrix source with Eigen, FFTW, zlib and Qt, then resolve each included imaging tool. Preserve conversion, modeling, tractography and preprocessing tests; reuse verified prerequisite evidence where versions match.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mrtrix3/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/243#issuecomment-5651544475).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
