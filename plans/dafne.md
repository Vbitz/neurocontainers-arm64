# dafne: ARM64 research plan

Researched: 2026-09-15. Recipe version: `1.8a4.post2`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

The recipe already has an ARM64 dependency path and the native image builds. The remaining failure is DAFNE's Qt/VTK GUI process segfaulting under Xvfb after standard runtime configuration fixes. This is runtime evidence against the current GUI stack, not evidence that DAFNE's Python or model code cannot run on ARM64.

## Pinned recipe and evidence

- [Recipe at accepted source `04970417e995`](https://github.com/Vbitz/neurocontainers/blob/04970417e995232706f4ce85ddf4db23c79d4f25/recipes/dafne/build.yaml).
- [DAFNE upstream](https://github.com/dafne-imaging/dafne) and [documentation](https://dafne.network/documentation/).
- Native follow-up [run 34876243931](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34876243931) passed 10/11 tests after adding `XDG_RUNTIME_DIR`.
- Software-rendering retry [run 34877537989](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34877537989) also passed 10/11; `timeout 25s xvfb-run -a dafne` exited 139 despite `LIBGL_ALWAYS_SOFTWARE=1`.

## Blocker and acceptance boundary

TensorFlow, SimpleITK, PyRadiomics, XCB dependency checks and runtime-state checks pass. The only failed capability is the required headless GUI startup, where the DAFNE/pyvistaqt/VTK rendering stack segfaults on native ARM64. No source build, emulation or test relaxation is justified.

Revisit when upstream DAFNE or its ARM64 Qt/VTK stack supplies a fix, or documents a supported headless ARM64 startup mode. Acceptance still requires a new native build, SIF conversion, deploy checks and all fulltests.
