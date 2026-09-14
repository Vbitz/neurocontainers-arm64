# connectomemapper3: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.2.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The pipeline source and GUI are public, but the container includes MATLAB Runtime, FreeSurfer and FSL. Its glnxa64 runtime cannot be supplied merely by replacing the Python environment or Qt wheels.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/connectomemapper3/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `freesurfer 7.1.1`, `matlabmcr 2014b`, `fsl 5.0.10`, `afni latest`, `ants 2.4.3`, `miniconda py39_23.11.0-2`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/191). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [connectomicslab/connectomemapper3 upstream documentation](https://github.com/connectomicslab/connectomemapper3/blob/master/README.md).
- [connectomicslab/connectomemapper3 Dockerfile](https://github.com/connectomicslab/connectomemapper3/blob/master/Dockerfile).
- [connectomicslab/connectomemapper3 setup.py](https://github.com/connectomicslab/connectomemapper3/blob/master/setup.py).
- [connectomicslab/connectomemapper3 release v3.2.0](https://github.com/connectomicslab/connectomemapper3/releases/tag/v3.2.0).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Identify the stages invoking compiled MATLAB and retain that blocker for full functionality. Resolve the native imaging dependencies separately; eventual validation must cover anatomical, diffusion and functional connectivity outputs rather than just the wrapper GUI.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/connectomemapper3/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/191#issuecomment-5651529761).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
