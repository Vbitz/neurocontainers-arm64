# emuses: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.3.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recorded native build failed because the production lock demands triton 3.3.1, which has no ARM wheel in the inspected release. EMUSES itself is Python source. The lock includes a GPU compiler package even though CPU functionality may not require it.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/emuses/build.yaml).
- Base image expression: `python:3.11-slim-bookworm`.
- Declared download inputs: `emuses_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/94). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34737868781); use the issue for exact candidate SHA and failure context.

## Upstream findings

Package `triton-3.3.1`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [chrisfoulon/emuses upstream documentation](https://github.com/chrisfoulon/emuses/blob/main/README.md).
- [chrisfoulon/emuses Dockerfile](https://github.com/chrisfoulon/emuses/blob/main/Dockerfile).
- [chrisfoulon/emuses requirements.txt](https://github.com/chrisfoulon/emuses/blob/main/requirements.txt).
- [chrisfoulon/emuses setup.py](https://github.com/chrisfoulon/emuses/blob/main/setup.py).
- [chrisfoulon/emuses release v1.3.0](https://github.com/chrisfoulon/emuses/releases/tag/v1.3.0).
- [triton-3.3.1 published package metadata](https://pypi.org/pypi/triton/3.3.1/json).

## Plan and acceptance criteria

Check the release's direct requirements and torch platform markers to determine whether upstream allows an ARM CPU lock without Triton. If the lock is mandatory, require an upstream compatible release. Preserve predictive-model training, inference and serialization checks.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/emuses/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

- The earlier native candidate stopped during `pip-sync` because the x86-generated lock pinned `triton==3.3.1`, which had no ARM64 distribution. The pinned PyTorch 2.7.1 release publishes a native Linux aarch64 wheel and declares its NVIDIA/Triton closure for x86_64 only.
- Candidate `685f5f4d9636d34aa8237646535d2a7dfc3a525d` on `arm64/emuses-integrated-80a` preserves the exact x86 lock and, only on native aarch64, removes the generated NVIDIA/Triton lock entries before the unchanged `pip-sync` step. Local validation and ARM64/x86_64 Dockerfile generation pass.
- The candidate is pushed and waiting for a native runner slot. Exact dispatch, SIF conversion, deploy checks and the existing EMUSES fulltest remain required before acceptance.
- Exact native retry [34775307167](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775307167) is now dispatched as attempt 3/6. It uses candidate `685f5f4d9636d34aa8237646535d2a7dfc3a525d`; inspect the complete build and runtime evidence before integration.

The candidate passed native Docker build, SIF conversion, deploy checks and 2/2 fulltests (0 failed, 0 skipped) in [run 34775307167](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775307167). Because it descends directly from accepted pin `80a84327a6659b0ac79a44f2c1853faa9eb84f4b`, it is accepted for serial top-level integration at `685f5f4d9636d34aa8237646535d2a7dfc3a525d`.

## Accepted implementation — 2026-09-14

The verified candidate `685f5f4d9636d34aa8237646535d2a7dfc3a525d` remains an ancestor of accepted submodule pin `41ddfbf5010657e0185ab1d7730b42149e8fb744`. Its ARM-only lock filtering removes the x86-only NVIDIA/Triton closure while preserving the CPU PyTorch route, and its native run passed 2/2 fulltests with no skips. No additional EMUSES build is required.

## Current upstream runtime investigation (2026-10-13)

Current released EMUSES v1.3.0 builds natively on ARM64, converts to SIF and passes deploy plus original help/import tests, but strict runtime proof fails:3/5 aggregate,2/4 functional. pip check reports missing pytest/pytest-asyncio required by released setup.py (its embedded distribution version is0.7.0, distinct from release tag1.3.0). The actual nested UMAP/HDBSCAN pipeline fits the embedding and initial clusterer, then all-fixed documented parameter configuration fails when inner_optimize_hdbscan falls back to raw {value:...} dictionaries and passes them to final HDBSCAN instead of integers: ValueError: Min samples and min cluster size must be integers! Released clustering_utils.py lines223-256 confirm the cause. Other released helper API errors were also observed statically. Latest official release remainsv1.3.0; no directly applicable released fix found. This is an upstream application runtime defect, not evidence of an ARM64 compiler limitation. Adding packaging dependencies alone cannot repair scientific pipeline execution. Preserve the failing capability check and experimental branch; no application patch, substituted implementation, parameter-mode workaround or ignored error. Revisit with an official released correction for fixed-parameter final-model construction and complete dependency metadata, then retest actual outputs/model persistence.

Evidence: https://github.com/Vbitz/neurocontainers-arm64/issues/94#issuecomment-6136957192; exact native run https://github.com/Vbitz/neurocontainers-arm64/actions/runs/38336405010.

## Current implementation verification — 2026-10-19

The CPU route is now verified at source `e35f92ad2553447ed86133a983ac12e5175d854a`.
Restoring PyTorch's architecture markers removes only the flattened x86 NVIDIA/Triton
requirements on ARM. The released scientific dependency pins remain. The recipe
also installs the two declared requirements from the released development lock,
and distinguishes distribution metadata `0.7.0` from release `1.3.0`.

The supported literal HDBSCAN parameters preserve the same fixed values and trial
mode. Actual 72-point UMAP/HDBSCAN fitting, finite transforms, accurate clustering,
unchanged inputs, saved models/data/plots and exact reload assertions pass. The
adjusted Rand score is 1.0. [Native ARM verification](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/39219604100)
passes **5/5**, and [upstream ARM and x86](https://github.com/neurodesk/neurocontainers/actions/runs/39220788043)
each pass **5/5**, with no failures/skips and both image-quality checks passing.
[PR #3707](https://github.com/neurodesk/neurocontainers/pull/3707) is merged.
Automatic publication is tracked separately; these tests alone do not assert publication.
