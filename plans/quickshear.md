# quickshear: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.2.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Quickshear itself is a source-available Python defacer. This container adds SynthStrip and OpenRecon integration by inheriting an amd64 image. A native CPU build of those exact auxiliary components is needed; the image architecture does not prove Quickshear is unportable.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/quickshear/build.yaml).
- Base image expression: `freesurfer/synthstrip:1.6`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/228). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `freesurfer/synthstrip:1.6`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [nipy/quickshear upstream documentation](https://github.com/nipy/quickshear/blob/master/README.rst).
- [nipy/quickshear pyproject.toml](https://github.com/nipy/quickshear/blob/master/pyproject.toml).
- [nipy/quickshear release v1.1.0](https://github.com/nipy/quickshear/releases/tag/v1.1.0).
- [ismrmrd/ismrmrd upstream documentation](https://github.com/ismrmrd/ismrmrd/blob/master/README.md).
- [ismrmrd/ismrmrd CMakeLists.txt](https://github.com/ismrmrd/ismrmrd/blob/master/CMakeLists.txt).
- [ismrmrd/ismrmrd Dockerfile](https://github.com/ismrmrd/ismrmrd/blob/master/Dockerfile).
- [ismrmrd/ismrmrd environment.yml](https://github.com/ismrmrd/ismrmrd/blob/master/environment.yml).
- [ismrmrd/ismrmrd release v1.15.0](https://github.com/ismrmrd/ismrmrd/releases/tag/v1.15.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/freesurfer/synthstrip/manifests/1.6).

## Plan and acceptance criteria

Recreate the same SynthStrip runtime on an ARM base, install the pinned Quickshear and preserve MRD conversion dependencies. Test skull stripping followed by defacing and MRD round-trip output, including preserved brain voxels.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/quickshear/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **✅**, fulltest **❌**; plan assessment: **Plausible**.
- Investigation outcome: **failed-runtime**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/228#issuecomment-5654227161).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
