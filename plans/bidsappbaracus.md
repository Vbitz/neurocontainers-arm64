# bidsappbaracus: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.4.post1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

BARACUS source is available, but upstream explicitly requires FreeSurfer 5.3.0 rather than the HCP variant. Its Dockerfile also installs an old x86 Anaconda distribution. Brain-age models are coupled to the preprocessing outputs; a newer FreeSurfer is not automatically equivalent.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsappbaracus/build.yaml).
- Base image expression: `bids/baracus:v{{ context.upstream_version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/128). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/baracus:v1.1.4`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/baracus upstream documentation](https://github.com/bids-apps/baracus/blob/master/README.md).
- [bids-apps/baracus Dockerfile](https://github.com/bids-apps/baracus/blob/master/Dockerfile).
- [bids-apps/baracus setup.py](https://github.com/bids-apps/baracus/blob/master/setup.py).
- [bids-apps/baracus release v1.1.4](https://github.com/bids-apps/baracus/releases/tag/v1.1.4).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/baracus/manifests/v1.1.4).

## Plan and acceptance criteria

Establish a same-version FreeSurfer source build and an ARM Python environment compatible with the model serialization. Test feature extraction and brain-age predictions against the existing fixture before accepting a dependency migration.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsappbaracus/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
