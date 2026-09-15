# tinyrange: ARM64 research plan

Researched: 2026-09-15. Recipe version: `0.4.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The recipe declares ARM64 and its image can be generated, but the complete fulltest requires a guest QEMU runtime. The ARM64 workflow explicitly prohibits QEMU or emulation as evidence of native ARM64 functionality, and omitting that test would leave an essential declared capability unverified.

## Pinned recipe and evidence

- [Recipe at accepted source `04970417e995`](https://github.com/Vbitz/neurocontainers/blob/04970417e995232706f4ce85ddf4db23c79d4f25/recipes/tinyrange/build.yaml).
- [TinyRange upstream](https://github.com/tinyrange-org/tinyrange).
- [Fulltest prerequisite issue #53](https://github.com/Vbitz/neurocontainers-arm64/issues/53).

## Blocker and revisit condition

The essential `Native QEMU runtime` test executes `/opt/tinyrange/tinyqemu/qemu-system-$(uname -m)`. That guest-emulation capability cannot be used as proof of this native ARM64 container under the workflow rules. No recipe edit can convert that required test into native functionality without changing the declared scope.

Revisit when TinyRange supplies a meaningful native ARM64 test that does not rely on emulation, or the recipe's required capability changes upstream. Do not dispatch an ARM64 candidate solely to skip this essential test.
