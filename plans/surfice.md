# surfice: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.20210730`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Surf Ice explicitly documents Linux source compilation with Lazarus/FreePascal. The recipe's amd64 libqt5pas package and binary archive are distribution choices. Native QtPas and rendering compatibility need testing, but no fundamental source limitation is established.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/surfice/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `surfice_linux_zip`, `libqt5pas1_2_9_0_amd64_deb`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/168). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [neurolabusc/surf-ice upstream documentation](https://github.com/neurolabusc/surf-ice/blob/master/README.md).
- [neurolabusc/surf-ice release v1.0.20211006](https://github.com/neurolabusc/surf-ice/releases/tag/v1.0.20211006).
- [davidbannon/libqt5pas upstream documentation](https://github.com/davidbannon/libqt5pas/blob/master/README.md).
- [davidbannon/libqt5pas release v1.2.16](https://github.com/davidbannon/libqt5pas/releases/tag/v1.2.16).

## Plan and acceptance criteria

Build the pinned source and its native Qt/Python bridge dependencies using documented settings. Test mesh loading, Python scripting and image export, preserving the OpenGL functionality covered by the existing suite.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/surfice/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
