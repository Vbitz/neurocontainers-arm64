# topofit: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5.1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The earlier claim that all three wheels are x86-only is incorrect: brainnet and brainsynth are platform-independent wheels; cortech is the explicit x86_64 native wheel. Upstream also identifies CUDA extensions for training. ARM cortech and the recipe's inference/device contract need resolution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/topofit/build.yaml).
- Base image expression: `pytorch/pytorch:2.6.0-cuda11.8-cudnn9-runtime`.
- Declared download inputs: `fsaverage_sphere`, `lh_cortex`, `rh_cortex`, `brainnet_wheel`, `brainsynth_wheel`, `cortech_wheel`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/236). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `v0.2` lists: `brainnet-0.2-py3-none-any.whl`. This release metadata establishes asset availability, not a passed native test.

Release `v0.1` lists: `brainsynth-0.1-py3-none-any.whl`. This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [simnibs/brainnet upstream documentation](https://github.com/simnibs/brainnet/blob/main/README.md).
- [simnibs/brainnet pyproject.toml](https://github.com/simnibs/brainnet/blob/main/pyproject.toml).
- [simnibs/brainnet release v0.2](https://github.com/simnibs/brainnet/releases/tag/v0.2).
- [simnibs/brainsynth upstream documentation](https://github.com/simnibs/brainsynth/blob/main/README.md).
- [simnibs/brainsynth pyproject.toml](https://github.com/simnibs/brainsynth/blob/main/pyproject.toml).
- [simnibs/brainsynth release v0.1](https://github.com/simnibs/brainsynth/releases/tag/v0.1).

## Plan and acceptance criteria

Build the exact cortech source through upstream configuration, inspect which mesh extensions inference uses, and resolve the supported CPU/GPU mode without dropping functionality. Test cortical surface geometry and OpenRecon outputs with the original weights.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/topofit/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-14

Upstream Cortech's v0.1 documentation provides a native source build through Conan and Meson, and the released Conan profile can be selected for ARM64. Candidate [`383a955c977619a8c64d2e2340ff724f551fe8f9`](https://github.com/Vbitz/neurocontainers/commit/383a955c977619a8c64d2e2340ff724f551fe8f9) is pushed on [`arm64/topofit-cortech-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/topofit-cortech-arm), based on accepted submodule pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`.

The candidate declares `aarch64`, uses the multi-architecture Ubuntu 24.04 base and official ARM64 CPU torch 2.6.0, builds Cortech v0.1 from its source archive with Conan's native `armv8` profile, and installs the unchanged pure-Python BrainNet and BrainSynth wheels. The x86_64 CUDA base and Cortech wheel path are preserved. The fulltest retains the CUDA 11.8 assertion for x86_64 and checks the ARM64 CPU runtime separately while exercising the same geometry and real CPU TopoFit workflows. Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. Native verification is queued behind the four active runs; this is attempt 1/6.

Because Napari advanced the accepted pin to `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc`, the TopoFit recipe change was replayed as integrated candidate [`c8e10fe8e0263b5ceecb53489856daf332ddf419`](https://github.com/Vbitz/neurocontainers/commit/c8e10fe8e0263b5ceecb53489856daf332ddf419) on [`arm64/topofit-cortech-arm-integrated`](https://github.com/Vbitz/neurocontainers/tree/arm64/topofit-cortech-arm-integrated). Validation and ARM64/x86_64 generation passed again. This exact integrated SHA is the candidate for native dispatch; acceptance requires its own native build, SIF, deploy and fulltest evidence.

Exact native dispatch is [run 34778187761](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778187761), attempt 1/6, started at `2026-09-13T19:36:05Z` with a deadline of `2026-09-14T07:36:05Z`.

Run 34778187761 reached the ARM Cortech editable install but failed because
`meson-python` could not find Ninja 1.8.2 or newer. Conan's native dependency
build completed, so this was a directly actionable missing system package.
Candidate [`1e161313793613e5c6e8b3ae086e6e5488028eac`](https://github.com/Vbitz/neurocontainers/commit/1e161313793613e5c6e8b3ae086e6e5488028eac)
adds Debian's `ninja-build`, passes validation and both architecture
generations, and is pushed on the same integrated branch. Exact retry [run
34778828330](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778828330)
is attempt 2/6. The top-level pin remains unchanged pending native build, SIF,
deploy and fulltest evidence.

Retry 34778828330 passed the Ninja check but failed at Cortech's Meson
configure because `pkg-config` was absent while locating CGAL. Candidate
[`88e6776aeb27f16ef43e015acb426b7e87fe0d1c`](https://github.com/Vbitz/neurocontainers/commit/88e6776aeb27f16ef43e015acb426b7e87fe0d1c)
adds that ordinary Debian prerequisite, passes validation and both
architectures' generation, and is dispatched in exact [run
34779394328](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779394328),
attempt 3/6. This is the second direct recipe dependency fix; stop if the next
failure is an upstream native dependency issue.

## Native verification and acceptance — 2026-09-14

The candidate completed successfully in exact native run [34779394328](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779394328). Source `88e6776aeb27f16ef43e015acb426b7e87fe0d1c` on `arm64/topofit-cortech-arm-integrated` was based on accepted pin `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc`. ARM64 Docker build, architecture verification, SIF conversion, deploy checks, and fulltest all passed: 15 passed, 0 failed, 0 skipped, including the real CPU TopoFit workflow and output geometry checks.

This candidate is accepted as the new top-level submodule pin. The investigation used 3 recipe attempts: the first exposed missing `ninja-build`, the second exposed missing `pkg-config`, and the third passed after both documented Debian prerequisites were added. No upstream dependency port was required. Future candidates must descend from the new accepted pin.

## Accepted implementation — 2026-09-14

Candidate `88e6776aeb27f16ef43e015acb426b7e87fe0d1c` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **15/15** fulltests in [run 34779394328](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779394328). The ARM route adds the documented build prerequisites and runs the real CPU geometry/output workflow while preserving x86_64 packaging.
