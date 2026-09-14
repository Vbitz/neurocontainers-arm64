# hypermapp3r: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.1.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recipe pins Python 3.7 and TensorFlow 1.15.5; upstream's setup also targets the TensorFlow 1.x generation and has discontinued local-install support. The old native ANTs/C3D binaries are additional obstacles. Source exists, but this legacy framework is not a routine ARM wheel installation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/hypermapp3r/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py311_24.9.2-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/202). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-1.15.5`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [AICONSlab/HyperMapp3r upstream documentation](https://github.com/AICONSlab/HyperMapp3r/blob/master/README.md).
- [AICONSlab/HyperMapp3r Dockerfile](https://github.com/AICONSlab/HyperMapp3r/blob/master/Dockerfile).
- [AICONSlab/HyperMapp3r requirements.txt](https://github.com/AICONSlab/HyperMapp3r/blob/master/requirements.txt).
- [AICONSlab/HyperMapp3r setup.py](https://github.com/AICONSlab/HyperMapp3r/blob/master/setup.py).
- [keras-team/keras-contrib upstream documentation](https://github.com/keras-team/keras-contrib/blob/master/README.md).
- [keras-team/keras-contrib setup.py](https://github.com/keras-team/keras-contrib/blob/master/setup.py).
- [tensorflow-1.15.5 published package metadata](https://pypi.org/pypi/tensorflow/1.15.5/json).

## Plan and acceptance criteria

The exact TensorFlow 1.15.5 PyPI release supplies only x86 wheels and no source archive. Check upstream supported container/dependency updates. Revisit only with a compatible released framework path and model-equivalence evidence. Rebuilding C3D alone will not make the segmentation network run.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/hypermapp3r/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/202#issuecomment-5651532162).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
