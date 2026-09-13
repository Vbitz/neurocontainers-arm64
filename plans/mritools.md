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
