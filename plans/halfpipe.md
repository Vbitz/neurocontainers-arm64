# halfpipe: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.2.3`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

HALFpipe publishes source and inherits fMRIPrep in its Dockerfile. The complete container adds a large neuroimaging/statistics stack; no ARM image is available for the pinned wrapper. The dependency inheritance, not absence of HALFpipe source, explains the current barrier.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/halfpipe/build.yaml).
- Base image expression: `halfpipe/halfpipe:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/107). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `halfpipe/halfpipe:1.2.3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [HALFpipe/HALFpipe upstream documentation](https://github.com/HALFpipe/HALFpipe/blob/main/README.rst).
- [HALFpipe/HALFpipe Dockerfile](https://github.com/HALFpipe/HALFpipe/blob/main/Dockerfile).
- [HALFpipe/HALFpipe pyproject.toml](https://github.com/HALFpipe/HALFpipe/blob/main/pyproject.toml).
- [HALFpipe/HALFpipe release 1.3.2](https://github.com/HALFpipe/HALFpipe/releases/tag/1.3.2).
- [Registry manifest inspected](https://registry-1.docker.io/v2/halfpipe/halfpipe/manifests/1.2.3).

## Plan and acceptance criteria

Inspect the 1.2.3 source image and lock, resolve fMRIPrep/native prerequisites, and reconstruct the matching environment. Test preprocessing and statistical outputs together. An independently working Python component is not proof that the inherited workflow is complete.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/halfpipe/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
