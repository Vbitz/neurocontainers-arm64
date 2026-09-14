# fastcsr: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.post3`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The recipe pins FreeSurfer 6.0 and a linux_x86_64 Nighres wheel plus legacy PyTorch. The original repository now points to pBFSLab/FastCSR. Source access exists, but native Nighres/JVM and FreeSurfer parity have not been established for this pinned pipeline.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fastcsr/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `freesurfer_tar`, `nighres_wheel`, `model_zip`, `data_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/142). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [IndiLab/FastCSR upstream documentation](https://github.com/IndiLab/FastCSR/blob/main/README.md).
- [Upstream successor source location](https://github.com/pBFSLab/FastCSR).

## Plan and acceptance criteria

Use the pinned revision and upstream build guidance for Nighres, keeping the original cortical algorithm and weights. Establish matching native FreeSurfer and Python dependencies; compare cortical surfaces and segmentation before accepting a migration.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fastcsr/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/142#issuecomment-5651347511).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Implementation disposition — 2026-09-14

Preflight confirms that the pinned recipe cannot produce an ARM64 candidate from its declared inputs. It requires the `Linux-centos6_x86_64` FreeSurfer 6.0 archive and a `cp38-cp38-linux_x86_64` Nighres wheel. These are executable native prerequisites for the FastCSR pipeline, so a declaration-only edit or a native runner would not establish a valid build. No candidate branch or duplicate build was created.

The final [issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/142#issuecomment-5651347511) records the exact URLs and the revisit condition. Revisit only when FastCSR/Nighres/FreeSurfer provides an ARM64-compatible asset, package, base image, or documented source-build route for the pinned functionality.
