# neurodock: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0.post1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

NeuroDock bundles a legacy PyDesigner/native diffusion stack in an amd64 image. The linked upstream repository now redirects to PyDKE, so current documentation is not automatically evidence for the pinned 1.0.0 image. The exact historical source and external tools must be reconstructed.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/neurodock/build.yaml).
- Base image expression: `dmri/neurodock:v{{ context.upstream_version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/221). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `dmri/neurodock:v1.0.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [muscbridge/PyDesigner upstream documentation](https://github.com/muscbridge/PyDKE/blob/master/README.rst).
- [muscbridge/PyDesigner Dockerfile](https://github.com/muscbridge/PyDKE/blob/master/Dockerfile).
- [muscbridge/PyDesigner pyproject.toml](https://github.com/muscbridge/PyDKE/blob/master/pyproject.toml).
- [muscbridge/PyDesigner requirements.txt](https://github.com/muscbridge/PyDKE/blob/master/requirements.txt).
- [muscbridge/PyDesigner release v2.0.0](https://github.com/muscbridge/PyDKE/releases/tag/v2.0.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/dmri/neurodock/manifests/v1.0.0).

## Plan and acceptance criteria

Find the image's original Dockerfile/revision and map FSL/MRtrix and any GPU-specific components. Rebuild the same application, not its renamed successor by assumption. Test diffusion/kurtosis estimation and associated preprocessing outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/neurodock/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/221#issuecomment-5651535853).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
