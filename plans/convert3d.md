# convert3d: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

C3D has public C++ source and a CMake/ITK build. The pinned nightly download is x86_64, but needing ITK does not itself constitute an upstream port. No ARM compiler failure is recorded for this recipe.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/convert3d/build.yaml).
- Base image expression: `debian:bookworm`.
- Declared download inputs: `archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/133). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pyushkevich/c3d upstream documentation](https://github.com/pyushkevich/c3d/blob/master/README.md).
- [pyushkevich/c3d CMakeLists.txt](https://github.com/pyushkevich/c3d/blob/master/CMakeLists.txt).

## Plan and acceptance criteria

Resolve the source revision corresponding to the nightly artifact, pin it, and build with a compatible native ITK using upstream instructions. Test image resampling, arithmetic and all deployed C3D tools. Stop only if ordinary configuration exposes an actual unsupported dependency.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/convert3d/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
