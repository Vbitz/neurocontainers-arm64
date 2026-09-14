# mrsimetabolicconnectome: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The source pipeline is public, while the recipe pins a broad environment with antspyx, CUDA-oriented packages and Qt. Current source documentation has evolved, so it cannot prove the pinned 1.0.0 set works on ARM. ANTsPy source availability and CPU optionality need separate consideration.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mrsimetabolicconnectome/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/215). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MRSI-Psychosis-UP/MRSI-Metabolic-Connectome upstream documentation](https://github.com/MRSI-Psychosis-UP/MRSI-Metabolic-Connectome/blob/main/README.md).
- [MRSI-Psychosis-UP/MRSI-Metabolic-Connectome pyproject.toml](https://github.com/MRSI-Psychosis-UP/MRSI-Metabolic-Connectome/blob/main/pyproject.toml).
- [MRSI-Psychosis-UP/MRSI-Metabolic-Connectome requirements.txt](https://github.com/MRSI-Psychosis-UP/MRSI-Metabolic-Connectome/blob/main/requirements.txt).
- [MRSI-Psychosis-UP/MRSI-Metabolic-Connectome setup.py](https://github.com/MRSI-Psychosis-UP/MRSI-Metabolic-Connectome/blob/main/setup.py).
- [MRSI-Psychosis-UP/MRSI-Metabolic-Connectome release v1.0.2](https://github.com/MRSI-Psychosis-UP/MRSI-Metabolic-Connectome/releases/tag/v1.0.2).

## Plan and acceptance criteria

Inspect the pinned environment and actual use of CuPy/CuCIM/Qt, distinguishing mandatory operations from optional acceleration. Resolve native dependencies without deleting capabilities, then validate metabolic similarity matrices and preprocessing outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mrsimetabolicconnectome/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/215#issuecomment-5651534740).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
