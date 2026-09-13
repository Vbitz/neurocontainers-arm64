# nibabies: ARM64 research plan

Researched: 2026-09-13. Recipe version: `24.0.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

NiBabies has public source, but its complete infant pipeline assembles MCRIBS/MIRTK/ITK/VTK and other native imaging tools. A newer Dockerfile still contains architecture-specific library paths. The exact 24.0.0 dependency set needs reconstruction before support can be assessed.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/nibabies/build.yaml).
- Base image expression: `nipreps/nibabies:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/109). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `nipreps/nibabies:24.0.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [nipreps/nibabies upstream documentation](https://github.com/nipreps/nibabies/blob/master/README.md).
- [nipreps/nibabies Dockerfile](https://github.com/nipreps/nibabies/blob/master/Dockerfile).
- [nipreps/nibabies pyproject.toml](https://github.com/nipreps/nibabies/blob/master/pyproject.toml).
- [nipreps/nibabies release 26.0.1](https://github.com/nipreps/nibabies/releases/tag/26.0.1).
- [Registry manifest inspected](https://registry-1.docker.io/v2/nipreps/nibabies/manifests/24.0.0).

## Plan and acceptance criteria

Inspect the pinned release stages and map each external executable. Establish native builds without dropping infant-specific processing, then validate an infant BIDS workflow and segmentation/surface outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/nibabies/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
