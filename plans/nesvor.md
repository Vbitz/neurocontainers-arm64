# nesvor: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5.0`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

NeSVoR's Dockerfile and setup explicitly compile CUDA extensions and use tiny-cuda-nn. Its source is public, but the core reconstruction path requires GPU support absent from the native CPU runner. This is stronger evidence than an amd64 image alone.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/nesvor/build.yaml).
- Base image expression: `junshenxu/nesvor:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/220). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `junshenxu/nesvor:v0.5.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [daviddmc/NeSVoR upstream documentation](https://github.com/daviddmc/NeSVoR/blob/master/README.md).
- [daviddmc/NeSVoR Dockerfile](https://github.com/daviddmc/NeSVoR/blob/master/Dockerfile).
- [daviddmc/NeSVoR setup.py](https://github.com/daviddmc/NeSVoR/blob/master/setup.py).
- [daviddmc/NeSVoR release v0.5.0](https://github.com/daviddmc/NeSVoR/releases/tag/v0.5.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/junshenxu/nesvor/manifests/v0.5.0).

## Plan and acceptance criteria

Require an appropriate native ARM NVIDIA GPU environment and supported matching CUDA/PyTorch/tiny-cuda-nn builds for complete testing. Do not replace the neural reconstruction with another implementation; validate actual reconstructed volumes if those prerequisites become available.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/nesvor/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
