# deepsif: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.1.post1`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

The container installs x86 CUDA/cuDNN and a broad modeling environment. DeepSIF publishes Python source, but documentation of a complete CPU execution path for all advertised components is insufficient here. GPU requirements and any MATLAB-dependent data generation must be considered separately.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/deepsif/build.yaml).
- Base image expression: `debian:11`.
- Builder templates: `miniconda latest`.
- Declared download inputs: `debian_ca_certificates`, `main_tar_gz`, `cuda_keyring_1_0_1_all_deb`, `cudnn_11_5_linux_x64_v8_3_0_98_tgz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/135). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bfinl/DeepSIF upstream documentation](https://github.com/bfinl/DeepSIF/blob/main/README.md).
- [bfinl/DeepSIF requirements.txt](https://github.com/bfinl/DeepSIF/blob/main/requirements.txt).

## Plan and acceptance criteria

Trace pinned training, evaluation and forward-model commands for mandatory CUDA/MATLAB use. Select only an upstream-supported CPU configuration that preserves scope, or document required ARM GPU/runtime infrastructure. Validate source localization outputs, not only imports.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/deepsif/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Conditional**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/135#issuecomment-5651346147).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
