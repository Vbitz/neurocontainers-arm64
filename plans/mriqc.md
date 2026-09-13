# mriqc: ARM64 research plan

Researched: 2026-09-13. Recipe version: `24.0.2`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

MRIQC is source available, and the container bundles external imaging dependencies behind an amd64 image. The obstacle is the complete matching environment, not the Python quality metrics themselves. Registration/skull-stripping helpers need native builds.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mriqc/build.yaml).
- Base image expression: `nipreps/mriqc:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/214). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `nipreps/mriqc:24.0.2`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [nipreps/mriqc upstream documentation](https://github.com/nipreps/mriqc/blob/master/README.rst).
- [nipreps/mriqc Dockerfile](https://github.com/nipreps/mriqc/blob/master/Dockerfile).
- [nipreps/mriqc pyproject.toml](https://github.com/nipreps/mriqc/blob/master/pyproject.toml).
- [nipreps/mriqc release 25.0.0rc0](https://github.com/nipreps/mriqc/releases/tag/25.0.0rc0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/nipreps/mriqc/manifests/24.0.2).

## Plan and acceptance criteria

Audit the 24.0.2 Dockerfile and external executables; resolve native prerequisites and preserve the original IQM/report pipeline. Validate structural and functional image-quality outputs against the existing fixtures.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mriqc/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
