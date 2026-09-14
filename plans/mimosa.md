# mimosa: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5.8`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

MIMoSA is R source with documented GitHub/Neuroconductor installation. The recipe compiles ANTsRCore/ANTsR and adds FSL; that dependency chain needs ARM validation but is not intrinsically a private library port. No specific ARM compiler error is recorded for this recipe.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mimosa/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `fsl 6.0.7.16`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/212). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [avalcarcel9/mimosa upstream documentation](https://github.com/avalcarcel9/mimosa/blob/master/README.md).
- [avalcarcel9/mimosa Dockerfile](https://github.com/avalcarcel9/mimosa/blob/master/Dockerfile).
- [ANTsX/ANTsRCore upstream documentation](https://github.com/ANTsX/ANTsRCore/blob/master/README.md).
- [ANTsX/ANTsRCore release v0.8.0](https://github.com/ANTsX/ANTsRCore/releases/tag/v0.8.0).

## Plan and acceptance criteria

Pin and build the R/ITK dependencies using upstream procedures and resolve the required FSL tools. Test preprocessing and lesion probabilities with fixed model parameters. Stop at an actionable unsupported dependency, not at the fact that C++ compilation is needed.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mimosa/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

- The ARM FSL version correction in candidate `1f1fa6ea2942b55d1c3ec01e615d38c2b777babc` reached the native ANTsRCore build. It failed at the final shared-library link with `too many GOT entries for -fpic`; the compiler explicitly requested recompilation with `-fPIC`. No runtime image was produced. Exact run: [34770095073](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770095073).
- Candidate `c58b71e8e7400e0beb6026201b323c5d7aa3916d` changes the ARM R Makevars entries from the small `-fpic` model to the large `-fPIC` model, preserving the package set and all existing source compatibility fixes. Local validation and ARM64/x86_64 generation pass.
- Exact retry [34773252089](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773252089) is queued/in progress as attempt 3/6. If the link succeeds, continue through the existing build and fulltest; if a subsequent ANTsR source error appears, classify that dependency under the investigation budget.

The prior successful tree was replayed onto the current accepted pin `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc` as integrated candidate `5341ef2ec334b3d82589af78a2e17cfc5dd63a80` on `arm64/mimosa-bids-integrated-v2`. Both required commits are present: the ARM64 declaration/FSL 6.0.7.22 selection and the large `-fPIC` linker fix. Local validation and ARM64/x86_64 generation pass. Its exact integration dispatch is [run 34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112), counted as attempt 4/6; acceptance depends on this exact integrated SHA.

Because TopoFit advanced the accepted pin to `88e6776aeb27f16ef43e015acb426b7e87fe0d1c`, the same two intended MIMoSA commits were replayed as candidate [`6940147e3090cf6729d769c574614740e9bfc522`](https://github.com/Vbitz/neurocontainers/commit/6940147e3090cf6729d769c574614740e9bfc522) on [`arm64/mimosa-topofit`](https://github.com/Vbitz/neurocontainers/tree/arm64/mimosa-topofit). Validation and ARM64/x86_64 Dockerfile generation passed. If the current older-base run passes, dispatch this exact integrated SHA for required current-pin verification before acceptance; otherwise use it as the base for a targeted fix.

## Implementation outcome — 2026-09-14

The older-base candidate passed native ARM64 build, SIF conversion, deploy checks and all 21 fulltests in [run 34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112). The same intended commits were replayed onto accepted pin `88e6776a` as `6940147e3090cf6729d769c574614740e9bfc522`. Exact current-pin verification is dispatched in [run 34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), attempt 5/6; acceptance remains pending its complete native result.

After PALS advanced the accepted pin to `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`, the two MIMoSA commits were replayed as candidate [`8aff06bb67d3aa099cb7fdfb0617d33f361508e7`](https://github.com/Vbitz/neurocontainers/commit/8aff06bb67d3aa099cb7fdfb0617d33f361508e7) on [`arm64/mimosa-pals`](https://github.com/Vbitz/neurocontainers/tree/arm64/mimosa-pals). Validation and both architecture generations pass. Dispatch this exact descendant after the active current-pin run is reviewed, if another accepted pin has not superseded it.

After SoopCT advanced the accepted pin to `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5`, the two MIMoSA commits were replayed as candidate `e0271a0cddcf0b1108c63df5d201099aca59f301` on `arm64/mimosa-soopct`. Validation and ARM64/x86_64 Dockerfile generation passed. The active run `34783066918` remains the prior-pin verification; dispatch this exact descendant after reviewing it.

The TopoFit-based candidate passed [run 34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918) with 20/20 native fulltests and no skips. After QuPath advanced the accepted pin to `c98a89ee6799cd32b6a2247554cf8447a37f24aa`, the same two intended commits were replayed as candidate `2c0198a5` on `arm64/mimosa-qupath`. The branch is pushed; validation and ARM64/x86_64 Dockerfile generation pass. Dispatch this exact current-pin descendant for acceptance verification.

Exact candidate `2c0198a51f419c07267b00ea34f408f29e7e59f5` is dispatched in native ARM64 [run 34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497). Acceptance requires this exact QuPath descendant to pass build, SIF, deploy and all fulltests.

## Current-pin integration candidate — 2026-09-14

After CLEARSWI advanced the accepted submodule pin to `b878ef4914bed658c8df82cf8d418de21d13315f`, the two MIMoSA ARM64 commits from the QuPath candidate were replayed onto that accepted pin on [`arm64/mimosa-clearswi`](https://github.com/Vbitz/neurocontainers/tree/arm64/mimosa-clearswi). Candidate [`84cfd4ab2128d5598d3df71685e4d26de46a8fb4`](https://github.com/Vbitz/neurocontainers/commit/84cfd4ab2128d5598d3df71685e4d26de46a8fb4) passes recipe validation and ARM64/x86_64 Dockerfile generation. The exact candidate is staged for dispatch after the current QuPath-based native run [34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497) completes; do not accept the older-base result directly.

The QuPath-based candidate `2c0198a51f419c07267b00ea34f408f29e7e59f5` passed the native ARM64 gates in [run 34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497): Docker/SIF/deploy succeeded and the fulltest passed 21/21 with no skips. Because that evidence predates the accepted CLEARSWI pin, the exact current-pin replay `84cfd4ab2128d5598d3df71685e4d26de46a8fb4` is dispatched in [run 34792042542](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34792042542). Acceptance remains pending that exact run.

## Replay after Syncro acceptance — 2026-09-14

Syncro advanced the accepted pin to `54a83518034d8b164ec8290c09a2ee91e42a9996`. The two MIMoSA ARM64 commits were replayed onto that exact pin as candidate [`6743ded6ddadc9d5173d2d77a6cc199363ec4f52`](https://github.com/Vbitz/neurocontainers/commit/6743ded6ddadc9d5173d2d77a6cc199363ec4f52) on [`arm64/mimosa-syncro`](https://github.com/Vbitz/neurocontainers/tree/arm64/mimosa-syncro). Recipe validation and ARM64/x86_64 generation pass. The b878-based verification [34792042542](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34792042542) remains active; dispatch the exact `6743ded6` candidate only after that same-recipe run completes.

## Replay after Syncro acceptance — 2026-09-14

The prior-pin replay `84cfd4ab2128d5598d3df71685e4d26de46a8fb4` completed native ARM64 Docker build, SIF conversion, deploy checks and 21/21 fulltests with no skips in [run 34792042542](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34792042542).

The two intended MIMoSA commits were replayed onto accepted Syncro pin `54a83518034d8b164ec8290c09a2ee91e42a9996` as candidate [`6743ded6ddadc9d5173d2d77a6cc199363ec4f52`](https://github.com/Vbitz/neurocontainers/commit/6743ded6ddadc9d5173d2d77a6cc199363ec4f52) on [`arm64/mimosa-syncro`](https://github.com/Vbitz/neurocontainers/tree/arm64/mimosa-syncro). Local validation and ARM64/x86_64 generation pass. The exact current-pin replay is dispatched in [run 34797053207](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34797053207), attempt 2/6; acceptance requires its complete native gates.

## Replay after VesselBoost acceptance — 2026-09-14

The Syncro-based replay [34797053207](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34797053207) completed native ARM64 Docker build, SIF conversion, deploy checks and 21/21 fulltests with no skips. The two intended MIMoSA commits were replayed onto the accepted VesselBoost pin `863c447457d817156882b12a6920fd3411f68543` as candidate [`df8a470aa8f1d5c45ffe2ac43fe39193a11e05d1`](https://github.com/Vbitz/neurocontainers/commit/df8a470aa8f1d5c45ffe2ac43fe39193a11e05d1) on [`arm64/mimosa-vesselboost`](https://github.com/Vbitz/neurocontainers/tree/arm64/mimosa-vesselboost). Recipe validation and ARM64/x86_64 generation pass. The exact candidate is dispatched in [run 34802537055](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34802537055), attempt 3/6; acceptance requires its complete native gates.
