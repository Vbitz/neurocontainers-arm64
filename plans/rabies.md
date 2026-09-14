# rabies: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5.3.post1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

RABIES publishes source and its Dockerfile, which explicitly installs an x86 MINC toolkit. ARM micromamba is available; the actual native work is MINC/ANTs/AFNI and the matched scientific Python environment, not changing the installer alone.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/rabies/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `melodic_IC.nii.gz`, `vascular_mask.nii.gz`, `EPI_template.nii.gz`, `EPI_brain_mask.nii.gz`, `EPI_WM_mask.nii.gz`, `EPI_CSF_mask.nii.gz`, `EPI_vascular_mask.nii.gz`, `EPI_labels.nii.gz`, `melodic_IC_resampled.nii.gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/162). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [CoBrALab/RABIES upstream documentation](https://github.com/CoBrALab/RABIES/blob/master/README.md).
- [CoBrALab/RABIES Dockerfile](https://github.com/CoBrALab/RABIES/blob/master/Dockerfile).
- [CoBrALab/RABIES setup.py](https://github.com/CoBrALab/RABIES/blob/master/setup.py).
- [CoBrALab/RABIES release 0.6.1](https://github.com/CoBrALab/RABIES/releases/tag/0.6.1).
- [ANTsX/ANTs upstream documentation](https://github.com/ANTsX/ANTs/blob/main/README.md).
- [ANTsX/ANTs CMakeLists.txt](https://github.com/ANTsX/ANTs/blob/main/CMakeLists.txt).
- [ANTsX/ANTs Dockerfile](https://github.com/ANTsX/ANTs/blob/main/Dockerfile).
- [ANTsX/ANTs release v2.6.5](https://github.com/ANTsX/ANTs/releases/tag/v2.6.5).

## Plan and acceptance criteria

Build the required toolkit versions through supported sources and retain atlas files. Validate rodent preprocessing, confound correction and connectivity results. Record a concrete dependency error if encountered; don't classify the entire open-source stack as binary-only.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/rabies/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/162#issuecomment-5651351465).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
