# aidamri: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.0`. Target: native Linux ARM64.

**Assessment: A recipe-level ARM route is now plausible; no fundamental blocker is established.**

AIDAmri is Python with source available. The container bundles an obsolete x86-only FSL 5.0.11 archive and a bundled Ubuntu 18.04 DSI Studio executable, while NiftyReg already builds from source. The current official FSL channel now publishes Linux aarch64 packages, and DSI Studio publishes ARM64 Linux releases, so the recipe can be tested by replacing those architecture-specific inputs conditionally while preserving the x86 path.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/aidamri/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `miniconda 4.7.12.1`.
- Declared download inputs: `aidamri_tar`, `niftyreg_tar`, `fsl_tar`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/119). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Aswendt-Lab/AIDAmri upstream documentation](https://github.com/Aswendt-Lab/AIDAmri/blob/master/README.md).
- [Aswendt-Lab/AIDAmri Dockerfile](https://github.com/Aswendt-Lab/AIDAmri/blob/master/Dockerfile).
- [Aswendt-Lab/AIDAmri requirements.txt](https://github.com/Aswendt-Lab/AIDAmri/blob/master/requirements.txt).
- [Aswendt-Lab/AIDAmri release v3.0](https://github.com/Aswendt-Lab/AIDAmri/releases/tag/v3.0).
- [KCL-BMEIS/niftyreg upstream documentation](https://github.com/KCL-BMEIS/niftyreg/blob/master/README.md).
- [KCL-BMEIS/niftyreg CMakeLists.txt](https://github.com/KCL-BMEIS/niftyreg/blob/master/CMakeLists.txt).
- [KCL-BMEIS/niftyreg release v2.0.0](https://github.com/KCL-BMEIS/niftyreg/releases/tag/v2.0.0).
- [Official FSL Linux aarch64 package index](https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/public/linux-aarch64/).
- [FSL architecture/build documentation](https://fsl.fmrib.ox.ac.uk/fsl/docs/development/management/build_system.html).
- [Official DSI Studio ARM64 downloads](https://dsi-studio.labsolver.org/download.html).
- [DSI Studio ARM64 release assets](https://github.com/frankyeh/DSI-Studio/releases).

## Plan and acceptance criteria

Use the accepted FSL ARM recipe path for the ARM build and select an official ARM64 DSI Studio release whose command line interface covers the commands invoked by AIDAmri. Compile the same NiftyReg revision, resolve the old Python 3.6 bootstrap on aarch64, and compare rodent registration and tractography outputs. A newer DSI release is a candidate dependency update and requires runtime validation against the existing AIDAmri tests.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/aidamri/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to one bounded recipe-level candidate from the current accepted pin. Stop if the FSL ARM environment does not provide the commands required by AIDAmri, if the DSI Studio release does not preserve those commands, or if the pinned Python dependency set has no supported aarch64 resolution. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Plausible route, candidate pending**.
- The prior blocked-prerequisite note is superseded by current official ARM64 FSL and DSI Studio releases. The exact candidate and native evidence are still pending; the issue remains unverified.

## Next candidate

- Add `aarch64` while preserving the existing x86_64 recipe path.
- Install the current official FSL ARM package set through the existing FSL template, while retaining FSL 5.0.11 for x86_64.
- Select an official DSI Studio Ubuntu ARM64 release and update the AIDAmri DSI path conditionally.
- Use an ARM-capable Miniconda bootstrap or another documented ARM64 Python runtime, then let the first native build determine whether the pinned Python 3.6-era requirements resolve.

## Native investigation result — 2026-09-14

The route was attempted on native ARM64 from accepted source `4911988c7900801c10f7fce39f143d301c8a3852` through six bounded build attempts on `arm64/aidamri`. The recipe successfully replaced the x86-only FSL and DSI inputs with official ARM64 routes and reached the NiftyReg source build. The final candidate used released NiftyReg v2.0.0 for ARM, disabled its x86 SSE option, installed Git, and supplied the release metadata expected by its CMake project while preserving the original x86_64 NiftyReg route.

The final native run [34831946025](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34831946025) failed at link time in NiftyReg's bundled libpng with missing ARM NEON symbols: `png_do_expand_palette_rgba8_neon`, `png_do_expand_palette_rgb8_neon`, `png_riffle_palette_neon`, and `png_init_filter_functions_neon`. No SIF, deploy checks or fulltest ran. The exact attempt history and blocker are recorded in [issue #119](https://github.com/Vbitz/neurocontainers-arm64/issues/119#issuecomment-5662474867).

**Disposition: blocked-upstream.** Revisit only with an upstream NiftyReg/libpng ARM64 fix or a documented supported system-libpng ARM64 configuration. Do not maintain a recipe-local patch to the embedded third-party library.

## New investigation window — 2026-09-15

NiftyReg v2.0.0's released CMake configuration explicitly searches for system
zlib and libpng before selecting its bundled copies. That is the documented
configuration route named in the blocker, so the AIDAmri change was replayed
onto the current accepted pin `7bf9e3a1ea7846fde48b8c226dc280321c9d15b3` as
candidate `bd5aa3c544bec99dc83b1641fb174b6e27c43a42` on
`arm64/aidamri-system-libpng`. The ARM64 path adds Ubuntu `libpng-dev` and
leaves the x86_64 path unchanged. Validation and both architecture Dockerfile
generations pass.

This is a fresh bounded recipe investigation window authorized by the active
porting goal. The candidate is ready for one native ARM64 build. Stop if the
system library is not selected or if the next error requires patching NiftyReg
or its embedded dependencies.

The exact candidate was dispatched as native ARM64 run
[34923542636](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34923542636),
attempt 1 in this fresh window. The dispatch and hypothesis are recorded in
[issue #119](https://github.com/Vbitz/neurocontainers-arm64/issues/119#issuecomment-5674047922).

Run 34923542636 installed `libpng-dev`, but NiftyReg selected FSL's
`/opt/fsl-5.0.11/bin/cc` wrapper. Its CMake could not find the system zlib or
libpng and rebuilt the bundled libpng, reproducing the missing ARM NEON symbols
at link time. Candidate `1a06fd6f8b785d152df9a79fed0d25102926fe4f` keeps the
system library change and explicitly selects `/usr/bin/gcc` and `/usr/bin/g++`
for the ARM64 NiftyReg CMake invocation. Validation and both architecture
Dockerfile generations pass. This is attempt 2/6; dispatch it as the final
compiler-selection hypothesis before classifying the dependency blocker.

The exact retry is dispatched as native ARM64 run
[34924143185](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34924143185).
The dispatch details are recorded in [issue #119](https://github.com/Vbitz/neurocontainers-arm64/issues/119#issuecomment-5674109825).

Run 34924143185 built the ARM64 image, converted it to SIF and passed deploy
checks. The fulltest reached 6/8 checks: all NiftyReg, FSL, AIDAmri startup,
asset and path checks passed. The Python import failed because pip selected
Traits 7.1.0, which removed `TraitDictObject` required by Nipype 1.7.0. The
DSI Studio executable returned `DSI Studio (doi:...)` rather than the x86-only
`DSI Studio version:` prefix. Candidate `04970417e995232706f4ce85ddf4db23c79d4f25`
pins ARM64 Traits 6.4.3 and updates that assertion to the stable shared output
prefix. Validation and both architecture Dockerfile generations pass. This is
attempt 3/6; the recipe remains within the bounded window.

The exact candidate is dispatched as native ARM64 run
[34925938740](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34925938740).
The dispatch details are recorded in [issue #119](https://github.com/Vbitz/neurocontainers-arm64/issues/119#issuecomment-5674387518).

## Verified implementation — 2026-09-15

Candidate `04970417e995232706f4ce85ddf4db23c79d4f25` passed exact native ARM64
run [34925938740](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34925938740):
Docker build, architecture verification, SIF conversion, deploy checks and all
**9/9 fulltests** passed with zero failures and zero skips. The candidate uses
the documented NiftyReg system-library route with native GCC/G++, pins ARM64
Traits 6.4.3 for Nipype 1.7.0, and preserves the x86_64 route. The durable
verified outcome is recorded in [issue #119](https://github.com/Vbitz/neurocontainers-arm64/issues/119#issuecomment-5674555318).

The fresh window used three substantive attempts: system libpng discovery,
compiler selection, and the runtime dependency/test corrections. The candidate
is ready for serial integration onto accepted pin `7bf9e3a1ea7846fde48b8c226dc280321c9d15b3`.
