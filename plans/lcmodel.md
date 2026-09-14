# lcmodel: ARM64 research plan

Researched: 2026-09-13. Recipe version: `6.3.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The author's site publishes Fortran source and a Linux sample Makefile. The current recipe selects an x86 binary bundle, but LCModel is not binary-only. Compiler compatibility, exact source/binary version matching and the ancillary LCMgui tools need checking.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/lcmodel/build.yaml).
- Base image expression: `ubuntu:16.04`.
- Declared download inputs: `lcm_64_tar`, `basis_3t_zip`, `basis_1_5t_zip`, `basis_7t_zip`, `basis_9_4t_zip`, `basisset_lcmodel_zip`, `mrs_basis_sets_zip`, `testdata_rar`, `manual_pdf`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/205). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [schorschinho/LCModel upstream documentation](https://github.com/schorschinho/LCModel/blob/main/README.md).
- [mr-science-lab/mrs-basis-sets upstream documentation](https://github.com/mr-science-lab/mrs-basis-sets/blob/main/README.md).
- [Author source download and Linux Makefile links](https://lcmodel.com/lcmodel.shtml).

## Plan and acceptance criteria

Pin the author's source archive and build using the documented Linux route, auditing date/time intrinsics and all bundled helper executables. Preserve basis sets and GUI behavior. Validate fitted concentrations/residuals against existing spectral fixtures rather than only checking program startup.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/lcmodel/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-13

The bounded source audit established a concrete blocker before dispatch. The
official `source.zip` and the public `schorschinho/LCModel` repository contain
only the core `LCModel.f` program and include files. The upstream README
explicitly states that the other LCModel tools are unavailable. The current
recipe and fulltest require `lcmodel`, `makebasis`, `plotraw`, `kecc`, `lcmgui`,
and the associated scripts. Those ancillary executables are present only in
the x86 vendor payload, so building the public core would leave the ARM64
recipe incomplete and would require weakening essential tests. Issue
[#205](https://github.com/Vbitz/neurocontainers-arm64/issues/205) records this
as `blocked-prerequisite`; no candidate or native run was created.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/205#issuecomment-5652802570).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
