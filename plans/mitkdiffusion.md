# mitkdiffusion: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.2.0.post1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

MITK Diffusion explicitly documents building from source using its Qt/CMake superbuild. Its prebuilt Linux archive is not an ARM candidate. The matching MITK/ITK/VTK/Qt versions and diffusion modules need native validation; this is not evidence of an inherent architecture prohibition.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mitkdiffusion/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/213). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MIC-DKFZ/MITK-Diffusion upstream documentation](https://github.com/MIC-DKFZ/MITK-Diffusion/blob/master/README.md).
- [MIC-DKFZ/MITK-Diffusion release v2.0.1](https://github.com/MIC-DKFZ/MITK-Diffusion/releases/tag/v2.0.1).

## Plan and acceptance criteria

Use the exact artifact revision and corresponding build guide, resolve native dependencies and preserve the GUI/CLI modules. Validate diffusion reconstruction, image I/O and tractography output before claiming the entire application works.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mitkdiffusion/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
