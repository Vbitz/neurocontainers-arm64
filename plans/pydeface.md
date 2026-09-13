# pydeface: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.2`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

PyDeface source is available and primarily requires FSL registration tools. The old inherited FSL image is the immediate barrier. Official ARM FSL packages provide a concrete path worth testing, although their version compatibility with the pinned 2.0.2 recipe must be checked.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/pydeface/build.yaml).
- Base image expression: `vnmd/fsl_6.0.3:20200905`.
- Declared download inputs: `miniconda_sh`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/161). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `vnmd/fsl_6.0.3:20200905`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [poldracklab/pydeface upstream documentation](https://github.com/poldracklab/pydeface/blob/master/README.md).
- [poldracklab/pydeface Dockerfile](https://github.com/poldracklab/pydeface/blob/master/Dockerfile).
- [poldracklab/pydeface pyproject.toml](https://github.com/poldracklab/pydeface/blob/master/pyproject.toml).
- [poldracklab/pydeface release v2.1.0](https://github.com/poldracklab/pydeface/releases/tag/v2.1.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/vnmd/fsl_6.0.3/manifests/20200905).

## Plan and acceptance criteria

Build on a native base with the same PyDeface source and compatible FSL commands, retaining templates and settings. Test actual defacing: removed facial voxels, preserved brain data and unchanged image geometry.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/pydeface/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
