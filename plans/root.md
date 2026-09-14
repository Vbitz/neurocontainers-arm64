# root: ARM64 research plan

Researched: 2026-09-13. Recipe version: `6.22.02`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

ROOT is source available with documented CMake builds, and current packaging includes explicit aarch64 configuration. The old 6.22.02-centos7 image is a packaging/legacy-toolchain problem, not proof that ROOT fundamentally cannot run on ARM.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/root/build.yaml).
- Base image expression: `rootproject/root:{{ context.version }}-centos7`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/116). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `rootproject/root:6.22.02-centos7`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [root-project/root upstream documentation](https://github.com/root-project/root/blob/master/README.md).
- [root-project/root CMakeLists.txt](https://github.com/root-project/root/blob/master/CMakeLists.txt).
- [root-project/root pyproject.toml](https://github.com/root-project/root/blob/master/pyproject.toml).
- [root-project/root requirements.txt](https://github.com/root-project/root/blob/master/requirements.txt).
- [root-project/root release v6-40-04](https://github.com/root-project/root/releases/tag/v6-40-04).
- [Registry manifest inspected](https://registry-1.docker.io/v2/rootproject/root/manifests/6.22.02-centos7).

## Plan and acceptance criteria

Evaluate the exact 6.22.02 source and bundled Cling/LLVM compatibility using official build instructions, or propose a version-aligned supported release update. Test C++ interpretation, ROOT file I/O and histogram fitting. Stop if the old compiler needs a private port.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/root/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `3bdd670d17eb6aae64902d1aed8091b2c464a79a` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **102/102** fulltests in [run 34764973586](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764973586). The ARM route uses the architecture-specific package manager path and preserves the ROOT deployment contract.
