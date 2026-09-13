# openmsk: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.2.0`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

This recipe explicitly asserts CUDA 11.8 torch and assembles several musculoskeletal tools. Their sources are available, and TensorFlow 2.14 has ARM CPU wheels, but a CPU package cannot satisfy the existing CUDA capability contract. Individual tools may support CPU operation; the full set is unresolved.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/openmsk/build.yaml).
- Base image expression: `tensorflow/tensorflow:2.14.0-gpu`.
- Declared download inputs: `dosma_sagittal_model`, `dosma_coronal_model`, `dosma_axial_model`, `nnunet_fullres_dataset`, `nnunet_fullres_model_config`, `nnunet_fullres_plans`, `nnunet_fullres_checkpoint_best`, `pymskt_right_knee_reference`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/223). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-2.14.0`: 3 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [gattia/nsm upstream documentation](https://github.com/gattia/nsm/blob/main/README.md).
- [gattia/nsm pyproject.toml](https://github.com/gattia/nsm/blob/main/pyproject.toml).
- [gattia/nsm requirements.txt](https://github.com/gattia/nsm/blob/main/requirements.txt).
- [gattia/nsm setup.py](https://github.com/gattia/nsm/blob/main/setup.py).
- [gattia/DOSMA upstream documentation](https://github.com/gattia/DOSMA/blob/master/README.md).
- [gattia/DOSMA pyproject.toml](https://github.com/gattia/DOSMA/blob/master/pyproject.toml).
- [gattia/DOSMA requirements.txt](https://github.com/gattia/DOSMA/blob/master/requirements.txt).
- [gattia/DOSMA setup.py](https://github.com/gattia/DOSMA/blob/master/setup.py).
- [tensorflow-2.14.0 published package metadata](https://pypi.org/pypi/tensorflow/2.14.0/json).

## Plan and acceptance criteria

Audit NSM, DOSMA, KneePipeline and pymskt at their pinned revisions for mandatory device and native-extension requirements. Preserve the GPU variant or define an explicitly supported CPU variant only if all functions remain available. Validate segmentation and anatomical modeling, not imports alone.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/openmsk/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
