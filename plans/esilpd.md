# esilpd: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.1.post1`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

VS Code has ARM distributions, so its x64 URL is fixable. This larger environment also selects a Debian x86 CUDA repository and compiled scientific dependencies. The exact scope of mandatory GPU use remains to be established from the workflow and tests.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/esilpd/build.yaml).
- Base image expression: `debian:11`.
- Builder templates: `miniconda py39_23.11.0-2`.
- Declared download inputs: `debian_ca_certificates`, `main_tar_gz`, `cuda_keyring_1_0_1_all_deb`, `cudnn_11_5_linux_x64_v8_3_0_98_tgz`, `download`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/140). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [mne-tools/mne-python upstream documentation](https://github.com/mne-tools/mne-python/blob/main/README.rst).
- [mne-tools/mne-python environment.yml](https://github.com/mne-tools/mne-python/blob/main/environment.yml).
- [mne-tools/mne-python pyproject.toml](https://github.com/mne-tools/mne-python/blob/main/pyproject.toml).
- [mne-tools/mne-python release v1.13.2](https://github.com/mne-tools/mne-python/releases/tag/v1.13.2).
- [mne-tools/mne-bids-pipeline upstream documentation](https://github.com/mne-tools/mne-bids-pipeline/blob/main/README.md).
- [mne-tools/mne-bids-pipeline pyproject.toml](https://github.com/mne-tools/mne-bids-pipeline/blob/main/pyproject.toml).
- [mne-tools/mne-bids-pipeline release v1.10.1](https://github.com/mne-tools/mne-bids-pipeline/releases/tag/v1.10.1).

## Plan and acceptance criteria

Audit the ESILPD entry points and pinned environment for CPU support, using an ARM editor asset and correct native packages. Keep GPU-dependent capabilities explicitly unverified without an ARM GPU runner; validate an actual electrophysiology analysis in the supported mode.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/esilpd/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Conditional**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/140#issuecomment-5651347148).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
