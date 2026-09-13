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
