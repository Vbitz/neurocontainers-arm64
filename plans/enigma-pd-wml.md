# enigma-pd-wml: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

An x86 Miniforge installer is a routine packaging fix; Miniforge supports ARM. The harder unresolved inputs are the inherited cvriend/pgs image, its UNet environment and the FSL preprocessing package set. The earlier installer-only blocker was insufficient.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/enigma-pd-wml/build.yaml).
- Base image expression: `cvriend/pgs:latest`.
- Declared download inputs: `miniforge_installer`, `enigma_pd_wml_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/139). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `cvriend/pgs:latest`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [UCL/Enigma-PD-WML upstream documentation](https://github.com/UCL/Enigma-PD-WML/blob/main/README.md).
- [UCL/Enigma-PD-WML Dockerfile](https://github.com/UCL/Enigma-PD-WML/blob/main/Dockerfile).
- [UCL/Enigma-PD-WML environment.yml](https://github.com/UCL/Enigma-PD-WML/blob/main/environment.yml).
- [UCL/Enigma-PD-WML release v1.1.1](https://github.com/UCL/Enigma-PD-WML/releases/tag/v1.1.1).
- [conda-forge/miniforge upstream documentation](https://github.com/conda-forge/miniforge/blob/main/README.md).
- [conda-forge/miniforge release 26.7.2-0](https://github.com/conda-forge/miniforge/releases/tag/26.7.2-0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/cvriend/pgs/manifests/latest).

## Plan and acceptance criteria

Inspect the pgs source/lock and build an equivalent ARM environment, then resolve the exact FSL packages. Preserve lesion inference and preprocessing. Record the first real unsupported dependency rather than stopping at the installer URL.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/enigma-pd-wml/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/139#issuecomment-5651346957).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
