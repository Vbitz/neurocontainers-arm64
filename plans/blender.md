# blender: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.0.1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Blender is open source with an extensive CMake build; choosing a linux-x64 archive in this recipe does not prove it cannot run on ARM64. The pinned release's full graphics, rendering and bundled-library configuration needs an ARM build.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/blender/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `blender_archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/122). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [blender/blender upstream documentation](https://github.com/blender/blender/blob/main/.github/README.md).
- [blender/blender CMakeLists.txt](https://github.com/blender/blender/blob/main/CMakeLists.txt).
- [blender/blender pyproject.toml](https://github.com/blender/blender/blob/main/pyproject.toml).

## Plan and acceptance criteria

Follow Blender's release-matched Linux build instructions, select supported generic CPU settings, and audit optional render backends. Preserve features covered by the recipe; test a headless rendered scene and normal GUI operation with the resulting binary.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/blender/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
