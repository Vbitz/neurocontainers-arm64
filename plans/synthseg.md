# synthseg: ARM64 research plan

Researched: 2026-09-13. Recipe version: `8.2.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Upstream explicitly supports CPU inference, and TensorFlow 2.13.1 has Linux ARM wheels. The recipe installs Python scripts and model data, not an unavoidable monolithic FreeSurfer executable. Its CUDA base is a packaging choice; the earlier blanket native-release blocker was inaccurate.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/synthseg/build.yaml).
- Base image expression: `nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04`.
- Declared download inputs: `mri_synthseg`, `FreeSurferColorLUT`, `synthseg_1.0.h5`, `synthseg_2.0.h5`, `synthseg_robust_2.0.h5`, `synthseg_parc_2.0.h5`, `synthseg_qc_2.0.h5`, `synthseg_photo_both_1.0.h5`, `synthseg_photo_single_1.0.h5`, `synthseg_segmentation_labels.npy`, `synthseg_segmentation_labels_2.0.npy`, `synthseg_segmentation_names.npy` (additional model/data inputs are in the recipe).
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/235). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-2.13.1`: 4 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BBillot/SynthSeg upstream documentation](https://github.com/BBillot/SynthSeg/blob/master/README.md).
- [BBillot/SynthSeg setup.py](https://github.com/BBillot/SynthSeg/blob/master/setup.py).
- [tensorflow-2.13.1 published package metadata](https://pypi.org/pypi/tensorflow/2.13.1/json).

## Plan and acceptance criteria

Recreate the same Python/TensorFlow/Surfa environment on an ARM CPU base and preserve every model and OpenRecon wrapper. Validate standard and robust segmentation, volumes/QC outputs and reconstruction integration using the existing assertions.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/synthseg/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `815cf1b3e10b0b4b6003dc728f4300c54ccc3116` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **18/18** fulltests in [run 34753249262](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34753249262). The ARM route uses CPU TensorFlow wheels and preserves the SynthSeg models, runtime assertions, and x86_64 path.
