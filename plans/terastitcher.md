# terastitcher: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.11.10`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

TeraStitcher publishes C++ source. The recipe's mirrored portable Linux archive is a prebuilt distribution, not evidence that source is unavailable. The exact 1.11.10 source correspondence and TIFF/image-I/O/GUI build requirements need checking.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/terastitcher/build.yaml).
- Base image expression: `fedora:35`.
- Declared download inputs: `TeraStitcher_portable_1_11_10_Linux_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/170). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [abria/TeraStitcher upstream documentation](https://github.com/abria/TeraStitcher/blob/master/README.md).
- [abria/TeraStitcher release v1.10.12](https://github.com/abria/TeraStitcher/releases/tag/v1.10.12).

## Plan and acceptance criteria

Map the archive to an upstream source revision and build native command-line and GUI tools with the same modules. Validate a small tiled-image stitching job, checking merged geometry and pixel output; do not replace its stitching algorithm.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/terastitcher/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `77b1ebe055243e309f5d5cbc0e7be279b72e9251` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **5/5** fulltests in [run 34754970340](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754970340). The ARM route builds the C++ source and enables the required utility target while preserving the x86_64 portable archive.
