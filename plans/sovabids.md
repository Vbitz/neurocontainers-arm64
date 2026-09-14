# sovabids: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.3.1a0.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The previous blocker was the VS Code x64 download. VS Code has native ARM packages, and sovabids itself is Python source. The recipe's broader pinned BIDS/MNE environment and GUI dependencies still need an ARM solve; no fundamental blocker is established.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/sovabids/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py310_25.5.1-0`.
- Declared download inputs: `vscode_deb`, `mne_bids_pipeline_main_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/167). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [yjmantilla/sovabids upstream documentation](https://github.com/yjmantilla/sovabids/blob/main/README.rst).
- [yjmantilla/sovabids pyproject.toml](https://github.com/yjmantilla/sovabids/blob/main/pyproject.toml).
- [yjmantilla/sovabids release v0.4.7](https://github.com/yjmantilla/sovabids/releases/tag/v0.4.7).
- [yjmantilla/bidscoin upstream documentation](https://github.com/yjmantilla/bidscoin/blob/master/README.rst).
- [yjmantilla/bidscoin pyproject.toml](https://github.com/yjmantilla/bidscoin/blob/master/pyproject.toml).
- [yjmantilla/bidscoin requirements.txt](https://github.com/yjmantilla/bidscoin/blob/master/requirements.txt).
- [yjmantilla/bidscoin setup.py](https://github.com/yjmantilla/bidscoin/blob/master/setup.py).

## Plan and acceptance criteria

Select the architecture-correct editor asset and inspect the existing environment lock for native package pins. Preserve conversion and editor behavior, then test real electrophysiology-to-BIDS output and validation.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/sovabids/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-infrastructure**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/167#issuecomment-5653614496).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
