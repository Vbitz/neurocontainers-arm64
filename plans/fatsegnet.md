# fatsegnet: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.gpu.post2`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

Upstream explicitly supports CPU and GPU Docker builds, contradicting a GPU-only interpretation. The actual obstacle is its old TensorFlow 1.6/associated Python stack, for which the inspected PyPI release has no ARM wheel.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fatsegnet/build.yaml).
- Base image expression: `tensorflow/tensorflow:1.6.0-gpu-py3`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/197). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-1.6.0`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Deep-MI/FatSegNet upstream documentation](https://github.com/Deep-MI/FatSegNet/blob/master/README.md).
- [Deep-MI/FatSegNet Dockerfile](https://github.com/Deep-MI/FatSegNet/blob/master/Dockerfile).
- [tensorflow-1.6.0 published package metadata](https://pypi.org/pypi/tensorflow/1.6.0/json).

## Plan and acceptance criteria

Check for an upstream-supported dependency update that preserves the released models. Otherwise a TensorFlow 1.x port is outside the recipe budget. A CPU variant is conceptually valid, but still needs that runtime and unchanged adipose-segmentation tests.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fatsegnet/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
