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
