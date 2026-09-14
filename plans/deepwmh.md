# deepwmh: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

DeepWMH and its nnU-Net fork are source available; installation delegates PyTorch selection to the user. The recipe's CUDA image and native ANTs/FSL tooling are concrete packaging barriers, but do not prove an ARM-incompatible algorithm.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/deepwmh/build.yaml).
- Base image expression: `nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04`.
- Builder templates: `miniconda py311_24.9.2-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/136). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [lchdl/DeepWMH upstream documentation](https://github.com/lchdl/DeepWMH/blob/develop/README.md).
- [lchdl/DeepWMH setup.py](https://github.com/lchdl/DeepWMH/blob/develop/setup.py).
- [lchdl/DeepWMH release v1.0.1](https://github.com/lchdl/DeepWMH/releases/tag/v1.0.1).
- [ANTsX/ANTs upstream documentation](https://github.com/ANTsX/ANTs/blob/main/README.md).
- [ANTsX/ANTs CMakeLists.txt](https://github.com/ANTsX/ANTs/blob/main/CMakeLists.txt).
- [ANTsX/ANTs Dockerfile](https://github.com/ANTsX/ANTs/blob/main/Dockerfile).
- [ANTsX/ANTs release v2.6.5](https://github.com/ANTsX/ANTs/releases/tag/v2.6.5).

## Plan and acceptance criteria

Check the pinned inference command's CPU support, resolve the exact nnU-Net environment and rebuild native preprocessing tools. If GPU is mandatory, retain a runner prerequisite. Test the same white-matter lesion segmentation with fixed models and inputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/deepwmh/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/136#issuecomment-5651346340).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
