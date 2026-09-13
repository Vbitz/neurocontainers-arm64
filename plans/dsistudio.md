# dsistudio: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2024.06.12.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The pinned 2024 CPU archive is not an ARM selector, but the current upstream 2026.7.25 release explicitly includes dsi_studio_linux_universal_cpu_arm64.zip. Source is also public. A blanket unavailable-ARM-assets blocker is obsolete; the version difference must be addressed.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/dsistudio/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `dsi_studio_ubuntu2204_cpu_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/195). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `2026.7.25` lists: `dsi_studio_linux_universal_cpu.zip`, `dsi_studio_linux_universal_cpu_arm64.zip`, `dsi_studio_linux_universal_cuda.zip`, `dsi_studio_linux_universal_cuda_arm64.zip`, `dsi_studio_linux_universal_legacy_cpu.zip`, `dsi_studio_macos-14-arm64_qt6.zip`, `dsi_studio_ubuntu2204_arm64.zip`. This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [frankyeh/DSI-Studio upstream documentation](https://github.com/frankyeh/DSI-Studio/blob/master/README.md).
- [frankyeh/DSI-Studio release 2026.7.25](https://github.com/frankyeh/DSI-Studio/releases/tag/2026.7.25).

## Plan and acceptance criteria

Inspect the pinned source's CPU build path to preserve 2024 behavior, or plan a version-aligned update using the published 2026 ARM asset and corresponding x86 release. Validate reconstruction and tractography outputs; do not infer runtime success from the asset name.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/dsistudio/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
