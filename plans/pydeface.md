# pydeface: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.2`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

PyDeface source is available and primarily requires FSL registration tools. The old inherited FSL image is the immediate barrier. Official ARM FSL packages provide a concrete path worth testing, although their version compatibility with the pinned 2.0.2 recipe must be checked.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/pydeface/build.yaml).
- Base image expression: `vnmd/fsl_6.0.3:20200905`.
- Declared download inputs: `miniconda_sh`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/161). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `vnmd/fsl_6.0.3:20200905`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [poldracklab/pydeface upstream documentation](https://github.com/poldracklab/pydeface/blob/master/README.md).
- [poldracklab/pydeface Dockerfile](https://github.com/poldracklab/pydeface/blob/master/Dockerfile).
- [poldracklab/pydeface pyproject.toml](https://github.com/poldracklab/pydeface/blob/master/pyproject.toml).
- [poldracklab/pydeface release v2.1.0](https://github.com/poldracklab/pydeface/releases/tag/v2.1.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/vnmd/fsl_6.0.3/manifests/20200905).

## Plan and acceptance criteria

Build on a native base with the same PyDeface source and compatible FSL commands, retaining templates and settings. Test actual defacing: removed facial voxels, preserved brain data and unchanged image geometry.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/pydeface/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

- Candidate `90ee2948253826e0413ca90be894f381d10009eb` on
  `arm64/pydeface-root` passed native ARM64 build, SIF conversion, deploy checks
  and **60/60 fulltests** in [run 34769469302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769469302).
  The ARM-only setuptools pin below 67.5 removes the `pkg_resources` warning
  that had hidden the version assertion.
- That candidate was based on an older accepted submodule history. Its four
  recipe commits were replayed onto accepted BIDSvue pin `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db`.
- Integrated candidate: `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` on
  `arm64/pydeface-integrated`, with validation and ARM64/x86_64 generation
  passing locally. The exact integrated native run is
  [34771433995](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34771433995),
  currently queued/in progress. Do not advance the top-level pin until this
  exact SHA passes build, SIF, deploy and fulltest.

## Accepted implementation — 2026-09-14

- Integrated candidate `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` on
  `arm64/pydeface-integrated` passed the exact native ARM64 verification in
  [run 34771433995](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34771433995).
- Docker build, architecture verification, SIF conversion, deploy checks and
  the complete fulltest suite passed: **60 passed, 0 failed, 0 skipped**.
- This candidate is ready for serial acceptance at the top-level submodule pin.

## Current native measurements — 2026-10-19

Current diagnostic source `aa6bb369db798d325e4d02b50a2200a02677cfbf` passes all
**61 scientific cases** on [native GitHub ARM](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/39220575769).
Only the deliberately failing review gate remains, so the aggregate result is
62/63 and is not a release pass. Normalized mutual information takes 179.466 seconds,
T2 154.335 seconds and mutual information 283.345 seconds, within the unchanged
300/300/600-second limits. The FLIRT executable checksum matches the slower
Blacksmith run. No whole-library byte identity or sampled-profile attribution is claimed.

The full 5,898,240-voxel registered-mask product, unchanged input, spatial geometry
and existing NIfTI storage bound remain asserted. The native runner option in
[PR #3709](https://github.com/neurodesk/neurocontainers/pull/3709) changes hardware
selection without changing scientific tests or deadlines. Final source
`c53d3b31980866f79fd3711e4e52a866f7b0569c` removes temporary diagnostics after this
review while preserving all 61 scientific mappings. It passes [62/62 fresh native checks](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/39226549671),
including all 61 fulltests and deployment, with zero failures/skips. Mutualinfo,
normmi and T2 take 268/161/140 seconds within the unchanged 600/300/300-second
limits. The existing [PR #3580](https://github.com/neurodesk/neurocontainers/pull/3580)
now tests this exact final head on both architectures in
[run 39232288136](https://github.com/neurodesk/neurocontainers/actions/runs/39232288136);
those results and every required gate remain necessary before merge.

The upstream bot subsequently merged current main into the PR, producing
`38776086a2fc4382d193ad1d3e6de69fd00fc981` and cancelling the earlier candidate jobs.
PyDeface and all shared build/test inputs remain byte-identical. Replacement
[upstream run 39233637142](https://github.com/neurodesk/neurocontainers/actions/runs/39233637142)
verifies the integrated head; C53 native evidence remains bound to its original SHA.
