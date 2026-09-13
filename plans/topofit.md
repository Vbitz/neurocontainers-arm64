# topofit: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5.1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The earlier claim that all three wheels are x86-only is incorrect: brainnet and brainsynth are platform-independent wheels; cortech is the explicit x86_64 native wheel. Upstream also identifies CUDA extensions for training. ARM cortech and the recipe's inference/device contract need resolution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/topofit/build.yaml).
- Base image expression: `pytorch/pytorch:2.6.0-cuda11.8-cudnn9-runtime`.
- Declared download inputs: `fsaverage_sphere`, `lh_cortex`, `rh_cortex`, `brainnet_wheel`, `brainsynth_wheel`, `cortech_wheel`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/236). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `v0.2` lists: `brainnet-0.2-py3-none-any.whl`. This release metadata establishes asset availability, not a passed native test.

Release `v0.1` lists: `brainsynth-0.1-py3-none-any.whl`. This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [simnibs/brainnet upstream documentation](https://github.com/simnibs/brainnet/blob/main/README.md).
- [simnibs/brainnet pyproject.toml](https://github.com/simnibs/brainnet/blob/main/pyproject.toml).
- [simnibs/brainnet release v0.2](https://github.com/simnibs/brainnet/releases/tag/v0.2).
- [simnibs/brainsynth upstream documentation](https://github.com/simnibs/brainsynth/blob/main/README.md).
- [simnibs/brainsynth pyproject.toml](https://github.com/simnibs/brainsynth/blob/main/pyproject.toml).
- [simnibs/brainsynth release v0.1](https://github.com/simnibs/brainsynth/releases/tag/v0.1).

## Plan and acceptance criteria

Build the exact cortech source through upstream configuration, inspect which mesh extensions inference uses, and resolve the supported CPU/GPU mode without dropping functionality. Test cortical surface geometry and OpenRecon outputs with the original weights.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/topofit/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-14

Upstream Cortech's v0.1 documentation provides a native source build through Conan and Meson, and the released Conan profile can be selected for ARM64. Candidate [`383a955c977619a8c64d2e2340ff724f551fe8f9`](https://github.com/Vbitz/neurocontainers/commit/383a955c977619a8c64d2e2340ff724f551fe8f9) is pushed on [`arm64/topofit-cortech-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/topofit-cortech-arm), based on accepted submodule pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`.

The candidate declares `aarch64`, uses the multi-architecture Ubuntu 24.04 base and official ARM64 CPU torch 2.6.0, builds Cortech v0.1 from its source archive with Conan's native `armv8` profile, and installs the unchanged pure-Python BrainNet and BrainSynth wheels. The x86_64 CUDA base and Cortech wheel path are preserved. The fulltest retains the CUDA 11.8 assertion for x86_64 and checks the ARM64 CPU runtime separately while exercising the same geometry and real CPU TopoFit workflows. Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. Native verification is queued behind the four active runs; this is attempt 1/6.

Because Napari advanced the accepted pin to `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc`, the TopoFit recipe change was replayed as integrated candidate [`c8e10fe8e0263b5ceecb53489856daf332ddf419`](https://github.com/Vbitz/neurocontainers/commit/c8e10fe8e0263b5ceecb53489856daf332ddf419) on [`arm64/topofit-cortech-arm-integrated`](https://github.com/Vbitz/neurocontainers/tree/arm64/topofit-cortech-arm-integrated). Validation and ARM64/x86_64 generation passed again. This exact integrated SHA is the candidate for native dispatch; acceptance requires its own native build, SIF, deploy and fulltest evidence.

Exact native dispatch is [run 34778187761](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778187761), attempt 1/6, started at `2026-09-13T19:36:05Z` with a deadline of `2026-09-14T07:36:05Z`.
