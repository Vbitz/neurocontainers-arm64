# metabody: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.5`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The recipe combines an x86 AFNI/R bundle, an installer with only an x86 branch, Python code and OpenRecon integration. AFNI source and ARM Python distributions provide plausible routes. BodyLocaliser task data are not themselves architecture-specific.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/metabody/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `update_afni_binaries`, `linux_ubuntu_24_R_4_3_libs_tgz`, `miniconda_installer`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/211). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [thomshaw92/BodyLocaliser upstream documentation](https://github.com/thomshaw92/BodyLocaliser/blob/main/README.md).
- [thomshaw92/BodyLocaliser requirements.txt](https://github.com/thomshaw92/BodyLocaliser/blob/main/requirements.txt).

## Plan and acceptance criteria

Build native AFNI/R dependencies and add the matching ARM installer path, keeping the same event data and reconstruction code. Validate the MRD-to-image path and AFNI first-level processing output; capture any specific native dependency failure.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/metabody/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
