# fsl: ARM64 research plan

Researched: 2026-09-13. Recipe version: `6.0.7.22.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The earlier blanket no-ARM-stack claim is contradicted by the official channel: linux-aarch64 repodata contains 94 distinct package names, including BET, FLIRT and FNIRT. Developer documentation also lists ARM build targets. This does not establish the exact 6.0.7.22 environment or optional CUDA tools.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fsl/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `fsl {{ context.fsl_version }}`.
- Declared download inputs: `v0_4_3_beta_tar_gz`, `UnixIntro_tar_gz`, `preCourse_tar_gz`, `registration_tar_gz`, `structural_tar_gz`, `fmri1_tar_gz`, `fmri2_tar_gz`, `fmri3_tar_gz`, `fmri_extras_tar_gz`, `rest_tar_gz`, `fdt_tar_gz`, `mrs_tar_gz` (additional model/data inputs are in the recipe).
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/242). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [ReproNim/neurodocker upstream documentation](https://github.com/ReproNim/neurodocker/blob/master/README.md).
- [ReproNim/neurodocker Dockerfile](https://github.com/ReproNim/neurodocker/blob/master/Dockerfile).
- [ReproNim/neurodocker pyproject.toml](https://github.com/ReproNim/neurodocker/blob/master/pyproject.toml).
- [ReproNim/neurodocker release 2.1.2](https://github.com/ReproNim/neurodocker/releases/tag/2.1.2).
- [physimals/oxasl_mp upstream documentation](https://github.com/physimals/oxasl_mp/blob/master/README.md).
- [physimals/oxasl_mp requirements.txt](https://github.com/physimals/oxasl_mp/blob/master/requirements.txt).
- [physimals/oxasl_mp setup.py](https://github.com/physimals/oxasl_mp/blob/master/setup.py).
- [Official ARM package index](https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/public/linux-aarch64/repodata.json).
- [FSL architecture/build documentation](https://fsl.fmrib.ox.ac.uk/fsl/docs/development/management/build_system.html).

## Plan and acceptance criteria

Resolve the pinned FSL environment against official ARM packages and audit extra oxasl/ICA-AROMA/GUI tools. Replace installer architecture assumptions and separate GPU execution prerequisites. Test core registration, segmentation and ASL functions without changing the scientific dependency versions speculatively.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fsl/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `9a5ae40c67667a088f50f0e9885833b983893f98` passed native ARM64 Docker build, architecture verification, SIF conversion, deploy checks, and all **129/129** fulltests in [run 34762946871](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34762946871). The ARM route uses the official FSL ARM package set and correct installed prefix while preserving x86_64 packaging.
