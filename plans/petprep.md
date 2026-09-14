# petprep: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.5`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

PETPrep source is public, but its image assembles a substantial native registration/segmentation environment. Current upstream Dockerfiles also install MATLAB runtime components for FreeSurfer. The pinned 0.0.5 image must be examined at its own revision before transferring current requirements.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/petprep/build.yaml).
- Base image expression: `nipreps/petprep:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/112). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `nipreps/petprep:0.0.5`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [nipreps/petprep upstream documentation](https://github.com/nipreps/petprep/blob/main/README.rst).
- [nipreps/petprep Dockerfile](https://github.com/nipreps/petprep/blob/main/Dockerfile).
- [nipreps/petprep pyproject.toml](https://github.com/nipreps/petprep/blob/main/pyproject.toml).
- [nipreps/petprep requirements.txt](https://github.com/nipreps/petprep/blob/main/requirements.txt).
- [nipreps/petprep release 0.0.10](https://github.com/nipreps/petprep/releases/tag/0.0.10).
- [Registry manifest inspected](https://registry-1.docker.io/v2/nipreps/petprep/manifests/0.0.5).

## Plan and acceptance criteria

Map the pinned pipeline's external tools and mandatory MCR calls. Resolve native preprocessing prerequisites and retain any runtime blocker for required stages. Test a complete small PET BIDS workflow and quantitative outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/petprep/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/112#issuecomment-5651282564).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
