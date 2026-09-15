# elastix: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.1.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

Elastix provides CMake source with ITK dependencies. The absence of an ARM release zip and the need to build ITK 5.3 are not fundamental blockers. No native failure from this exact source build is established in the prior preflight assessment.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/elastix/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `downloaded_file`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/92). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [SuperElastix/elastix upstream documentation](https://github.com/SuperElastix/elastix/blob/main/README.md).
- [SuperElastix/elastix CMakeLists.txt](https://github.com/SuperElastix/elastix/blob/main/CMakeLists.txt).
- [SuperElastix/elastix Dockerfile](https://github.com/SuperElastix/elastix/blob/main/Dockerfile).
- [SuperElastix/elastix release 5.3.1](https://github.com/SuperElastix/elastix/releases/tag/5.3.1).

## Plan and acceptance criteria

Pin the 5.1.0 source and compatible ITK configuration, then build normally on ARM. Test both elastix registration and transformix output. A specific compiler/library failure would justify stopping; merely encountering ITK would not.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/elastix/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/92#issuecomment-5653939321).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Verified implementation — 2026-09-14

Candidate `41ddfbf5010657e0185ab1d7730b42149e8fb744` on `arm64/elastix-itk547` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **33/33 fulltests** with no skips in [run 34842787062](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34842787062). The route builds official ITK v5.4.7 and pinned Elastix 5.1.0 from source. The final runtime wrappers prepend `/opt/itk/lib` and the Elastix library directory so Apptainer fulltests remain functional when the host supplies `LD_LIBRARY_PATH`. This candidate descends from accepted pin `4911988c7900801c10f7fce39f143d301c8a3852` and is ready for serial integration.
