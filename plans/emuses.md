# emuses: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.3.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recorded native build failed because the production lock demands triton 3.3.1, which has no ARM wheel in the inspected release. EMUSES itself is Python source. The lock includes a GPU compiler package even though CPU functionality may not require it.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/emuses/build.yaml).
- Base image expression: `python:3.11-slim-bookworm`.
- Declared download inputs: `emuses_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/94). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34737868781); use the issue for exact candidate SHA and failure context.

## Upstream findings

Package `triton-3.3.1`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [chrisfoulon/emuses upstream documentation](https://github.com/chrisfoulon/emuses/blob/main/README.md).
- [chrisfoulon/emuses Dockerfile](https://github.com/chrisfoulon/emuses/blob/main/Dockerfile).
- [chrisfoulon/emuses requirements.txt](https://github.com/chrisfoulon/emuses/blob/main/requirements.txt).
- [chrisfoulon/emuses setup.py](https://github.com/chrisfoulon/emuses/blob/main/setup.py).
- [chrisfoulon/emuses release v1.3.0](https://github.com/chrisfoulon/emuses/releases/tag/v1.3.0).
- [triton-3.3.1 published package metadata](https://pypi.org/pypi/triton/3.3.1/json).

## Plan and acceptance criteria

Check the release's direct requirements and torch platform markers to determine whether upstream allows an ARM CPU lock without Triton. If the lock is mandatory, require an upstream compatible release. Preserve predictive-model training, inference and serialization checks.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/emuses/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
