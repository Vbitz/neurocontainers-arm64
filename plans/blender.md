# blender: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.0.1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Blender is open source with an extensive CMake build; choosing a linux-x64 archive in this recipe does not prove it cannot run on ARM64. The pinned release's full graphics, rendering and bundled-library configuration needs an ARM build.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/blender/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `blender_archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/122). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [blender/blender upstream documentation](https://github.com/blender/blender/blob/main/.github/README.md).
- [blender/blender CMakeLists.txt](https://github.com/blender/blender/blob/main/CMakeLists.txt).
- [blender/blender pyproject.toml](https://github.com/blender/blender/blob/main/pyproject.toml).

## Plan and acceptance criteria

Follow Blender's release-matched Linux build instructions, select supported generic CPU settings, and audit optional render backends. Preserve features covered by the recipe; test a headless rendered scene and normal GUI operation with the resulting binary.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/blender/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

- Candidate `55c2ae1a3c41a5c61da9f3763a63c5f091646819` reached the native ARM64
  Blender dependency build, but the runner timed out while downloading GMP
  6.3.0 from `gmplib.org`; no compiler or application failure was observed.
  The failure is recorded in [run 34763788910](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763788910).
- One unchanged retry is allowed for this transient download failure. The
  candidate commits were replayed onto accepted pin `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db` as
  `ad9ee486bb7898bdb2fa9e0265a876a7c5c16288` on `arm64/blender-integrated`.
  Local validation and ARM64/x86_64 generation pass. Dispatch is pending a
  runner slot; do not start another Blender attempt if this retry fails for a
  persistent data or build reason.

## Implementation outcome — 2026-09-14 (continued)

- The permitted unchanged retry `34773488949` reached Blender's native
  dependency configure but failed on a missing ARM64 ALSA development library,
  not on the earlier GMP download. CMake reported `Failed to enabled required
  ALSA backend` with `ALSA_LIBRARY` and `ALSA_INCLUDE_DIR` missing.
- Candidate `42b81983` adds the documented Ubuntu `libasound2-dev` package to
  the ARM dependency set. Recipe validation and ARM64/x86_64 generation pass.
  The exact candidate is dispatched as
  [run 34774135689](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774135689),
  attempt 3/6. If this exposes another recipe-level dependency, it remains
  within the bounded investigation; stop on a deep upstream build failure.

## Implementation outcome — bounded investigation checkpoint — 2026-09-14

- Run [34774135689](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774135689) reached the bundled Flex configure stage and failed because `autopoint` was absent: `Can't exec "autopoint"` followed by `autoreconf: error: autopoint failed`. This is an ordinary recipe dependency omission, but it was the sixth native build attempt when counting the earlier source candidates and the permitted GMP retry.
- Candidate `171bd9b6c54a199718a24f064f5a2809df1fa6d` on `arm64/blender-integrated` adds Ubuntu `autopoint`, passes recipe validation and both architecture generations, and is pushed for a future authorized investigation window. It was not dispatched because the per-recipe six-attempt and twelve-hour limits are exhausted. A separate accidental dispatch with a mistyped ref was canceled before checkout and produced no evidence.
- Concrete revisit condition: a new authorized investigation window or changed build environment permits testing the prepared `autopoint` candidate. Preserve the branch and do not claim Blender ARM64 support until an exact native candidate passes all gates.

## New authorized investigation window — 2026-09-14

The user explicitly requested implementation of all feasible plans, reopening this concrete prepared recipe-level candidate after the prior six-attempt budget ended. The full ARM64 source-build candidate was replayed onto accepted pin `b878ef4914bed658c8df82cf8d418de21d13315f` on [`arm64/blender-clearswi`](https://github.com/Vbitz/neurocontainers/tree/arm64/blender-clearswi). Candidate [`9a08a7f8ee6118f10df406be8ce75f20c2188cce`](https://github.com/Vbitz/neurocontainers/commit/9a08a7f8ee6118f10df406be8ce75f20c2188cce) adds the missing `autopoint` package to the existing documented ARM64 dependency route. Validation and ARM64/x86_64 generation pass.

This new window started `2026-09-14T00:26:26Z` and ends `2026-09-14T12:26:26Z`, attempt 1/6. The exact candidate is dispatched in [run 34792723996](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34792723996). Stop on a deep upstream build failure or another concrete blocker.

Attempt 1 in the reopened window failed before compilation because the Blender dependency bootstrap timed out downloading GMP 6.3.0 from gmplib.org. GNU's official FTP archive lists the same release, so candidate [`f55f8d643b6ed36f33fef280439a385486ea5a8d`](https://github.com/Vbitz/neurocontainers/commit/f55f8d643b6ed36f33fef280439a385486ea5a8d) pre-seeds that official archive into the dependency package directory with its verified SHA-256. Validation and both architecture generations pass. The exact targeted retry is dispatched in [run 34793445214](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34793445214), attempt 2/6.

Attempt 2 failed in the preseed command because the dependency package directory did not yet exist. Candidate [`0d2d3c1a0d29454ab70300a63f86cae8842081ce`](https://github.com/Vbitz/neurocontainers/commit/0d2d3c1a0d29454ab70300a63f86cae8842081ce) creates it before copying the official GNU GMP archive. Validation and both architecture generations pass. The exact retry is dispatched in [run 34793655215](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34793655215), attempt 3/6.

The GMP preseed allowed Blender to reach native Flex compilation, where attempt 3 failed because `makeinfo` was absent during Flex's documentation install. Candidate [`1df5eaae87cb2c51f4110d2ae448cb26b5872203`](https://github.com/Vbitz/neurocontainers/commit/1df5eaae87cb2c51f4110d2ae448cb26b5872203) adds Ubuntu `texinfo`, passes validation and both architecture generations, and is dispatched in [run 34794572307](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34794572307), attempt 4/6.
