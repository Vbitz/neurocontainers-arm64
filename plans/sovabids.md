# sovabids: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.3.1a0.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The previous blocker was the VS Code x64 download. VS Code has native ARM packages, and sovabids itself is Python source. The recipe's broader pinned BIDS/MNE environment and GUI dependencies still need an ARM solve; no fundamental blocker is established.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/sovabids/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py310_25.5.1-0`.
- Declared download inputs: `vscode_deb`, `mne_bids_pipeline_main_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/167). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [yjmantilla/sovabids upstream documentation](https://github.com/yjmantilla/sovabids/blob/main/README.rst).
- [yjmantilla/sovabids pyproject.toml](https://github.com/yjmantilla/sovabids/blob/main/pyproject.toml).
- [yjmantilla/sovabids release v0.4.7](https://github.com/yjmantilla/sovabids/releases/tag/v0.4.7).
- [yjmantilla/bidscoin upstream documentation](https://github.com/yjmantilla/bidscoin/blob/master/README.rst).
- [yjmantilla/bidscoin pyproject.toml](https://github.com/yjmantilla/bidscoin/blob/master/pyproject.toml).
- [yjmantilla/bidscoin requirements.txt](https://github.com/yjmantilla/bidscoin/blob/master/requirements.txt).
- [yjmantilla/bidscoin setup.py](https://github.com/yjmantilla/bidscoin/blob/master/setup.py).

## Plan and acceptance criteria

Select the architecture-correct editor asset and inspect the existing environment lock for native package pins. Preserve conversion and editor behavior, then test real electrophysiology-to-BIDS output and validation.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/sovabids/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-infrastructure**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/167#issuecomment-5653614496).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Final bounded investigation — 2026-09-15

- Candidate `7dc7fb657f1a8eb0fdcdd0f6c966882a928677ba` reached the ARM64 dependency route in native run [34854062915](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34854062915). The image installed Ubuntu ARM PyQt5, compiled the ARM `traits` extension with the added `build-essential`, and built and installed pinned Bidscoin without PyQt source compilation.
- The build stopped at the recipe's existing `pip check` before SIF conversion because Ubuntu's `spyder` package installs `ipykernel 6.7.0`, which requires `debugpy`, and `debugpy` was absent. No deploy checks or fulltest ran.
- Outcome: **blocked-prerequisite** after the six-attempt recipe budget. The concrete revisit condition is an ARM candidate that adds and validates the missing `debugpy` dependency, with a fresh explicit budget or changed upstream package metadata. The candidate branch remains pushed for evidence; it is not accepted into the top-level pin.

## Reopened debugpy follow-up — 2026-09-15

The user explicitly requested continued implementation after the prior
six-attempt investigation. The last native build reached `pip check` and
reported that Ubuntu's installed `ipykernel 6.7.0` from `spyder` requires
`debugpy`, which was absent from the ARM environment after the PyQt and
`traits` fixes. Candidate
`e3bbad5e59bc3037374a7f8db380f528aa25a70d` on
[`arm64/sovabids-debugpy`](https://github.com/Vbitz/neurocontainers/tree/arm64/sovabids-debugpy)
adds `debugpy` to the ARM-only dependency install. It is based on accepted
pin `b13364554a3f6b3e3ab99d18fbc5ee9bca2d3585`; x86_64 is unchanged. Local
validation and both architecture generations pass.

This fresh continuation window started at `2026-09-14T16:53:59Z` and ends at
`2026-09-15T04:53:59Z`, attempt 1/6 in the new window. The exact candidate is
being dispatched on native Linux ARM64. Acceptance still requires the full
build, SIF, deploy and test gates; a new native upstream dependency failure
will be recorded as the blocker.

Run [34871579327](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34871579327)
passed native ARM64 image build and SIF conversion, but fulltest reported
**56 passed, 40 failed, 0 skipped**. The first actionable runtime failures
were a NumPy/pandas ABI mismatch (`numpy.dtype size changed`) and SOVA's
`from numpy import mat` import failing because the ARM-only unpinned helper
install upgraded NumPy beyond the recipe's pinned 1.26.4/pandas 1.5.3 pair.

Candidate `3cd80779270718fdd6204a837d88c5588c22ee44` on
[`arm64/sovabids-debugpy`](https://github.com/Vbitz/neurocontainers/tree/arm64/sovabids-debugpy)
reapplies the existing NumPy and pandas pins in the ARM-only install after
the helper packages; x86_64 is unchanged. Local validation and both
architecture generations pass. This is attempt 2/6 in the reopened window;
the exact candidate is dispatched for native ARM64 verification.

Run [34873161511](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34873161511)
passed the exact native ARM64 Docker build, architecture verification, SIF
conversion, deploy checks and fulltest: **96 passed, 0 failed, 0 skipped**.
Candidate `3cd80779270718fdd6204a837d88c5588c22ee44` is verified and ready for
serial integration from accepted pin
`b13364554a3f6b3e3ab99d18fbc5ee9bca2d3585`. Durable evidence is recorded in
[issue #167](https://github.com/Vbitz/neurocontainers-arm64/issues/167#issuecomment-5667942216).

## Integration outcome — 2026-09-15

The verified candidate was integrated serially from accepted mritools pin
`b13364554a3f6b3e3ab99d18fbc5ee9bca2d3585`. Root commit `5c23952` advances the
top-level submodule pointer to
`3cd80779270718fdd6204a837d88c5588c22ee44` and is pushed on `main`.
`python3 scripts/tracking_issue.py --write` refreshed and verified coverage
issue #2. The local submodule checkout is clean at the accepted SOVA-BIDS
commit; the overall goal remains active for unresolved recipes.
