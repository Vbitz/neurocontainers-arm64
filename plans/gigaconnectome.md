# gigaconnectome: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.6.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The upstream Dockerfile builds a Python/Nilearn application from public source. Its published image being amd64-only is not a fundamental algorithm or dependency blocker. A matching ARM Python/scientific dependency environment is the outstanding requirement.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/gigaconnectome/build.yaml).
- Base image expression: `bids/giga_connectome:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/106). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/giga_connectome:0.6.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/giga_connectome upstream documentation](https://github.com/bids-apps/giga_connectome/blob/main/README.md).
- [bids-apps/giga_connectome Dockerfile](https://github.com/bids-apps/giga_connectome/blob/main/Dockerfile).
- [bids-apps/giga_connectome pyproject.toml](https://github.com/bids-apps/giga_connectome/blob/main/pyproject.toml).
- [bids-apps/giga_connectome requirements.txt](https://github.com/bids-apps/giga_connectome/blob/main/requirements.txt).
- [bids-apps/giga_connectome release 0.6.0](https://github.com/bids-apps/giga_connectome/releases/tag/0.6.0).
- [nilearn/nilearn upstream documentation](https://github.com/nilearn/nilearn/blob/main/README.rst).
- [nilearn/nilearn package.json](https://github.com/nilearn/nilearn/blob/main/package.json).
- [nilearn/nilearn pyproject.toml](https://github.com/nilearn/nilearn/blob/main/pyproject.toml).
- [nilearn/nilearn release 0.14.1](https://github.com/nilearn/nilearn/releases/tag/0.14.1).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/giga_connectome/manifests/0.6.0).

## Plan and acceptance criteria

Rebuild the 0.6.0 Dockerfile using an ARM-capable base with the same requirements. Preserve parcellation data and output schema, and run a small time-series/connectome computation with expected matrix dimensions and values.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/gigaconnectome/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `dc1439d82ec42fd3cb5b38e85ca1d5800a3484b2` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **94/94** fulltests in [run 34757505350](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757505350). The ARM route rebuilds the Python/Nilearn application on the multi-architecture Bookworm base while preserving its x86_64 image route.
