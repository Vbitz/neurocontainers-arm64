# mritools: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.3.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

CompileMRI publishes a source compilation procedure and recommends Julia 1.10 because newer versions may fail. The precompiled Linux bundle is x64; Julia itself supports ARM. The bundled package versions and PackageCompiler path need validation, with the CLEARSWI sysimage failure as relevant but not conclusive evidence.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mritools/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `v`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/156). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [korbinian90/CompileMRI.jl upstream documentation](https://github.com/korbinian90/CompileMRI.jl/blob/master/README.md).
- [korbinian90/CompileMRI.jl Project.toml](https://github.com/korbinian90/CompileMRI.jl/blob/master/Project.toml).
- [korbinian90/CompileMRI.jl release v4.9.0](https://github.com/korbinian90/CompileMRI.jl/releases/tag/v4.9.0).
- [korbinian90/romeo upstream documentation](https://github.com/korbinian90/ROMEO/blob/master/README.md).
- [korbinian90/romeo release newReleases](https://github.com/korbinian90/ROMEO/releases/tag/newReleases).

## Plan and acceptance criteria

Resolve the source project/manifest corresponding to mritools 3.3.0, build with the supported Julia version and test every deployed CLI. Revisit a shared compiler failure only with an applicable documented fix; retain ROMEO/SWI/TGV scientific assertions.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mritools/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

A native ARM64 source candidate was tested from `arm64/mritools-bids` using the official Julia 1.10.10 Linux AArch64 archive and CompileMRI.jl v3.3.0. Runs [34770096752](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770096752) and [34770328188](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770328188) both reached the Julia dependency graph but failed in the released CompileMRI `deps/build.jl` bootstrap. Its generated `App` project is precompiled while dependencies are added sequentially, then `ClearswiApp` and the current `MriResearchTools` resolution are incompatible; the direct error was `Package App does not have RomeoApp in its dependencies` followed by an unsatisfiable `MriResearchTools` requirement. Disabling automatic intermediate precompile did not change the result.

**Disposition: blocked-upstream.** Revisit when CompileMRI publishes a corrected App dependency bootstrap or a released ARM64-compatible mritools source/bundle. Patching the upstream application dependency graph would exceed this recipe port.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/156#issuecomment-5654736848).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Changed upstream source follow-up — 2026-09-14

CompileMRI released v4.9.0 on 2026-09-03. Its `App/Project.toml` declares the
complete application environment up front (`ROMEO` 1.6.0, `CLEARSWI` 1.7.0,
`MriResearchTools` 3.8.0 and TGV QSM 0.5.3), replacing the sequential
dependency bootstrap that blocked the earlier ARM source candidate. The
release still publishes Linux only as x86_64, so this is a changed upstream
source route that builds the same released application with native Julia rather
than substituting a different implementation.

Candidate `ae93e24b8f6bf279397db9ff861f7dfe2126577b` on
[`arm64/mritools-v490`](https://github.com/Vbitz/neurocontainers/tree/arm64/mritools-v490)
updates the container and fulltest to 4.9.0, uses the official Julia 1.10.12
Linux AArch64 archive, and preserves the official Linux x86_64 archive for the
x86 path. Local validation and both architecture Dockerfile generations pass.
The exact native run is [34859110074](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34859110074).

The earlier mistyped-SHA dispatch [34858988330](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34858988330)
was canceled during checkout and produced no recipe evidence; it is not a
build attempt. This follow-up started at `2026-09-14T14:57:01Z` and ends at
`2026-09-15T02:57:01Z`; the two historical 3.3.0 attempts remain part of the
recipe record. Require native build, SIF, deploy checks and the complete
fulltest before accepting 4.9.0. If the released source fails again in its
dependency build, record the upstream blocker and stop this follow-up.

Run `34859110074` passed the native ARM64 image build, SIF conversion and
deploy checks and completed 53/54 fulltests. The only failure was the inherited
ROMEO version assertion expecting `3`; the 4.9.0 release correctly reports
ROMEO 1.6.0. Candidate `4f73c13762dc293190214271ed2b91b559ea3dbf` updates that
single assertion, passes local validation and both architecture generations,
and is dispatched in exact native run
[34863087923](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34863087923)
as follow-up attempt 3/6. Acceptance requires all 54 tests; the local
submodule remains restored at the accepted pin while the run executes.

## Accepted implementation — 2026-09-15

Candidate `b13364554a3f6b3e3ab99d18fbc5ee9bca2d3585` on
[`arm64/mritools-v490`](https://github.com/Vbitz/neurocontainers/tree/arm64/mritools-v490)
passed exact native run
[34866790216](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34866790216).
The ARM64 Docker build, architecture verification, SIF conversion, deploy
checks and fulltest all passed: **55 passed, 0 failed, 0 skipped**. The ARM
route builds released CompileMRI/mritools 4.9.0 from source with Julia 1.10.12;
the x86_64 route keeps the official 4.9.0 binary archive. The final fulltest
assertion records the bundled executable's observed ROMEO output, `4.9.0`.

The candidate is ready for serial integration from accepted pin
`41ddfbf5010657e0185ab1d7730b42149e8`. Evidence and the verified outcome are
recorded in [issue #156](https://github.com/Vbitz/neurocontainers-arm64/issues/156#issuecomment-5667497490).

## Integration outcome — 2026-09-15

The verified candidate was integrated serially from accepted pin
`41ddfbf5010657e0185ab1d7730b42149e8`. Root commit
`1b0ca0a` advances the top-level submodule pointer to
`b13364554a3f6b3e3ab99d18fbc5ee9bca2d3585` and is pushed on `main`.
`python3 scripts/tracking_issue.py --write` refreshed and verified coverage
issue #2. The local submodule checkout is clean at the accepted mritools
commit; the overall ARM64 goal remains active for the unresolved inventory.
