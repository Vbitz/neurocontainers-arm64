# meica: ARM64 research plan

Researched: 2026-09-13. Recipe version: `4.0.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

MEICA4 source is available, but the recipe downloads a matched meica-afni-runtime-linux-x86_64 bundle. Upstream describes using externally installed AFNI on macOS, indicating the runtime bundle is a distribution mechanism rather than the entire algorithm.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/meica/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `meica_source`, `meica_afni_runtime`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/151). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [ME-ICA/me-ica upstream documentation](https://github.com/ME-ICA/me-ica/blob/main/README.md).
- [ME-ICA/me-ica Dockerfile](https://github.com/ME-ICA/me-ica/blob/main/Dockerfile).
- [ME-ICA/me-ica requirements.txt](https://github.com/ME-ICA/me-ica/blob/main/requirements.txt).
- [ME-ICA/me-ica release 4.0.1](https://github.com/ME-ICA/me-ica/releases/tag/4.0.1).
- [ME-ICA/meica-afni upstream documentation](https://github.com/ME-ICA/meica-afni/blob/master/README.md).
- [ME-ICA/meica-afni release 4.0.1](https://github.com/ME-ICA/meica-afni/releases/tag/4.0.1).

## Plan and acceptance criteria

Identify the matched AFNI source/revision and required utilities, and build an equivalent native runtime rather than copying x86 libraries. Preserve MEICA4's environment and validate multi-echo denoising and its quantitative reports.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/meica/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/151#issuecomment-5651349311).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
