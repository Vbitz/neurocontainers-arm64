# openadscpu: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The source project supports CPU use and pins antspyx 0.5.4, which has a source distribution but no inspected Linux ARM wheel. The absence of a wheel does not prove a fundamental ANTs/ITK port is needed; the bounded BrainLesion source failure is relevant evidence to investigate.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/openadscpu/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/66). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `antspyx-0.5.4`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `antspyx-0.6.1`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [farialab/OpenADS upstream documentation](https://github.com/farialab/OpenADS/blob/main/README.md).
- [farialab/OpenADS setup.py](https://github.com/farialab/OpenADS/blob/main/setup.py).
- [antspyx-0.5.4 published package metadata](https://pypi.org/pypi/antspyx/0.5.4/json).
- [antspyx-0.6.1 published package metadata](https://pypi.org/pypi/antspyx/0.6.1/json).

## Plan and acceptance criteria

Use the upstream ANTsPy build procedure only with an applicable configuration/release fix for the observed dependency failure. Preserve torch/model versions and test registration, lesion segmentation and report generation on native ARM.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/openadscpu/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

The ARM64 source route was implemented and integrated in candidate
`6103a923f43106c039ddf22a59c99c25352e459b`. It passed native Docker build,
architecture verification, SIF conversion, deploy checks, and all **3/3**
fulltests in [run 34759549792](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759549792).
The candidate is an ancestor of the accepted submodule pin
`df8a470aa8f1d5c45ffe2ac43fe39193a11e05d1`, so the successful route remains
accepted without a duplicate build.
