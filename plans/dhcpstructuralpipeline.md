# dhcpstructuralpipeline: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The project explicitly documents native source installation. Its CMake build needs MIRTK and VTK and the pipeline adds a legacy imaging toolchain. The published-image limitation is not evidence that this source pipeline is fundamentally x86-only.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/dhcpstructuralpipeline/build.yaml).
- Base image expression: `biomedia/dhcp-structural-pipeline:latest@{{ context.base_image_digest }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/194). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `biomedia/dhcp-structural-pipeline:latest@sha256:318a11ba9d70fdca2fb96200afabe0109722c9072bc71b9644f65c6c10de57b3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BioMedIA/dhcp-structural-pipeline upstream documentation](https://github.com/BioMedIA/dhcp-structural-pipeline/blob/master/README.md).
- [BioMedIA/dhcp-structural-pipeline CMakeLists.txt](https://github.com/BioMedIA/dhcp-structural-pipeline/blob/master/CMakeLists.txt).
- [BioMedIA/dhcp-structural-pipeline Dockerfile](https://github.com/BioMedIA/dhcp-structural-pipeline/blob/master/Dockerfile).
- [Registry manifest inspected](https://registry-1.docker.io/v2/biomedia/dhcp-structural-pipeline/manifests/sha256:318a11ba9d70fdca2fb96200afabe0109722c9072bc71b9644f65c6c10de57b3).

## Plan and acceptance criteria

Follow release-matched native installation instructions and map the surface/segmentation dependencies. Build those with ordinary ARM configuration and compare neonatal segmentation and cortical surfaces; capture the first unsupported dependency if one appears.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/dhcpstructuralpipeline/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
