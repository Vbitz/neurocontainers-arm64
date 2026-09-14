# deepisles: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

Upstream installation documents NVIDIA GPU use and pins a legacy PyTorch/CUDA and SimpleITK-SimpleElastix environment. PyTorch 1.11 itself has ARM CPU wheels, so the old claim that the entire version is unavailable on ARM is incorrect. GPU execution and the exact auxiliary stack remain blockers.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/deepisles/build.yaml).
- Base image expression: `ubuntu:24.04`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/134). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `torch-1.11.0`: 4 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [ezequieldlrosa/DeepIsles upstream documentation](https://github.com/ezequieldlrosa/DeepIsles/blob/main/README.md).
- [ezequieldlrosa/DeepIsles Dockerfile](https://github.com/ezequieldlrosa/DeepIsles/blob/main/Dockerfile).
- [ezequieldlrosa/DeepIsles requirements.txt](https://github.com/ezequieldlrosa/DeepIsles/blob/main/requirements.txt).
- [ezequieldlrosa/DeepIsles release v1.1](https://github.com/ezequieldlrosa/DeepIsles/releases/tag/v1.1).
- [torch-1.11.0 published package metadata](https://pypi.org/pypi/torch/1.11.0/json).

## Plan and acceptance criteria

Determine whether the pinned release has an officially supported CPU inference mode. If not, full testing needs native ARM GPU infrastructure and matching CUDA dependencies. If it does, resolve that CPU environment and validate lesion masks with unchanged weights.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/deepisles/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Conditional**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/134#issuecomment-5651345951).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
