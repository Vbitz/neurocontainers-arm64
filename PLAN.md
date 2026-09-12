# ARM64 porting checkpoint

Updated: 2026-09-12 (Australia/Brisbane)

## Current state

- Top-level branch: `main`
- Top-level commit: `52bacb0519402ed1fab606083e9ee309f5a90e0b`
- Pinned submodule: `neurocontainers@7bd4f9ee9734c4dd3a449290c39955f009f081d3`
- Submodule checkout: `arm64/globus`, clean, origin `Vbitz/neurocontainers`
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

The `bidstools`, `dicompare`, and `eharmonize` baseline runs started at
`2026-09-12T09:36:08Z`; each passed on attempt 1. Their accepted-pin rechecks
started at `2026-09-12T09:44:07Z` and use the full accepted source SHA
`7bd4f9ee9734c4dd3a449290c39955f009f081d3`.

The `afib1` current-pin verification started at `2026-09-12T09:46:06Z` on
attempt 1 with a deadline of `2026-09-12T21:46:06Z`.

| Recipe | Baseline/source SHA | Fork branch | Run | Issue | Next action |
| --- | --- | --- | --- | --- | --- |
| `dcm2niix` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110310](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110310) | [#4](https://github.com/Vbitz/neurocontainers-arm64/issues/4) | verified: 106 passed; retain as accepted pin evidence |
| `niimath` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110419](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110419) | [#6](https://github.com/Vbitz/neurocontainers-arm64/issues/6) | verified: 115 passed; retain as accepted pin evidence |
| `niftyreg` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110299](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110299) | [#10](https://github.com/Vbitz/neurocontainers-arm64/issues/10) | verified: 89 passed; retain as accepted pin evidence |
| `vina` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110418](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110418) | [#3](https://github.com/Vbitz/neurocontainers-arm64/issues/3) | verified: 8 passed; retain as accepted pin evidence |
| `dcm2bids` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685269662](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685269662) | [#5](https://github.com/Vbitz/neurocontainers-arm64/issues/5) | verified: 61 passed; retain as accepted pin evidence |
| `niistat` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685269554](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685269554) | [#7](https://github.com/Vbitz/neurocontainers-arm64/issues/7) | verified: 93 passed; retain as accepted pin evidence |
| `heudiconv` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685389090](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685389090) | [#9](https://github.com/Vbitz/neurocontainers-arm64/issues/9) | verified: 69 passed; retain as accepted pin evidence |
| `gimp` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685484205](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685484205) | [#8](https://github.com/Vbitz/neurocontainers-arm64/issues/8) | verified: 7 passed; retain as accepted pin evidence |
| `openrefine` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685556897](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685556897) | [#11](https://github.com/Vbitz/neurocontainers-arm64/issues/11) | verified: 2 passed; retain as accepted pin evidence |
| `julia` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685647289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685647289) | [#17](https://github.com/Vbitz/neurocontainers-arm64/issues/17) | verified: 137 passed; retain as accepted pin evidence |
| `apptainer` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685647267](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685647267) | [#15](https://github.com/Vbitz/neurocontainers-arm64/issues/15) | verified: 6 passed; retain as accepted pin evidence |
| `datalad` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685666449](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685666449) | [#12](https://github.com/Vbitz/neurocontainers-arm64/issues/12) | verified: 10 passed; retain as accepted pin evidence |
| `mricron` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685692303](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685692303) | [#13](https://github.com/Vbitz/neurocontainers-arm64/issues/13) | verified: 105 passed; retain as accepted pin evidence |
| `libreoffice` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685794423](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685794423) | [#16](https://github.com/Vbitz/neurocontainers-arm64/issues/16) | verified: 3 passed; retain as accepted pin evidence |
| `globus` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | `arm64/globus` | [34686096832](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686096832) | [#14](https://github.com/Vbitz/neurocontainers-arm64/issues/14) | verified; integrated into top-level pin |
| `bidstools` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | pinned accepted branch | baseline [34686282914](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686282914); accepted [34686613888](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686613888) | [#20](https://github.com/Vbitz/neurocontainers-arm64/issues/20) | verified: 12 passed |
| `dicompare` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | pinned accepted branch | baseline [34686283152](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686283152); accepted [34686615747](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686615747) | [#19](https://github.com/Vbitz/neurocontainers-arm64/issues/19) | verified: 105 passed |
| `eharmonize` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | pinned accepted branch | baseline [34686283058](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686283058); accepted [34686618053](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686618053) | [#18](https://github.com/Vbitz/neurocontainers-arm64/issues/18) | verified: 6 passed |
| `afib1` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34686701687](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686701687) | [#21](https://github.com/Vbitz/neurocontainers-arm64/issues/21) | verified: 5 passed |
| `arfiproc` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34686847933](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686847933) | pending | current-pin verification queued |
| `b0map` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34686964891](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686964891) | pending | current-pin verification queued |

## Verified results

- `dcm2niix` / `arm64`: run `34685110310`, source `87e1c726`, 106 passed, 0 failed, 0 skipped; issue [#4](https://github.com/Vbitz/neurocontainers-arm64/issues/4).
- `vina` / `arm64`: run `34685110418`, source `87e1c726`, 8 passed, 0 failed, 0 skipped; issue [#3](https://github.com/Vbitz/neurocontainers-arm64/issues/3).
- `dcm2bids` / `arm64`: run `34685269662`, source `87e1c726`, 61 passed, 0 failed, 0 skipped; issue [#5](https://github.com/Vbitz/neurocontainers-arm64/issues/5).
- `niimath` / `arm64`: run `34685110419`, source `87e1c726`, 115 passed, 0 failed, 0 skipped; issue [#6](https://github.com/Vbitz/neurocontainers-arm64/issues/6).
- `niistat` / `arm64`: run `34685269554`, source `87e1c726`, 93 passed, 0 failed, 0 skipped; issue [#7](https://github.com/Vbitz/neurocontainers-arm64/issues/7).
- `niftyreg` / `arm64`: run `34685110299`, source `87e1c726`, 89 passed, 0 failed, 0 skipped; issue [#10](https://github.com/Vbitz/neurocontainers-arm64/issues/10).
- `heudiconv` / `arm64`: run `34685389090`, source `87e1c726`, 69 passed, 0 failed, 0 skipped; issue [#9](https://github.com/Vbitz/neurocontainers-arm64/issues/9).
- `gimp` / `arm64`: run `34685484205`, source `87e1c726`, 7 passed, 0 failed, 0 skipped; issue [#8](https://github.com/Vbitz/neurocontainers-arm64/issues/8).
- `openrefine` / `arm64`: run `34685556897`, source `87e1c726`, 2 passed, 0 failed, 0 skipped; issue [#11](https://github.com/Vbitz/neurocontainers-arm64/issues/11).
- `datalad` / `arm64`: run `34685666449`, source `87e1c726`, 10 passed, 0 failed, 0 skipped; issue [#12](https://github.com/Vbitz/neurocontainers-arm64/issues/12).
- `mricron` / `arm64`: run `34685692303`, source `87e1c726`, 105 passed, 0 failed, 0 skipped; issue [#13](https://github.com/Vbitz/neurocontainers-arm64/issues/13).
- `julia` / `arm64`: run `34685647289`, source `87e1c726`, 137 passed, 0 failed, 0 skipped; issue [#17](https://github.com/Vbitz/neurocontainers-arm64/issues/17).
- `apptainer` / `arm64`: run `34685647267`, source `87e1c726`, 6 passed, 0 failed, 0 skipped; issue [#15](https://github.com/Vbitz/neurocontainers-arm64/issues/15).
- `libreoffice` / `arm64`: run `34685794423`, source `87e1c726`, 3 passed, 0 failed, 0 skipped; issue [#16](https://github.com/Vbitz/neurocontainers-arm64/issues/16).
- `globus` / `arm64`: run `34686096832`, source `7bd4f9ee`, 72 passed, 0 failed, 0 skipped; issue [#14](https://github.com/Vbitz/neurocontainers-arm64/issues/14).
- `bidstools` / `arm64`: accepted-pin run `34686613888`, source `7bd4f9ee`, 12 passed, 0 failed, 0 skipped; issue [#20](https://github.com/Vbitz/neurocontainers-arm64/issues/20).
- `dicompare` / `arm64`: accepted-pin run `34686615747`, source `7bd4f9ee`, 105 passed, 0 failed, 0 skipped; issue [#19](https://github.com/Vbitz/neurocontainers-arm64/issues/19).
- `eharmonize` / `arm64`: accepted-pin run `34686618053`, source `7bd4f9ee`, 6 passed, 0 failed, 0 skipped; issue [#18](https://github.com/Vbitz/neurocontainers-arm64/issues/18).
- `afib1` / `arm64`: accepted-pin run `34686701687`, source `7bd4f9ee`, 5 passed, 0 failed, 0 skipped; issue [#21](https://github.com/Vbitz/neurocontainers-arm64/issues/21).
- `arfiproc` / `arm64`: accepted-pin run [34686847933](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686847933) pending; issue to be created by the workflow reporter.
- `b0map` / `arm64`: accepted-pin run [34686964891](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686964891) pending; issue to be created by the workflow reporter.

## Integration

- Accepted integration SHA: `7bd4f9ee9734c4dd3a449290c39955f009f081d3`
- Top-level submodule pointer advances from `87e1c726` to the tested Globus candidate.

## Next action

Review `b0map` and `arfiproc`, record their final issue outcomes, then continue
with the next eligible declared recipes while keeping this queue synchronized.
