# mrsiproc: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.2.0.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

Upstream explicitly describes compiled MATLAB reconstruction scripts; the recipe bundles R2021b glnxa64 runtime along with FSL, FreeSurfer, MINC and Julia. Replacing the Julia or Python installer does not remove the compiled MATLAB dependency.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mrsiproc/build.yaml).
- Base image expression: `vnmd/fsl_6.0.7.1`.
- Builder templates: `dcm2niix {{ context.dcm2niix_version }}`, `minc {{ context.minc_version }}`, `miniconda latest`.
- Declared download inputs: `libjpeg62_turbo_deb`, `hdbet_0_model`, `hdbet_1_model`, `hdbet_2_model`, `hdbet_3_model`, `hdbet_4_model`, `lcm_64_tar`, `lcmodel_3t_zip`, `lcmodel_1_5t_zip`, `lcmodel_7t_zip`, `lcmodel_9_4t_zip`, `basisset_lcmodel_zip` (additional model/data inputs are in the recipe).
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/157). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `vnmd/fsl_6.0.7.1`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [korbinian90/mrsi_pipeline_neurodesk upstream documentation](https://github.com/korbinian90/mrsi_pipeline_neurodesk/blob/main/README.md).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/vnmd/fsl_6.0.7.1/manifests/latest).

## Plan and acceptance criteria

Record the reconstruction/MCR pairing and retain the full-container blocker until a native supported runtime exists. Independently buildable utilities should not be mistaken for a complete MRSI reconstruction port; validate spectra and maps when the prerequisite changes.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mrsiproc/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/157#issuecomment-5651350529).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
