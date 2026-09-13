# clinica: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.10.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Clinica is Python source and documents pipeline-specific external dependencies. This container promises a broader FSL/FreeSurfer/MRtrix/ANTs stack. Its complete dependency set is unverified on ARM; a successful Python install would not verify all pipelines.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/clinica/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `miniconda py310_25.5.1-0`, `fsl 6.0.7.16`, `spm12 r7487`, `freesurfer 7.4.1`, `ants 2.4.3`, `mrtrix3 3.0.4`, `dcm2niix latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/189). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [aramis-lab/clinica upstream documentation](https://github.com/aramis-lab/clinica/blob/dev/README.md).
- [aramis-lab/clinica environment.yml](https://github.com/aramis-lab/clinica/blob/dev/environment.yml).
- [aramis-lab/clinica pyproject.toml](https://github.com/aramis-lab/clinica/blob/dev/pyproject.toml).
- [aramis-lab/clinica release v0.11.3](https://github.com/aramis-lab/clinica/releases/tag/v0.11.3).

## Plan and acceptance criteria

Map the pinned recipe's tests and advertised pipelines to exact external tools. Port the required tools serially, then test representative image processing end to end. Do not treat optional upstream dependencies as essential without checking how this container uses them.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/clinica/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
