# neurodesktop-lite: ARM64 research plan

Researched: 2026-09-15. Recipe version: `20260428.post2`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

The native build reached the desktop image setup and failed in the pinned JupyterLab Slurm extension's frontend metadata generation. This is a released extension/JupyterLab compatibility failure, not evidence that the desktop base or all listed tools are unportable to ARM64.

## Pinned recipe and evidence

- [Recipe at accepted source `04970417e995`](https://github.com/Vbitz/neurocontainers/blob/04970417e995232706f4ce85ddf4db23c79d4f25/recipes/neurodesktop-lite/build.yaml).
- [JupyterLab upstream](https://github.com/jupyterlab/jupyterlab) and [jupyterlab-slurm source](https://github.com/NERSC/jupyterlab-slurm).
- Native build [run 34691454730](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691454730).

## Blocker and revisit condition

The pinned `jupyterlab-slurm` source at `c34354f0aaa1b12f6243224bed631cf07c858409` cannot resolve `@jupyterlab/core-meta` for the requested `4.0.x` version; the fallback GitHub lookup was rate limited. Docker build stopped before SIF, deploy checks and fulltest. Revisit with a released compatible jupyterlab-slurm/JupyterLab combination or a direct upstream packaging fix. Do not retry the unchanged extension source or substitute a different desktop application.
