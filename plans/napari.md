# napari: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.8.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Napari itself is Python source with supported Qt installation choices. This recipe additionally advertises local VoxTell/nnInteractive inference backed by CUDA PyTorch. An ARM viewer alone would not preserve the promised backend capabilities; those exact plugin/device requirements need resolution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/napari/build.yaml).
- Base image expression: `ubuntu:24.04`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/219). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [napari/napari upstream documentation](https://github.com/napari/napari/blob/main/README.md).
- [napari/napari pyproject.toml](https://github.com/napari/napari/blob/main/pyproject.toml).
- [napari/napari release v0.9.1](https://github.com/napari/napari/releases/tag/v0.9.1).
- [MIC-DKFZ/napari-voxtell upstream documentation](https://github.com/MIC-DKFZ/napari-voxtell/blob/main/README.md).
- [MIC-DKFZ/napari-voxtell pyproject.toml](https://github.com/MIC-DKFZ/napari-voxtell/blob/main/pyproject.toml).

## Plan and acceptance criteria

Audit pinned plugin CPU support and dependencies, choose a native Qt backend and matching torch packages, and test image layers plus actual plugin inference. If an essential backend requires GPU, record the runner prerequisite rather than classifying all Napari as unsupported.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/napari/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-14

The official PyTorch CPU index now lists matching Linux `aarch64` wheels for the pinned torch 2.8.0 and torchvision 0.23.0 versions. Candidate [`8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc`](https://github.com/Vbitz/neurocontainers/commit/8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc) is pushed on [`arm64/napari-cpu-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/napari-cpu-arm), based on accepted submodule pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`.

The candidate declares `aarch64`, preserves the x86_64 CUDA `cu126` path, and selects the official CPU wheel index only on ARM64. Napari, VoxTell and nnInteractive package installation plus the existing plugin discovery fulltest remain unchanged. Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. Native verification is queued behind the active runner work and must pass native build, SIF conversion, deploy checks and the existing plugin tests before acceptance. This is attempt 1/6.
