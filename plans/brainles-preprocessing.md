# brainles-preprocessing: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.6.10.post1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

Upstream requires antspyx and explicitly describes source-build prerequisites. Screened antspyx 0.5.4/0.6.1 releases lack Linux ARM wheels but provide source distributions. This is a dependency build gap, not proof that ANTs/ITK fundamentally require x86.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/brainles-preprocessing/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py311_24.9.2-0`.
- Declared download inputs: `hdbet_0_model`, `hdbet_1_model`, `hdbet_2_model`, `hdbet_3_model`, `hdbet_4_model`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/186). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `antspyx-0.5.4`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `antspyx-0.6.1`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BrainLesion/preprocessing upstream documentation](https://github.com/BrainLesion/preprocessing/blob/main/README.md).
- [BrainLesion/preprocessing pyproject.toml](https://github.com/BrainLesion/preprocessing/blob/main/pyproject.toml).
- [BrainLesion/preprocessing release v0.6.13](https://github.com/BrainLesion/preprocessing/releases/tag/v0.6.13).
- [antspyx-0.5.4 published package metadata](https://pypi.org/pypi/antspyx/0.5.4/json).
- [antspyx-0.6.1 published package metadata](https://pypi.org/pypi/antspyx/0.6.1/json).

## Plan and acceptance criteria

Use the upstream antspyx build procedure for the exact resolved version, informed by the BrainLesion failure record. Identify a released/configuration fix before repeating that failed path. Validate registration, normalization and skull stripping with the pinned models.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/brainles-preprocessing/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-14

The upstream ANTsPy documentation explicitly supports installing from source with `python -m pip install .` and lists BLAS, LAPACK, Fortran, PNG, CMake and Python development packages as possible Linux prerequisites. Based on that released build route, candidate [`2f061f36896188f8be2d00b73519d819c8c2d164`](https://github.com/Vbitz/neurocontainers/commit/2f061f36896188f8be2d00b73519d819c8c2d164) is pushed on [`arm64/brainles-preprocessing-source`](https://github.com/Vbitz/neurocontainers/tree/arm64/brainles-preprocessing-source), based on accepted submodule pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`.

The candidate declares `aarch64`, adds the documented native build packages only to the ARM64 image, and installs the exact compatible `antspyx==0.5.4` source distribution with `--no-binary=antspyx` before installing the unchanged BrainLesion package. The x86_64 wheel path and fulltest are preserved. Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. Native verification is queued until one of the four current runs completes; it must pass the existing build, SIF, deploy and fulltest gates before acceptance. This is attempt 1/6 for the source investigation, with the window starting when dispatched and a 12-hour deadline.

The candidate is now dispatched as [run 34777430024](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777430024). The investigation window is `2026-09-13T19:21:12Z`–`2026-09-14T07:21:12Z`; this remains attempt 1/6 and requires native Docker build, SIF conversion, deploy checks and the existing fulltest suite before acceptance.

The first attempt failed before staging because Zenodo returned HTTP 504 for `hdbet_0_model` after three downloader retries. The one permitted unchanged retry is [run 34777631695](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777631695), using the same candidate SHA and counted as attempt 2/6. If this retry sees another Zenodo failure, classify the recipe as infrastructure-blocked without further retries; the source build has not yet been exercised.

## Bounded outcome — 2026-09-14

The unchanged retry also failed before staging with HTTP 504 for the same declared `hdbet_0_model` download after three builder retries. The native source-build candidate was therefore not exercised. This is a concrete infrastructure blocker after two attempts, not evidence that the released antspyx source cannot compile on ARM64. Revisit when the Zenodo record is reachable reliably or an authorized stable mirror is available; preserve candidate `2f061f36896188f8be2d00b73519d819c8c2d164` on `arm64/brainles-preprocessing-source` and do not repeat the unchanged dispatch.

The final outcome is recorded in [issue #186](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5655583825).

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-infrastructure**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5655583825).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Changed-infrastructure follow-up — 2026-09-14

A direct preflight at `2026-09-14T18:49:41Z` returned HTTP 200 and `application/octet-stream` for all five declared HD-BET model URLs. This changes the prior data-service condition that prevented both native attempts from reaching Docker staging. The existing source-build candidate `2f061f36896188f8be2d00b73519d819c8c2d164` was therefore reopened as attempt 3/6 in a fresh 12-hour window and dispatched on the native ARM64 workflow as [run 34883244804](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34883244804). The issue checkpoint is [#186](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5669009474), with the exact dispatch recorded [here](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5669022628).

Require the full ARM64 Docker build, SIF conversion, deploy checks and complete existing fulltest before considering the route verified. The candidate remains based on its recorded earlier accepted source and must be rebased and retested serially before integration if it passes.

## Native source-build result — 2026-09-15

The changed-data candidate `2f061f36896188f8be2d00b73519d819c8c2d164` passed the native ARM64 Docker build, SIF conversion, deploy checks and all 16 fulltests in [run 34883244804](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34883244804). The issue reporter records 16 passed, 0 failed and 0 skipped in [issue #186](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5669707592).

Because that candidate was based on the older parent `685f5f4d9636d34aa8237646535d2a7dfc3a525d`, its single recipe commit was cherry-picked onto the current accepted pin `2ad9c2ff6c9762868c99ebbe3ac59b7f895cfc51`. The integrated candidate is `bfa2364d60f7cd99e83b813a48f6c39d41c6945e` on `integration/brainles-preprocessing`; local validation and ARM64/x86_64 generation passed. Exact native retest is queued as attempt 4/6 in [run 34888489034](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34888489034), with the dispatch checkpoint in [issue #186](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5669775446). Acceptance remains pending that exact integrated result.

## Accepted ARM64 result — 2026-09-15

The serially integrated candidate `bfa2364d60f7cd99e83b813a48f6c39d41c6945e` passed the exact native ARM64 workflow `34888489034`: Docker build, architecture verification, SIF conversion, deploy checks, and fulltest all passed (16 passed, 0 failed, 0 skipped). The submodule pin was advanced from `2ad9c2ff6c9762868c99ebbe3ac59b7f895cfc51` and pushed in root commit `b8d2189`. Issue: https://github.com/Vbitz/neurocontainers-arm64/issues/186
