# relion: ARM64 research plan

Researched: 2026-09-13. Recipe version: `4.0.1.sm75`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

RELION itself has a public source build with optional CUDA acceleration. This recipe is specifically an sm75 CUDA environment and includes MotionCor2 plus other external executables. Its complete capability set cannot be tested on a CPU-only ARM runner; RELION is not inherently GPU-only.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/relion/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `relion_source`, `cuda_pin`, `cuda_repo_deb`, `ctffind_archive`, `motioncor2_zip`, `go_archive`, `singularity_archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/163). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [3dem/relion upstream documentation](https://github.com/3dem/relion/blob/master/README.md).
- [3dem/relion CMakeLists.txt](https://github.com/3dem/relion/blob/master/CMakeLists.txt).
- [3dem/relion environment.yml](https://github.com/3dem/relion/blob/master/environment.yml).
- [3dem/relion pyproject.toml](https://github.com/3dem/relion/blob/master/pyproject.toml).
- [3dem/relion release 5.1.0](https://github.com/3dem/relion/releases/tag/5.1.0).

## Plan and acceptance criteria

Audit the pinned 4.0.1 CPU build as a distinct supported mode, but preserve the existing GPU variant and external tools. Full GPU verification requires native ARM NVIDIA hardware and matching helper binaries. Test reconstruction/refinement output, not just CMake success.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/relion/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
