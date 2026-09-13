# brainlesion: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

A native attempt already reached the antspyx/ITK build and failed in source setup, including a missing master ref and PNG/ZLIB configuration. That is concrete bounded investigation evidence, not an instruction-set incompatibility. Source exists for the dependency.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/brainlesion/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda py310_25.5.1-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/247). Earlier labels are historical claims, not independent proof of a fundamental blocker.

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

Preserve the recorded candidate and first errors. Revisit only with an applicable released antspyx build fix or documented source configuration. Keep registration, skull stripping, segmentation and atlas tests intact; do not infer ARM failure for independent pure-Python components.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/brainlesion/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Keep the recorded failure as the current blocker for that candidate. A released upstream fix or documented configuration addressing its first error is the condition for a justified retry. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
