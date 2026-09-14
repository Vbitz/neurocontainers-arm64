# nftsim: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.2`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

NFTsim publishes a C++11 source build and cross-platform guidance. The wrapper's amd64 GHCR image is a packaging limitation; there is no demonstrated intrinsic ARM requirement in the core simulator. MATLAB helpers are separate from the deployed CLI simulation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/nftsim/build.yaml).
- Base image expression: `ghcr.io/farwa-abbas/nftsim:{{ context.base_image_tag }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/222). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `ghcr.io/farwa-abbas/nftsim:1.0.2`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BrainDynamicsUSYD/nftsim upstream documentation](https://github.com/BrainDynamicsUSYD/nftsim/blob/master/README.md).
- [BrainDynamicsUSYD/nftsim release v.1.1.0](https://github.com/BrainDynamicsUSYD/nftsim/releases/tag/v.1.1.0).
- [Registry manifest inspected](https://ghcr.io/v2/farwa-abbas/nftsim/manifests/1.0.2).

## Plan and acceptance criteria

Build the source corresponding to 1.0.2 on a native base using its Makefile and supported compiler settings. Preserve sample configurations and executable paths, then run a numerical simulation and compare its output to the fulltest expectations.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/nftsim/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-13

The ARM64 source-build route was implemented on `arm64/integrate-nftsim-synthseg`.
Candidate `ce058afece0774f0fe915f3bc07c04507c7665bc` built the pinned C++11
source natively, passed SIF conversion and deploy checks, and passed all **68/68**
fulltests in [run 34754095890](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754095890).
The commit is an ancestor of the current accepted submodule pin
`df8a470aa8f1d5c45ffe2ac43fe39193a11e05d1`, so the tested recipe remains in the
accepted history without rerunning an unchanged recipe.

The ARM path keeps the published x86_64 image unchanged and builds the public
source with the ARM-compatible generic C++ flags. The numerical simulation and
all existing runtime assertions passed on native Linux ARM64.
