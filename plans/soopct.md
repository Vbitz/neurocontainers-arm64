# soopct: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The pipeline publishes Python source, but registration needs antspyx and some normalization paths require SynthSR. Screened antspyx releases provide source but no ARM wheel. Upstream explicitly identifies the additional SynthSR dependency, so conversion-only success would not verify the full workflow.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/soopct/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda py313_25.5.1-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/232). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `antspyx-0.5.4`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `antspyx-0.6.1`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [rordenlab/soop-ct upstream documentation](https://github.com/rordenlab/soop-ct/blob/main/README.md).
- [rordenlab/soop-ct requirements.txt](https://github.com/rordenlab/soop-ct/blob/main/requirements.txt).
- [antspyx-0.5.4 published package metadata](https://pypi.org/pypi/antspyx/0.5.4/json).
- [antspyx-0.6.1 published package metadata](https://pypi.org/pypi/antspyx/0.6.1/json).

## Plan and acceptance criteria

Resolve the exact ANTsPy source build and native SynthSR environment without changing implementations. Test DICOM-to-BIDS conversion plus registration/normalization outputs; use existing BrainLesion evidence to avoid repeating a known unmodified failing build.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/soopct/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation candidate — 2026-09-14

Candidate [`d4566cb95d73717f55176350179fb8cb8f1f776f`](https://github.com/Vbitz/neurocontainers/commit/d4566cb95d73717f55176350179fb8cb8f1f776f)
is pushed on [`arm64/soopct-antspyx-source`](https://github.com/Vbitz/neurocontainers/tree/arm64/soopct-antspyx-source), based on accepted pin `8bcc3e3d`. It declares ARM64, preserves the Python 3.13 x86_64 template unchanged, and uses the known working Python 3.11 ARM route with native `build-essential`, CMake and image-library packages. ARM explicitly installs antspyx 0.5.4 from source; the pure Python SOOP-CT, BrainChop, NumPy, SciPy and NiBabel dependencies remain unchanged. Local validation and both architecture generations pass.

This candidate is queued behind the four active native runs. Acceptance requires the exact ARM64 build, SIF conversion, deploy checks and the full SOOP-CT conversion, BrainChop CLI and dependency fulltests. A concrete first build error will determine whether the source route is feasible or blocked upstream.

Because TopoFit advanced the accepted pin to `88e6776aeb27f16ef43e015acb426b7e87fe0d1c`, the recipe commit was replayed unchanged as candidate [`d977311057123bb1efdb704ea7b4f9858ae52ad2`](https://github.com/Vbitz/neurocontainers/commit/d977311057123bb1efdb704ea7b4f9858ae52ad2) on [`arm64/soopct-antspyx-source-topofit`](https://github.com/Vbitz/neurocontainers/tree/arm64/soopct-antspyx-source-topofit). Validation and ARM64/x86_64 Dockerfile generation passed. Exact native run [34780565877](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34780565877) is attempt 1/6; the report must establish whether the native antspyx route passes the complete runtime suite.

## Implementation outcome — 2026-09-14

Run [34780565877](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34780565877) built the ARM64 image and SIF and passed deploy checks plus 5/6 fulltests. The only failure was importing the source-built ANTsPy extension because Miniconda's bundled `libstdc++.so.6` lacked `GLIBCXX_3.4.30`, while the Ubuntu 24.04 system runtime provides it.

Candidate [`3185beb81152728d6abc16cda172ca06270535b1`](https://github.com/Vbitz/neurocontainers/commit/3185beb81152728d6abc16cda172ca06270535b1) adds ARM64 `libstdc++6` and points Miniconda's standard library soname at `/usr/lib/aarch64-linux-gnu/libstdc++.so.6`. The x86_64 route is unchanged. Local validation and both architecture generations pass. The first invalid dispatch was canceled before checkout and is not an attempt; the corrected exact native retry is [run 34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956), attempt 2/6. Acceptance still requires all build, SIF, deploy and fulltest gates.

After PALS advanced the accepted pin to `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`, the two SOOP-CT commits were replayed as candidate [`e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5`](https://github.com/Vbitz/neurocontainers/commit/e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5) on [`arm64/soopct-pals`](https://github.com/Vbitz/neurocontainers/tree/arm64/soopct-pals). Validation and both architecture generations pass. Dispatch this exact descendant for integrated verification only after the active SoopCT run establishes that the runtime fix is effective.
