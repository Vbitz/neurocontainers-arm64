# dsistudio: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2024.06.12.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The pinned 2024 CPU archive is not an ARM selector, but the current upstream 2026.7.25 release explicitly includes dsi_studio_linux_universal_cpu_arm64.zip. Source is also public. A blanket unavailable-ARM-assets blocker is obsolete; the version difference must be addressed.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/dsistudio/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `dsi_studio_ubuntu2204_cpu_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/195). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `2026.7.25` lists: `dsi_studio_linux_universal_cpu.zip`, `dsi_studio_linux_universal_cpu_arm64.zip`, `dsi_studio_linux_universal_cuda.zip`, `dsi_studio_linux_universal_cuda_arm64.zip`, `dsi_studio_linux_universal_legacy_cpu.zip`, `dsi_studio_macos-14-arm64_qt6.zip`, `dsi_studio_ubuntu2204_arm64.zip`. This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [frankyeh/DSI-Studio upstream documentation](https://github.com/frankyeh/DSI-Studio/blob/master/README.md).
- [frankyeh/DSI-Studio release 2026.7.25](https://github.com/frankyeh/DSI-Studio/releases/tag/2026.7.25).

## Plan and acceptance criteria

Inspect the pinned source's CPU build path to preserve 2024 behavior, or plan a version-aligned update using the published 2026 ARM asset and corresponding x86 release. Validate reconstruction and tractography outputs; do not infer runtime success from the asset name.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/dsistudio/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

- The official 2026.7.25 ARM64 CPU binary built natively and passed SIF,
  deploy, registration, export, ordinary tracking and atlas checks, but the
  prior fulltest failed 16 of 84 checks. The first candidate's failures were
  release-layout mismatches rather than an ARM executable failure: connectivity
  matrices are written as `<tract>.<atlas>.connectivity.mat`, three current
  missing-input messages say `file not exist`, and the old AutoTrack shorthand
  IDs expand to atlas bundles that produce zero-result marker files. The
  pipeline also passed obsolete `--export_stat=1`, which the current binary
  reports as unrecognized. Evidence: [run 34763556926](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763556926).
- Candidate fulltest changes use the current connectivity names, exact release
  atlas IDs with known output, current missing-input wording, and rely on the
  current AutoTrack statistics output after removing the obsolete option.
  Recipe validation and ARM64/x86_64 generation pass.
- The three ARM64 recipe commits were replayed onto accepted PyDeface pin
  `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` as candidate
  `87f0dbb45ae3ab1d1b2b1a52ff0bcae14f18d89c` on
  `arm64/dsistudio-integrated-80a`. Dispatch is waiting for a native runner
  slot; this is a bounded follow-up to verify whether the release-aligned CLI
  assertions pass.

Further release-alignment: the first revised candidate still selected broad
shorthand AutoTrack names that the current human atlas expanded into
zero-result sub-bundles. Candidate `bdb427db440ea72de1e6fc50fc7a115c41fef5aa`
uses exact atlas IDs that produced non-empty tracts in the native report and
keeps the connectivity output and current error-message fixes. Validation and
both architecture generations pass. This is the candidate to dispatch when a
slot opens; no DSI run has been started for this final local revision yet.

Exact native retry [34774820860](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774820860) is now dispatched as attempt 2/6. It is based on the accepted PyDeface pin and must pass Docker build, architecture verification, SIF conversion, deploy checks and the fulltest before integration.

The native image built, converted and passed deploy checks, but [run 34774820860](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774820860) still failed five essential AutoTrack operations: multiple bundles, superior longitudinal fasciculus, corpus callosum, thalamic radiation and the pipeline multiple-bundle export. The final result was 78/83 executed fulltests passing, with no skips. These commands exit 1 with the official ARM64 CPU runtime even after release-aligned filenames, error strings, exact atlas IDs and CLI syntax were corrected. The recipe investigation is exhausted; revisit only with a released upstream ARM64 runtime/data or documented parameter fix for these required operations.

## Tracker disposition — 2026-09-14

- Coverage status: build **✅**, fulltest **❌**; plan assessment: **Plausible**.
- Investigation outcome: **failed-runtime**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/195#issuecomment-5655340599).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
