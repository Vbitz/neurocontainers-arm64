# romeo: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.2.8`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

ROMEO.jl publishes source and a documented Julia execution path. The recipe downloads a precompiled application bundle, which needs a native equivalent. Julia ARM support makes a source/JIT route plausible; compiled app version 3.2.8 must be mapped to its actual Julia package version.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/romeo/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `romeo_linux_3_2_8_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/164). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [korbinian90/ROMEO.jl upstream documentation](https://github.com/korbinian90/ROMEO.jl/blob/master/README.md).
- [korbinian90/ROMEO.jl Project.toml](https://github.com/korbinian90/ROMEO.jl/blob/master/Project.toml).
- [korbinian90/ROMEO.jl release v1.6.0](https://github.com/korbinian90/ROMEO.jl/releases/tag/v1.6.0).
- [korbinian90/ROMEO upstream documentation](https://github.com/korbinian90/ROMEO/blob/master/README.md).
- [korbinian90/ROMEO release newReleases](https://github.com/korbinian90/ROMEO/releases/tag/newReleases).

## Plan and acceptance criteria

Recover the release project/manifest and use the same algorithm and CLI through the supported Julia source or app build. Validate phase unwrapping and coil combination, preserving output conventions and numerical checks.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/romeo/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **✅**, fulltest **❌**; plan assessment: **Plausible**.
- Investigation outcome: **failed-runtime**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5653761465).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## CompileMRI 4.9 ARM64 follow-up — 2026-09-15

The earlier ROMEO 3.2.8 source route built natively but failed at the released Julia package environment's CLI precompilation boundary. The accepted mritools 4.9.0 port then supplied changed evidence: CompileMRI v4.9.0 has a complete released project, Julia 1.10.12 has a native Linux ARM64 runtime, and the same source route passed the full ROMEO functional suite inside mritools.

Candidate `137a31db5dee0ba5f19aa8a3e642eab5234058d7` on `arm64/romeo-v490`, based on accepted source `3cd80779270718fdd6204a837d88c5588c22ee44`, updates ROMEO to CompileMRI 4.9.0. ARM64 builds the released CompileMRI source with Julia 1.10.12; x86_64 uses the matching official `mritools_linux_x64_4.9.0` asset. The existing ROMEO fulltest is preserved with its version expectation aligned to 4.9.0. Recipe validation and both architecture Dockerfile generations passed.

Exact native run: [34875388957](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34875388957). Issue [#164](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5668044487) records the follow-up hypothesis and [the dispatch checkpoint](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5668053043). Follow-up window: `2026-09-14T17:32:21Z`–`2026-09-15T05:32:21Z`. The shared checkout is restored to accepted pin `3cd80779270718fdd6204a837d88c5588c22ee44` while the run executes.

## Fulltest compatibility retry — 2026-09-15

Run `34875388957` built the native ARM64 image and passed SIF conversion, deployment and 102/104 fulltests. All functional unwrapping, pipeline, error handling and Julia checks passed. The only failures were help assertions inherited from the older recipe: CompileMRI 4.9.0 no longer prints the removed `--coil-combination` alias and now reports template default `1`.

Candidate `2ad9c2ff6c9762868c99ebbe3ac59b7f895cfc51` on `arm64/romeo-v490` updates the former alias assertion to the current `activates MCPC3Ds phase offset correction` help text and the template default assertion to `default: 1`. This preserves the coil-combination feature check and aligns the version-specific default with the tested upstream CLI. Local recipe validation and ARM64/x86_64 Dockerfile generation passed.

Issue [#164](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5668458801) records the retry hypothesis and [the exact dispatch](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5668551288). The exact candidate is queued as native ARM64 attempt 2 in [run 34878790921](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34878790921). The invalid dispatch [run 34878760802](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34878760802) was cancelled immediately and produced no recipe evidence. Acceptance still requires build, SIF, deploy and all fulltests with zero skips.

## Accepted implementation — 2026-09-15

Candidate `2ad9c2ff6c9762868c99ebbe3ac59b7f895cfc51` passed exact native ARM64 run [34878790921](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34878790921): Docker build, architecture verification, SIF conversion, deploy checks and **105/105 fulltests**, with zero failures and zero skips. The two CompileMRI 4.9.0 help expectations were aligned with the tested current CLI; all functional unwrapping, pipeline, error handling and Julia checks passed. Issue [#164](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5668857011) records the verified result.

The candidate is now the accepted submodule pin through root integration commit `32cb228`, pushed to `main`. The local checkout is clean and detached at `2ad9c2ff6c9762868c99ebbe3ac59b7f895cfc51` while remaining root documentation changes stay local.
