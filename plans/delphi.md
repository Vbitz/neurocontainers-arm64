# delphi: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.2.post1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The pinned Delphi research stack requires legacy TensorFlow 1.15, Ray 0.8.4 and a Rust nightly/C++ toolchain. PyPI provides no Linux ARM TensorFlow 1.15 wheel. Public source exists, but replacing the framework or porting cryptographic native kernels exceeds a small recipe adjustment.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/delphi/build.yaml).
- Base image expression: `docker.io/tensorflow/tensorflow:1.15.0-gpu-py3`.
- Declared download inputs: `cuda_keyring`, `cmake_3_22_2_linux_x86_64_tar_gz`, `rustup_init`, `libtorch`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/137). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `tensorflow-1.15.0`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [yexincheng/delphi upstream documentation](https://github.com/yexincheng/delphi/blob/master/README.md).
- [mc2-project/delphi upstream documentation](https://github.com/mc2-project/delphi/blob/master/README.md).
- [tensorflow-1.15.0 published package metadata](https://pypi.org/pypi/tensorflow/1.15.0/json).

## Plan and acceptance criteria

Inspect the pinned Rust/C++ architecture requirements and upstream released compatibility fixes. Revisit with an upstream-supported ARM dependency set; preserve both cryptographic protocol behavior and inference accuracy. Do not treat a newer TensorFlow version as a drop-in fix.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/delphi/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/137#issuecomment-5651346525).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
