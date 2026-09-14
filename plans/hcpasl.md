# hcpasl: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.2.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Upstream lists FSL, Workbench and FreeSurfer as prerequisites, including boundary-based registration. FSL now has official ARM packages and Workbench has source; the previous generic all-dependencies-unavailable claim is too broad. Full matching FreeSurfer functionality remains unresolved.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/hcpasl/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda {{ context.miniconda_version }}`, `fsl {{ context.fsl_version }}`, `freesurfer {{ context.freesurfer_version }}`.
- Declared download inputs: `hcp_asl_source`, `hcp_pipelines_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/201). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [physimals/hcp-asl upstream documentation](https://github.com/physimals/hcp-asl/blob/master/README.md).
- [physimals/hcp-asl requirements.txt](https://github.com/physimals/hcp-asl/blob/master/requirements.txt).
- [physimals/hcp-asl setup.py](https://github.com/physimals/hcp-asl/blob/master/setup.py).
- [Washington-University/HCPpipelines upstream documentation](https://github.com/Washington-University/HCPpipelines/blob/master/README.md).
- [Washington-University/HCPpipelines environment.yml](https://github.com/Washington-University/HCPpipelines/blob/master/environment.yml).
- [Washington-University/HCPpipelines release v6.0.0](https://github.com/Washington-University/HCPpipelines/releases/tag/v6.0.0).

## Plan and acceptance criteria

Resolve the recipe's FSL 6.0.7.22 and Workbench requirements on ARM, then establish the specific FreeSurfer BBR commands. Preserve HCP atlas inputs and compare surface-mapped perfusion outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/hcpasl/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/201#issuecomment-5651531967).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
