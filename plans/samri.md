# samri: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

SAMRI provides source installation and documentation, but the recipe inherits old FSL and bundles Intel ANTs/Bru2Nii plus a legacy Python environment. Those are separable dependency tasks rather than an intrinsic Python architecture barrier.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/samri/build.yaml).
- Base image expression: `vnmd/fsl_6.0.3:20200905`.
- Declared download inputs: `miniconda_installer`, `samri_source`, `bru2_linux_zip`, `ants_archive`, `mouse_brain_atlases_generator_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/165). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `vnmd/fsl_6.0.3:20200905`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [IBT-FMI/SAMRI upstream documentation](https://github.com/IBT-FMI/SAMRI/blob/master/README.md).
- [IBT-FMI/SAMRI release 0.5.4](https://github.com/IBT-FMI/SAMRI/releases/tag/0.5.4).
- [neurolabusc/Bru2Nii upstream documentation](https://github.com/neurolabusc/Bru2Nii/blob/master/README.md).
- [neurolabusc/Bru2Nii release v1.0.20180303](https://github.com/neurolabusc/Bru2Nii/releases/tag/v1.0.20180303).
- [Registry manifest inspected](https://registry-1.docker.io/v2/vnmd/fsl_6.0.3/manifests/20200905).

## Plan and acceptance criteria

Build the same native tools from supported source, resolve the pinned Python 3.7-era package set, and retain mouse atlas data. Validate Bruker conversion, registration and analysis outputs with the existing fixtures.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/samri/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/165#issuecomment-5651352056).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
