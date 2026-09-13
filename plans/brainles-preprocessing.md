# brainles-preprocessing: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.6.10.post1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

Upstream requires antspyx and explicitly describes source-build prerequisites. Screened antspyx 0.5.4/0.6.1 releases lack Linux ARM wheels but provide source distributions. This is a dependency build gap, not proof that ANTs/ITK fundamentally require x86.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/brainles-preprocessing/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py311_24.9.2-0`.
- Declared download inputs: `hdbet_0_model`, `hdbet_1_model`, `hdbet_2_model`, `hdbet_3_model`, `hdbet_4_model`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/186). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `antspyx-0.5.4`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `antspyx-0.6.1`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BrainLesion/preprocessing upstream documentation](https://github.com/BrainLesion/preprocessing/blob/main/README.md).
- [BrainLesion/preprocessing pyproject.toml](https://github.com/BrainLesion/preprocessing/blob/main/pyproject.toml).
- [BrainLesion/preprocessing release v0.6.13](https://github.com/BrainLesion/preprocessing/releases/tag/v0.6.13).
- [antspyx-0.5.4 published package metadata](https://pypi.org/pypi/antspyx/0.5.4/json).
- [antspyx-0.6.1 published package metadata](https://pypi.org/pypi/antspyx/0.6.1/json).

## Plan and acceptance criteria

Use the upstream antspyx build procedure for the exact resolved version, informed by the BrainLesion failure record. Identify a released/configuration fix before repeating that failed path. Validate registration, normalization and skull stripping with the pinned models.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/brainles-preprocessing/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
