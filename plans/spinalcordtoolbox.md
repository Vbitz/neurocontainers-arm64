# spinalcordtoolbox: ARM64 research plan

Researched: 2026-09-13. Recipe version: `7.3.3`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

The previous native attempt stopped during PyQt5 source metadata generation with exit 143. This is not an unsupported-instruction error. PyQt5 5.15.11 is available as a Conda ARM package, but SCT's exact bundled Qt/Python pins and other native binaries remain constraints.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/spinalcordtoolbox/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `downloaded_tar_file`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/74). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699323574); use the issue for exact candidate SHA and failure context.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699607997); use the issue for exact candidate SHA and failure context.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [spinalcordtoolbox/spinalcordtoolbox upstream documentation](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/README.rst).
- [spinalcordtoolbox/spinalcordtoolbox Dockerfile](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/Dockerfile).
- [spinalcordtoolbox/spinalcordtoolbox requirements.txt](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/requirements.txt).
- [spinalcordtoolbox/spinalcordtoolbox setup.py](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/setup.py).
- [spinalcordtoolbox/spinalcordtoolbox release 7.3](https://github.com/spinalcordtoolbox/spinalcordtoolbox/releases/tag/7.3).
- [Conda-forge native Qt package metadata](https://api.anaconda.org/package/conda-forge/pyqt).

## Plan and acceptance criteria

Inspect the pinned installer and dependency freeze for a documented native Qt route; use an applicable upstream configuration fix before retrying. Preserve SCT segmentation, registration and viewer functionality, and record runtime scientific results rather than treating installer completion as success.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/spinalcordtoolbox/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Keep the recorded failure as the current blocker for that candidate. A released upstream fix or documented configuration addressing its first error is the condition for a justified retry. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5646623032).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Changed ARM dependency route — 2026-09-15

Conda-forge now publishes native `linux-aarch64` `pyqt=5.15.11` for Python 3.10. Candidate `b9043a1d` on `arm64/spinalcordtoolbox-conda-pyqt`, based on accepted pin `41ddfbf5010657e0185ab1d7730b42149e8fb744`, keeps the ARM Miniforge selection and installs that package in SCT's Conda environment. It removes only the three PyQt entries from the ARM copy of `requirements-freeze.txt`, preventing pip from selecting the source distribution that caused the prior exit-143 failure; x86_64 remains unchanged.

Recipe validation and both architecture Dockerfile generations pass. Follow-up run [34856371358](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34856371358) confirmed the PyQt route through successful ARM64 SCT installation and failed only on a GitHub 504 for the `sc_epi` model archive. The one permitted unchanged retry, [34857273165](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34857273165), failed on a GitHub 504 for the ARM64 Miniforge installer. No SIF, deploy or fulltest ran. SCT is recorded **blocked-infrastructure** in [issue #74](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5665830191); revisit only when those endpoints are reachable or stable mirrors are provided, with a fresh bounded investigation if needed.

## Changed-infrastructure follow-up — 2026-09-14

A direct preflight at `2026-09-14T18:52:28Z` returned HTTP 200 and `application/octet-stream` for the exact ARM64 Miniforge installer and previously failing `sc_epi` model archive, as well as HTTP 200 for the SCT 7.3 source tarball. This changes the prior data-service condition that stopped the native route before SIF/fulltest. The existing Conda PyQt candidate `b9043a1dd3c3a48fce336f1ba390806cfd97ff45` was reopened as attempt 5/6 in a fresh 12-hour window and dispatched on the native ARM64 workflow as [run 34883583223](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34883583223). The issue checkpoint is [#74](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5669052021), with the exact dispatch recorded [here](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5669058290).

Require the full ARM64 Docker build, SIF conversion, deploy checks and complete existing fulltest before considering the route verified. If it passes, rebase the candidate onto current accepted pin `2ad9c2ff6c9762868c99ebbe3ac59b7f895cfc51`, regenerate and retest serially before integration.

## Attempt 5 result and final configuration retry — 2026-09-14

Run [34883583223](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34883583223) confirmed that the changed data endpoints were reachable: the ARM64 Miniforge environment, native Conda PyQt and all declared models installed. The build then failed at SCT's existing `sct_check_dependencies` gate because the ARM64 CPU Torch 2.2.2 wheel reports `torch.__version__ == 2.2.2` without the `+cpu` marker; SCT 7.3 therefore classifies it as GPU and invokes `nvidia-smi`. The first actionable error was `FileNotFoundError: GPU version of torch is installed, but could not find NVIDIA's GPU software: 'nvidia-smi'`.

The official PyTorch CPU index now publishes matching Python 3.10 Linux aarch64 wheels with the required marker: `torch==2.10.0+cpu` and `torchvision==0.25.0+cpu`. Candidate `4be33834e3786c05629d4aeb2920e09d5ebd27e8` replaces SCT's ARM-only `torch<2.3` selector with that pair. Recipe validation and both architecture generations passed, and the final allowed attempt is dispatched as [run 34884606432](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34884606432); issue checkpoints are [attempt 5](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5669168070) and [final dispatch](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5669189172).

This is attempt 6/6 in the fresh window `2026-09-14T18:52:28Z`–`2026-09-15T06:52:28Z`. Require native Docker build, SIF conversion, deploy checks and complete fulltest. If this released framework upgrade is incompatible with SCT 7.3, record that upstream compatibility blocker and stop.

## Bounded terminal outcome — 2026-09-15

The final candidate [4be33834e3786c05629d4aeb2920e09d5ebd27e8](https://github.com/Vbitz/neurocontainers/commit/4be33834e3786c05629d4aeb2920e09d5ebd27e8) passed the changed Torch check in native run [34884606432](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34884606432): SCT reported `2.10.0+cpu`, so the prior false GPU classification was resolved. The existing SCT dependency gate then found the actual upstream binary blocker. The downloaded `binaries_linux` bundle contains x86 executables; `isct_antsRegistration` and `isct_propseg` both fail with `Exec format error` on ARM64. The same check reports PyQt5 import and C++ ABI errors from the bundled Qt libraries.

This is attempt 6/6 in the fresh window and no SIF or fulltest ran. The terminal outcome is **blocked-upstream**, recorded in [issue #74](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5669320254). Revisit when SCT publishes an ARM64 Linux binary bundle plus a supported ARM64 Qt/Conda combination, or documents a supported source build for those native components. Both candidates remain pushed; no further unchanged SCT attempt is justified.
