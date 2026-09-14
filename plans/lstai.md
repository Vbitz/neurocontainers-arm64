# lstai: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The prior TensorFlow-2.13.1-unavailable claim is false: PyPI lists Linux ARM wheels. LST-AI 1.1.0 source is public and the recipe already uses CPU torch. Its dcm2niix asset, HD-BET and exact environment still require ARM resolution. Current 2.0 release-candidate changes are not evidence for 1.1.0.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/lstai/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `lst_data_zip`, `dcm2niix_lnx_zip`, `0_model`, `1_model`, `2_model`, `3_model`, `4_model`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/207). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-2.13.1`: 4 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [CompImg/LST-AI upstream documentation](https://github.com/CompImg/LST-AI/blob/main/README.md).
- [CompImg/LST-AI setup.py](https://github.com/CompImg/LST-AI/blob/main/setup.py).
- [CompImg/LST-AI release v2.0.0rc1](https://github.com/CompImg/LST-AI/releases/tag/v2.0.0rc1).
- [rordenlab/dcm2niix upstream documentation](https://github.com/rordenlab/dcm2niix/blob/master/README.md).
- [rordenlab/dcm2niix CMakeLists.txt](https://github.com/rordenlab/dcm2niix/blob/master/CMakeLists.txt).
- [rordenlab/dcm2niix Dockerfile](https://github.com/rordenlab/dcm2niix/blob/master/Dockerfile).
- [rordenlab/dcm2niix pyproject.toml](https://github.com/rordenlab/dcm2niix/blob/master/pyproject.toml).
- [rordenlab/dcm2niix release v1.0.20260724](https://github.com/rordenlab/dcm2niix/releases/tag/v1.0.20260724).
- [tensorflow-2.13.1 published package metadata](https://pypi.org/pypi/tensorflow/2.13.1/json).

## Plan and acceptance criteria

Resolve the exact 1.1.0 CPU environment with ARM TensorFlow and torch, build native dcm2niix, and preserve HD-BET/model weights. Validate lesion masks and model outputs without adopting the newer inference implementation just to obtain a pass.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/lstai/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/207#issuecomment-5654126784).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
