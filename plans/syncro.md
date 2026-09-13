# syncro: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.1.1.post1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recipe uses an amd64 SynthStrip base with Python SynthSR, TensorFlow and antspyx. The linked SynthSR project documents standalone installation. The environment can plausibly be reconstructed, but the exact TensorFlow/model versions and ANTsPy source build remain unverified.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/syncro/build.yaml).
- Base image expression: `freesurfer/synthstrip:{{ context.synthstrip_version }}`.
- Declared download inputs: `MNI152_T1_1mm_brain_nii_gz`, `downloaded_file`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/234). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `freesurfer/synthstrip:1.8`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [neurolabusc/py_synthsr upstream documentation](https://github.com/neurolabusc/py_synthsr/blob/main/README.md).
- [neurolabusc/py_synthsr pyproject.toml](https://github.com/neurolabusc/py_synthsr/blob/main/pyproject.toml).
- [neurolabusc/py_synthsr requirements.txt](https://github.com/neurolabusc/py_synthsr/blob/main/requirements.txt).
- [Registry manifest inspected](https://registry-1.docker.io/v2/freesurfer/synthstrip/manifests/1.8).

## Plan and acceptance criteria

Build the same SynthStrip/SynthSR components on a native base and resolve the pinned TensorFlow/antspyx environment. Preserve synthesis, skull stripping and registration behavior; validate image geometry and output intensities rather than only imports.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/syncro/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation candidate — 2026-09-14

Candidate [`8dd676cecc56534da67f43997407e9237b4cb2ae8`](https://github.com/Vbitz/neurocontainers/commit/8dd676cecc56534da67f43997407e9237b4cb2ae8)
is pushed on [`arm64/syncro-native-components`](https://github.com/Vbitz/neurocontainers/tree/arm64/syncro-native-components), based on accepted pin `8bcc3e3d`. It preserves the x86_64 SynthStrip image route and reconstructs the ARM64 path from the accepted standalone SynthStrip recipe: FreeSurfer's upstream `mri_synthstrip` script and model files, PyTorch 2.2.2 CPU, surfa, an antspyx 0.5.4 source build, and the pinned py_synthsr source with TensorFlow 2.21.0. Local validation and both architecture generations pass.

The candidate is queued behind four active native jobs. Acceptance requires the exact ARM64 build, SIF conversion, deploy checks, SynthStrip output checks and the complete SYNcro/SynthSR fulltest. A native failure will distinguish an image reconstruction issue from an unsupported dependency.

Because TopoFit advanced the accepted pin to `88e6776aeb27f16ef43e015acb426b7e87fe0d1c`, the Syncro change was replayed onto that pin. Candidate [`0be219003af62ffcac5f673f6795034346de0b0d`](https://github.com/Vbitz/neurocontainers/commit/0be219003af62ffcac5f673f6795034346de0b0d) is pushed on [`arm64/syncro-native-components-topofit`](https://github.com/Vbitz/neurocontainers/tree/arm64/syncro-native-components-topofit). Validation and ARM64/x86_64 Dockerfile generation passed. It remains queued until a native slot opens.

After PALS advanced the accepted pin to `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`, the Syncro change was replayed as candidate `a186f7f89df41b56a8e3d937afd0d6eefa49d3b7` on `arm64/syncro-pals`. Validation and ARM64/x86_64 Dockerfile generation passed. Dispatch this exact candidate after a native slot opens for integrated verification.

After SoopCT advanced the accepted pin to `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5`, the Syncro change was replayed as candidate `c91eb0e5de57ad5dc6efd4cca25081983bfc9758` on `arm64/syncro-soopct`. Validation and ARM64/x86_64 Dockerfile generation passed. Dispatch this exact candidate when a native slot opens.

After QuPath advanced the accepted pin to `c98a89ee6799cd32b6a2247554cf8447a37f24aa`, the Syncro change was replayed as candidate `625e8944fe195e5175fab9835a42f1b0f80c5d3c` on `arm64/syncro-qupath`. Validation and ARM64/default-architecture Dockerfile generation passed. The exact candidate is dispatched in native ARM64 [run 34786442868](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786442868), attempt 1/6.

Run `34786442868` failed during ARM64 dependency installation because SciPy was incorrectly requested from the PyTorch CPU index, which has no Python 3.10/aarch64 SciPy distribution. Candidate `7d9d2a442ce492a6ce8b1df1e6a1f8bfc9cbde6` separates the PyPI NumPy/SciPy install from the PyTorch install, passes validation and both architecture generations, and is dispatched as attempt 2/6 in [run 34786862612](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786862612).

Run `34786862612` stopped at recipe checkout because the dispatch used a mistyped SHA; it did not run Docker or consume a substantive build attempt. The exact pushed candidate is `7d9d2a445467b75e4b881c27aae4f049fdac5050`, dispatched for the same targeted retry in [run 34786938986](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786938986).

Run `34786938986` reached the ARM64 Docker build but `antspyx==0.5.4` failed while configuring its bundled ITK: `Could NOT find PNG (missing: PNG_LIBRARY PNG_PNG_INCLUDE_DIR)`. The later missing `ITKConfig.cmake` error is downstream of that failure. Candidate `5c761183` on `arm64/syncro-antspyx-png` adds the documented ARM64 `libpng-dev` build dependency, preserving x86_64 and the complete source/runtime test route. Local validation and both architecture generations pass; dispatch this exact candidate as the next bounded retry when the open native slot is used.

The exact candidate `5c7611831036c5b0d22eab09254589031c9df017` is dispatched in native ARM64 [run 34787372368](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787372368). The immediately preceding abbreviated-SHA dispatch [34787340767](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787340767) was canceled at recipe checkout before Docker or tests and is not a substantive attempt.
