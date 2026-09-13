# nipype: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.8.5.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

Nipype itself is Python source. This recipe additionally installs MATLAB Runtime glnxa64 and an amd64 Go toolchain for Singularity. Go can be replaced with an ARM build, but that does not supply the compiled MATLAB functionality promised by this environment.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/nipype/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `matlabmcr 2019b`, `miniconda py39_24.7.1-0`.
- Declared download inputs: `go1_19_linux_amd64_tar_gz`, `singularity_ce_3_10_2_tar_gz`, `download`, `spm12_r7771_Linux_R2019b_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/159). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [nipy/nipype upstream documentation](https://github.com/nipy/nipype/blob/master/README.rst).
- [nipy/nipype pyproject.toml](https://github.com/nipy/nipype/blob/master/pyproject.toml).
- [nipy/nipype release 1.11.0](https://github.com/nipy/nipype/releases/tag/1.11.0).
- [sylabs/singularity upstream documentation](https://github.com/sylabs/singularity/blob/main/README.md).
- [sylabs/singularity release v4.5.1](https://github.com/sylabs/singularity/releases/tag/v4.5.1).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Map the included MATLAB interfaces and required standalone tools, retaining their runtime blocker for full support. Build native Go/Singularity and Python dependencies separately. Validate workflow execution through the actual external tools, not only Nipype imports.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/nipype/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
