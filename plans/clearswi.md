# clearswi: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.6.1`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

The recorded native build installed Julia dependencies but LLVM failed with vscale selection while PackageCompiler generated a sysimage. Upstream also documents running Julia source directly. The demonstrated blocker is the compiled sysimage path, not all CLEARSWI execution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/clearswi/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `julia_linux_x86_64_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/75). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699875754); use the issue for exact candidate SHA and failure context.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [korbinian90/CLEARSWI.jl upstream documentation](https://github.com/korbinian90/CLEARSWI.jl/blob/master/README.md).
- [korbinian90/CLEARSWI.jl Project.toml](https://github.com/korbinian90/CLEARSWI.jl/blob/master/Project.toml).
- [korbinian90/CLEARSWI.jl release v1.7.0](https://github.com/korbinian90/CLEARSWI.jl/releases/tag/v1.7.0).

## Plan and acceptance criteria

Check whether the pinned version's documented Julia CLI can preserve every deployed option without a custom sysimage; otherwise require a released Julia/HostCPUFeatures fix. Retain SWI and QSM output checks and avoid copying a compiled x86 image.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/clearswi/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Keep the recorded failure as the current blocker for that candidate. A released upstream fix or documented configuration addressing its first error is the condition for a justified retry. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

A bounded ARM64 candidate is prepared on `arm64/clearswi-bids` at `cf9a122bc839f0bde01d013bdf17ef7a915541e7`. It adds the official Julia 1.12.6 Linux AArch64 archive and skips only the custom PackageCompiler sysimage step on ARM64, retaining the stock Julia sysimage and the same package installation, CLI, deploy and runtime assertions. Local validation and both architecture Dockerfile generations pass. Native run [34770539453](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770539453) is in progress.

- The first source candidate `cf9a122bc839f0bde01d013bdf17ef7a915541e7` built
  and converted successfully, and deploy checks passed. Its fulltest reached
  67/68: the only failure was the existing `CLI phase scaling types` test,
  which runs five native CLI operations and timed out at 120 seconds. The
  individual operations were otherwise passing; the timeout occurred at the
  aggregate test boundary after the preceding phase-scaling and strength tests.
- Candidate `256b2824f39066e26a632a754f271879c3c085e9` raises only that test's
  timeout to 300 seconds, preserving all commands and output assertions. Local
  validation and ARM64/x86_64 generation pass. Exact retry
  [34772631281](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34772631281)
  is queued/in progress as attempt 2/6. If it passes, replay the same one-line
  fulltest change onto the accepted integration state before accepting.

The candidate passed all 68 native tests in [run 34772631281](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34772631281). Its two intended commits were replayed onto accepted pin `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` as `21382bb0421c036c87a86e29c796cfcdeb319e35` on `arm64/clearswi-integrated-80a`. Local validation and both architecture generations pass; exact integrated verification is pending a native runner slot.

After EMUSES advanced the accepted pin to `685f5f4d9636d34aa8237646535d2a7dfc3a525d`, the same intended commits were replayed as `488f143223358f000b57fdc06b2693a89b896110` on `arm64/clearswi-integrated-emuses`. Exact native verification is [run 34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906); acceptance still requires all 68 tests on this integrated commit.
