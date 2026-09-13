# vesselboost: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.64`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

Upstream now documents CPU installation as well as CUDA, contradicting a GPU-only label. Its current CPU requirements still include antspyx 0.4.2, while the recipe pins a different source/runtime snapshot and inherits CUDA torch. Exact dependency and model compatibility remain unresolved.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/vesselboost/build.yaml).
- Base image expression: `pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime`.
- Declared download inputs: `vesselboost_zip`, `synthstrip_weights`, `manual_0429`, `omelette1_0429`, `omelette2_0429`, `t2s_mod_ep1k2_0728`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/239). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [KMarshallX/VesselBoost upstream documentation](https://github.com/KMarshallX/VesselBoost/blob/master/README.md).
- [KMarshallX/VesselBoost environment.yml](https://github.com/KMarshallX/VesselBoost/blob/master/environment.yml).
- [KMarshallX/VesselBoost requirements.txt](https://github.com/KMarshallX/VesselBoost/blob/master/requirements.txt).
- [KMarshallX/VesselBoost release v2.0.5](https://github.com/KMarshallX/VesselBoost/releases/tag/v2.0.5).

## Plan and acceptance criteria

Inspect the pinned source's CPU device handling, retain model files, and resolve its antspyx/native dependencies. Validate vessel segmentation and test-time adaptation if advertised. Use current CPU documentation as a lead, not proof for the pinned version.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/vesselboost/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-14

Candidate `0e80eb6d366ef992c52e3b6777af599ae5dc004e` is pushed on `arm64/vesselboost-cpu-arm`, based on accepted pin `8bcc3e3d`. It declares ARM64, selects the official Python 3.11 multi-architecture base and CPU PyTorch 2.5.0 stack, and builds the pinned antspyx 0.4.2 source distribution with ordinary native prerequisites. The x86 CUDA path remains unchanged. Local validation and both architecture generations pass.

The initial dispatch [34778576148](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778576148) used an abbreviated ref and failed before checkout because GitHub could not resolve it; it is metadata-only and is not recipe evidence. The corrected exact dispatch uses the full candidate SHA in [run 34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), attempt 1/6, with investigation window `2026-09-13T19:43:51Z`–`2026-09-14T07:43:51Z`. Acceptance requires the native build, SIF conversion, deploy checks and complete VesselBoost fulltest.

Because TopoFit advanced the accepted pin to `88e6776aeb27f16ef43e015acb426b7e87fe0d1c`, the recipe change was replayed as candidate [`a95b10b2079a98b60652392acd857433035da60a`](https://github.com/Vbitz/neurocontainers/commit/a95b10b2079a98b60652392acd857433035da60a) on [`arm64/vesselboost-topofit`](https://github.com/Vbitz/neurocontainers/tree/arm64/vesselboost-topofit). Validation and ARM64/x86_64 Dockerfile generation passed. If the active older-base run passes, this exact current-pin candidate requires a fresh native verification before acceptance.

After PALS advanced the accepted pin to `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`, the VesselBoost ARM64 commit was replayed as candidate [`6d47f60d5ff28aac70af62d4d133406bf8a025be`](https://github.com/Vbitz/neurocontainers/commit/6d47f60d5ff28aac70af62d4d133406bf8a025be) on [`arm64/vesselboost-pals`](https://github.com/Vbitz/neurocontainers/tree/arm64/vesselboost-pals). Validation and both architecture generations pass. Dispatch this exact descendant after the active VesselBoost run is reviewed, if another accepted pin has not superseded it.

The older-base run [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136) completed with 43/46 tests passed. The three failures were the no-proxy, preprocessing, and alternate-model TTA tests, each hitting the default 120-second timeout; the native build, SIF, deploy checks, prediction, training, proxy TTA, and remaining checks passed. Candidate `f5e832e68861afee8823074ce72d83c932ccd2e1` adds a 300-second timeout to those existing tests only, was validated locally for both architectures, and was dispatched from the current accepted pin in [run 34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), attempt 2/6. Acceptance remains pending the complete native result.

After SoopCT advanced the accepted pin to `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5`, the ARM64 recipe and timeout commits were replayed as candidate `aa85e3af73e3a933e1552eb9d995a804be7eae8c` on `arm64/vesselboost-soopct`. Validation and ARM64/x86_64 Dockerfile generation passed. The active timeout retry `34783650179` remains the previous-pin verification; dispatch this exact descendant after reviewing it.

The PALS-based timeout retry passed [run 34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179) with 46/46 native fulltests and no skips. After QuPath advanced the accepted pin to `c98a89ee6799cd32b6a2247554cf8447a37f24aa`, the same ARM64 and timeout commits were replayed as candidate `0d952620` on `arm64/vesselboost-qupath`. The branch is pushed; validation and ARM64/x86_64 Dockerfile generation pass. Dispatch this exact current-pin descendant for acceptance verification.
