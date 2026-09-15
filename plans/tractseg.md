# tractseg: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.9.post2`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recipe pins torch 1.6.0+cpu, whose inspected release lacks an ARM wheel, and also includes FSL/MRtrix. Current upstream TractSeg is source available and documents broader Python support, so the old environment pin is not proof of an intrinsic model limitation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/tractseg/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `mrtrix3 3.0.4`, `miniconda py37_23.1.0-1`, `fsl 6.0.7.16`.
- Declared download inputs: `pretrained_weights_tract_segmentation_xtract_v1.npz`, `pretrained_weights_tract_segmentation_v3.npz`, `pretrained_weights_endings_segmentation_v4.npz`, `pretrained_weights_dm_regression_xtract_v1.npz`, `pretrained_weights_dm_regression_v2.npz`, `pretrained_weights_peak_regression_part1_v2.npz`, `pretrained_weights_peak_regression_part2_v2.npz`, `pretrained_weights_peak_regression_part3_v2.npz`, `pretrained_weights_peak_regression_part4_v2.npz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/238). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `torch-1.6.0`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MIC-DKFZ/TractSeg upstream documentation](https://github.com/MIC-DKFZ/TractSeg/blob/master/Readme.md).
- [MIC-DKFZ/TractSeg setup.py](https://github.com/MIC-DKFZ/TractSeg/blob/master/setup.py).
- [torch-1.6.0 published package metadata](https://pypi.org/pypi/torch/1.6.0/json).

## Plan and acceptance criteria

Check the exact TractSeg 2.9 requirements and model compatibility for a documented newer torch CPU version. Resolve native FSL/MRtrix and preserve bundle segmentation/tracking outputs. A framework change requires scientific comparison, not just a successful import.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/tractseg/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-13

The first implementation candidate is pushed as [`a6bd2f46399657df8b56cfc12ce48f147796d1fc`](https://github.com/Vbitz/neurocontainers/commit/a6bd2f46399657df8b56cfc12ce48f147796d1fc) on [`arm64/tractseg-modern-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/tractseg-modern-arm), based on accepted submodule pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`. It keeps the existing x86_64 binary and Python 3.7/torch 1.6 route. The ARM64 path uses the pinned MRtrix3 3.0.4 source template and Miniconda py311 with the native `torch==2.4.1` wheel. This is an ordinary upstream source build and does not change the scientific toolchain.

Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. Native verification is pending; the candidate must pass the existing MRtrix, FSL, TractSeg, Tractometry and deployment fulltest assertions before acceptance. Investigation window: `2026-09-13T19:06:28Z` through `2026-09-14T07:06:28Z`, attempt 1/6. Issue checkpoint: [#238 comment](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5655429034).

## Attempt 1 result and unchanged retry — 2026-09-14

The first native dispatch, [run 34776715361](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776715361), did not reach Docker build. Builder staging retried the declared `best_weights_ep62.npz` download three times and received HTTP 504 from Zenodo each time. This is an infrastructure/data failure, not evidence against the ARM64 recipe changes.

The one permitted unchanged retry is dispatched as [run 34777140518](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777140518) using the same candidate SHA `a6bd2f46399657df8b56cfc12ce48f147796d1fc`. It is attempt 2/6 within the original investigation window. If the same download failure recurs, record an infrastructure blocker and move to the next recipe; do not alter the scientific tests or keep retrying the data service.

The unchanged retry failed in the same pre-build staging step: [run 34777140518](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777140518) received HTTP 504 from Zenodo for `best_weights_ep266.npz` after three downloader retries. Since two different declared weight files failed identically, the recipe is blocked by the external data service for this investigation. Revisit when the Zenodo records are reachable or the project provides a stable mirrored artifact; no further unchanged retry is justified.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-infrastructure**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5655511092).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Changed-infrastructure follow-up — 2026-09-14

A direct preflight at `2026-09-14T18:49:41Z` returned HTTP 200 and `application/octet-stream` for all nine declared TractSeg weight URLs, including the two files that failed in the earlier native staging attempts. This changes the prior data-service condition that prevented the ARM64 route from reaching Docker build. The existing native dependency candidate `a6bd2f46399657df8b56cfc12ce48f147796d1fc` was therefore reopened as attempt 3/6 in a fresh 12-hour window and dispatched on the native ARM64 workflow as [run 34883270646](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34883270646). The issue checkpoint is [#238](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5669009716), with the exact dispatch recorded [here](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5669022897).

Require the full ARM64 Docker build, SIF conversion, deploy checks and complete existing fulltest before considering the route verified. The candidate remains based on its recorded earlier accepted source and must be rebased and retested serially before integration if it passes.

## FSL platform fix — 2026-09-15

The changed-data candidate reached ARM64 MRtrix3 source compilation, Miniconda/Python, TractSeg installation and all nine weight files, then stopped at the FSL template in [run 34883270646](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34883270646). The first actionable error was `Cannot find a version of FSL matching platform` for FSL 6.0.7.16. The current official FSL manifest has no `linux-aarch64` entry for 6.0.7.16, while it publishes `6.0.7.22_linux-aarch64.yml`; the accepted FSL ARM64 recipe has already passed that supported route. The evidence is recorded in [issue #238](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5669726486).

Candidate `2c5b7a4e8f1366d18ace4f67c919a4361d563b2a` on `arm64/tractseg-modern-arm` now selects FSL 6.0.7.22 only for ARM64 and preserves 6.0.7.16 on x86_64. Recipe validation and both Dockerfile generations passed. It is dispatched as attempt 4/6 in [run 34888237665](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34888237665), with the dispatch checkpoint in [issue #238](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5669742396). Acceptance remains pending the native build, SIF, deploy and fulltest result.

## MRtrix GUI follow-up — 2026-09-15

The FSL-corrected candidate `2c5b7a4e8f1366d18ace4f67c919a4361d563b2a` built and passed 119/120 fulltests in native run `34888237665`; only `which mrview` failed. The ARM64 MRtrix source template defaults to `-nogui`, so the expected viewer was not installed. Candidate `711220fe` removes that option and adds the upstream documented Qt/OpenGL development packages only on ARM64. Local validation and both architecture generations passed. Exact native attempt 5/6 is run `34895895495`: https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5670698530

## Dispatch correction — 2026-09-15

Run `34895895495` was a setup-only failure caused by passing the short SHA `711220fe` to checkout; no recipe step ran. The same candidate was re-dispatched with full SHA `711220fe497d3d76103af7b25f7cdf0db8970789` as the intended native attempt 5/6 in run `34896019692`. Issue checkpoint: https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5670712666

## Final native attempt — 2026-09-15

Run `34896019692` failed during MRtrix configure with `Qt moc not found` because the candidate installed Qt after the source template. Candidate `6d8895ee29484f29eb1e799c364a8dca5950d8a8` moves the ARM-only Qt/OpenGL packages before the template; local validation and generation passed. Final native attempt 6/6: `34897243628`. Issue: https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5670855779

## Integrated retest checkpoint — 2026-09-15

The three TractSeg commits were replayed cleanly onto the accepted BrainLesion pin `bfa2364d60f7cd99e83b813a48f6c39d41c6945e`, producing integrated candidate `27ea0a8a3336d633f761b6921d6770bc22a9ba2a`. Local recipe validation and ARM64/x86_64 generation passed; the generated ARM64 Dockerfile installs Qt/OpenGL development packages before the MRtrix source configure and selects FSL 6.0.7.22, while x86_64 remains on FSL 6.0.7.16.

The exact integrated native retest is run `34904389457`: https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34904389457. Acceptance is pending build, SIF, deploy, and fulltest results. The abbreviated-ref setup run `34904352147` is recorded as non-evidence.

## Corrected integration retry — 2026-09-15

The first integrated replay omitted the fourth intended commit `711220fe`, leaving MRtrix configured with `-nogui`; exact run `34904389457` consequently failed only `MRtrix mrview check` at 119/120. The missing commit was added to the integration branch as `91ec1355ac6a0ffa4dc065dc415cc099ad5574d2`, and local validation plus both architecture generations confirm ARM64 GUI configure is enabled with Qt/OpenGL installed before configure.

The corrected exact native integration retest is [run 34910314613](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34910314613). The top-level pin remains unchanged pending this result.

## Current-pin replay after QuickShear acceptance — 2026-09-15

QuickShear is now the accepted submodule pin `7b70cacfbf0d2c04e8ef7fd7b355da0dff4a0a2e` in root commit `03c823387d8147f143e098713ecfc742177e4284`. Because the previously corrected TractSeg integration candidate was based on the prior pin, its four intended commits were replayed onto the current pin as `7bf9e3a1ea7846fde48b8c226dc280321c9d15b3` on `integration/tractseg-quickshear`.

Recipe validation and ARM64/x86_64 generation passed. The generated ARM64 Dockerfile keeps Qt/OpenGL installation before source MRtrix3 configuration, enables the viewer, and selects FSL 6.0.7.22; the x86_64 output retains the existing binary MRtrix and FSL 6.0.7.16 routes. Exact native ARM64 retest [run 34910862134](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34910862134) is pending. The run's top-level dispatcher SHA is expected to differ because `neurocontainers_ref` points to the full candidate SHA; source metadata must be checked before acceptance.
