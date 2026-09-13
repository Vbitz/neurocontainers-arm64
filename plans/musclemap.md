# musclemap: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.4.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Upstream explicitly supports CPU operation and provides source; the recipe nevertheless inherits a CUDA PyTorch image. That image choice does not establish a GPU-only algorithm. The model/software revisions, SCT integration and OpenRecon dependencies still need ARM validation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/musclemap/build.yaml).
- Base image expression: `pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime`.
- Declared download inputs: `musclemap_zip`, `spinalcordtoolbox_tar`, `wholebody_model_pth`, `wholebody_model_json`, `abdomen_model_pth`, `abdomen_model_json`, `forearm_model_pth`, `forearm_model_json`, `leg_model_pth`, `leg_model_json`, `pelvis_model_pth`, `pelvis_model_json` (additional model/data inputs are in the recipe).
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/218). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MuscleMap/MuscleMap upstream documentation](https://github.com/MuscleMap/MuscleMap/blob/main/README.md).
- [MuscleMap/MuscleMap requirements.txt](https://github.com/MuscleMap/MuscleMap/blob/main/requirements.txt).
- [MuscleMap/MuscleMap setup.py](https://github.com/MuscleMap/MuscleMap/blob/main/setup.py).
- [MuscleMap/MuscleMap release 2.0](https://github.com/MuscleMap/MuscleMap/releases/tag/2.0).
- [spinalcordtoolbox/spinalcordtoolbox upstream documentation](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/README.rst).
- [spinalcordtoolbox/spinalcordtoolbox Dockerfile](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/Dockerfile).
- [spinalcordtoolbox/spinalcordtoolbox requirements.txt](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/requirements.txt).
- [spinalcordtoolbox/spinalcordtoolbox setup.py](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/setup.py).
- [spinalcordtoolbox/spinalcordtoolbox release 7.3](https://github.com/spinalcordtoolbox/spinalcordtoolbox/releases/tag/7.3).

## Plan and acceptance criteria

Recreate the pinned torch 2.4.1 CPU environment on an ARM base and preserve all models, GUI and integration code. Validate whole-body/regional segmentation and MRD output; retain any independent SCT dependency blocker without dropping its functionality.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/musclemap/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
