# cpac: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.8.7`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

C-PAC source is public; its image wraps multiple native neuroimaging stages. A missing ARM manifest only blocks reuse of that image. Rebuilding the matching AFNI/ANTs/FSL/FreeSurfer environment and preserving pipeline outputs is the substantive work.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/cpac/build.yaml).
- Base image expression: `fcpindi/c-pac:{{ context.base_image_tag }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/244). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `fcpindi/c-pac:release-v1.8.7.post1.dev3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [FCP-INDI/C-PAC upstream documentation](https://github.com/FCP-INDI/C-PAC/blob/main/README.md).
- [FCP-INDI/C-PAC Dockerfile](https://github.com/FCP-INDI/C-PAC/blob/main/Dockerfile).
- [FCP-INDI/C-PAC requirements.txt](https://github.com/FCP-INDI/C-PAC/blob/main/requirements.txt).
- [FCP-INDI/C-PAC setup.py](https://github.com/FCP-INDI/C-PAC/blob/main/setup.py).
- [FCP-INDI/C-PAC release v1.3.0.post2](https://github.com/FCP-INDI/C-PAC/releases/tag/v1.3.0.post2).
- [Registry manifest inspected](https://registry-1.docker.io/v2/fcpindi/c-pac/manifests/release-v1.8.7.post1.dev3).

## Plan and acceptance criteria

Inspect the exact release's staged Dockerfiles and enumerate every required native artifact. Build prerequisites from supported sources and validate a small complete configured C-PAC workflow, including preprocessing and connectivity outputs.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/cpac/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
