# fmriprep: ARM64 research plan

Researched: 2026-09-13. Recipe version: `25.2.5`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The published image is an assembly of Python and native preprocessing tools. The project provides its source and Dockerfile; its absent ARM manifest is a packaging obstacle. FreeSurfer and other complete preprocessing dependencies must be resolved for the recipe's actual advertised scope.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fmriprep/build.yaml).
- Base image expression: `nipreps/fmriprep:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/105). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `nipreps/fmriprep:25.2.5`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [nipreps/fmriprep upstream documentation](https://github.com/nipreps/fmriprep/blob/master/README.rst).
- [nipreps/fmriprep Dockerfile](https://github.com/nipreps/fmriprep/blob/master/Dockerfile).
- [nipreps/fmriprep pyproject.toml](https://github.com/nipreps/fmriprep/blob/master/pyproject.toml).
- [nipreps/fmriprep release 25.2.5](https://github.com/nipreps/fmriprep/releases/tag/25.2.5).
- [Registry manifest inspected](https://registry-1.docker.io/v2/nipreps/fmriprep/manifests/25.2.5).

## Plan and acceptance criteria

Audit the 25.2.5 image stages and lock, map each native artifact, and rebuild prerequisites from supported ARM sources/packages. Validate a minimal BIDS subject through preprocessing and reports; CLI success alone cannot verify the pipeline.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fmriprep/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
