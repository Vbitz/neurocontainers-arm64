# ARM64 porting checkpoint

Updated: 2026-09-12 (Australia/Brisbane)

## Current state

- Top-level branch: `main`
- Top-level commit: `b81fbc5`
- Pinned submodule: `neurocontainers@87e1c7265e8b6c767cd3154c67caca984116711e`
- Submodule checkout: `main`, clean, origin `Vbitz/neurocontainers`
- Fork Actions: disabled (`enabled: false`)
- Existing verified pipeline check: `workshopdemo` / `arm64`, run [34684189569](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34684189569), 4 passed, source `87e1c726`
- Coverage snapshot: 54 of 247 recipes declare ARM64 support; the tracker is issue [#2](https://github.com/Vbitz/neurocontainers-arm64/issues/2)

## Queue

Initial verification batch, using the current accepted pin and no recipe edits:

- `dcm2niix` — source build on ARM64, focused DICOM conversion CLI tests
- `niimath` — pinned upstream source build, NIfTI math CLI tests
- `niftyreg` — declared ARM64 build, registration CLI tests
- `vina` — declared ARM64 build, command line smoke tests

After reviewing each result, refill up to four available slots with the next
eligible declared recipe, then assess practical undeclared recipes. Keep one
issue per recipe/variant and record durable evidence in comments.

## Active attempts

Initial verification started at `2026-09-12T09:09:37Z`; each recipe is on
attempt 1 with a 12-hour deadline of `2026-09-12T21:09:37Z`.

| Recipe | Baseline/source SHA | Fork branch | Run | Issue | Next action |
| --- | --- | --- | --- | --- | --- |
| `dcm2niix` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110310](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110310) | pending | wait for build/test/report |
| `niimath` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110419](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110419) | pending | wait for build/test/report |
| `niftyreg` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110299](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110299) | pending | wait for build/test/report |
| `vina` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110418](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110418) | pending | wait for build/test/report |

## Integration

- Accepted integration SHA: `87e1c7265e8b6c767cd3154c67caca984116711e`
- Top-level submodule pointer has no candidate changes.

## Next action

Validate and dispatch the four initial candidates against the exact pinned
submodule SHA, capture run IDs and issue URLs, and review completed results
before changing any recipe.
