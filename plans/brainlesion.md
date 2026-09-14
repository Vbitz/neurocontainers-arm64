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

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/247#issuecomment-5652220143).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Implementation disposition — 2026-09-14

The implementation investigation is exhausted at the recipe boundary. Three native attempts were made in total: the original candidate failed because `antspyx==0.6.3` had no Linux ARM64 wheel and its source fallback could not find `g++`; candidate [`9d8d71c`](https://github.com/Vbitz/neurocontainers/commit/9d8d71cbff92fcce2e79ad0c6d464f494427376e9) added the compiler and reached the source setup, which then required `git` and `make`; candidate [`fc0e838`](https://github.com/Vbitz/neurocontainers/commit/fc0e838959b69665233dac90b63bdf9c3c4797c9) added those prerequisites and reached the bundled ITK/ANTs configuration. The final native run reported `pathspec 'master' did not match any file(s) known to git` and missing ZLIB/PNG development libraries. No SIF, deploy, or fulltest stage ran.

The final [issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/247#issuecomment-5652220143) records the two targeted recipe corrections and the stop at the upstream source-build boundary. Do not retry this recipe without a released Linux ARM64 `antspyx` wheel or documented ARM64 source-build instructions that address the ITK/ANTs branch and dependency failures.
