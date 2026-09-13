# deeplabcut: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.3.11`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The previous missing-TensorFlow-2.12-ARM claim is contradicted by PyPI: ARM wheels exist, with a tensorflow-cpu-aws dependency. DeepLabCut source is available. Its GUI and pinned auxiliary environment still need validation; current 3.x documentation must not be substituted for the 2.3.11 recipe.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/deeplabcut/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/192). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-2.12.0`: 4 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `tensorflow-cpu-aws-2.12.0`: 4 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [DeepLabCut/DeepLabCut upstream documentation](https://github.com/DeepLabCut/DeepLabCut/blob/main/README.md).
- [DeepLabCut/DeepLabCut pyproject.toml](https://github.com/DeepLabCut/DeepLabCut/blob/main/pyproject.toml).
- [DeepLabCut/DeepLabCut setup.py](https://github.com/DeepLabCut/DeepLabCut/blob/main/setup.py).
- [DeepLabCut/DeepLabCut release v3.0.1](https://github.com/DeepLabCut/DeepLabCut/releases/tag/v3.0.1).
- [tensorflow-2.12.0 published package metadata](https://pypi.org/pypi/tensorflow/2.12.0/json).
- [tensorflow-cpu-aws-2.12.0 published package metadata](https://pypi.org/pypi/tensorflow-cpu-aws/2.12.0/json).

## Plan and acceptance criteria

Resolve the exact 2.3.11 environment and ARM CPU TensorFlow implementation. Check GUI bindings, video codecs and model dependencies. Test pose inference on a small clip with expected keypoints; retain any required training functionality.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/deeplabcut/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
