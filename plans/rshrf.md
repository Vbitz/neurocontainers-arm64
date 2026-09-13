# rshrf: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.7.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The BIDS rsHRF repository is the Python implementation and its Dockerfile uses Python plus installable dependencies. It links a separate MATLAB implementation, which should not be conflated with this container. An amd64-only image is the current packaging obstacle.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/rshrf/build.yaml).
- Base image expression: `bids/rshrf:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/115). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/rshrf:v1.7.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/rsHRF upstream documentation](https://github.com/bids-apps/rsHRF/blob/master/README.md).
- [bids-apps/rsHRF Dockerfile](https://github.com/bids-apps/rsHRF/blob/master/Dockerfile).
- [bids-apps/rsHRF pyproject.toml](https://github.com/bids-apps/rsHRF/blob/master/pyproject.toml).
- [bids-apps/rsHRF requirements.txt](https://github.com/bids-apps/rsHRF/blob/master/requirements.txt).
- [bids-apps/rsHRF setup.py](https://github.com/bids-apps/rsHRF/blob/master/setup.py).
- [bids-apps/rsHRF release v1.7.0](https://github.com/bids-apps/rsHRF/releases/tag/v1.7.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/rshrf/manifests/v1.7.0).

## Plan and acceptance criteria

Rebuild the v1.7.0 source and dependency environment on ARM, preserving BIDS entry points. Test HRF estimation and deconvolution with expected output shape and numerical results; inspect compiled dependencies before claiming success.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/rshrf/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
