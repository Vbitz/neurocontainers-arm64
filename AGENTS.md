# ARM64 container development

This repository owns manual build orchestration and documentation. Recipes,
fulltest suites, and shared builder fixes belong in the `neurocontainers`
submodule, whose origin is `https://github.com/Vbitz/neurocontainers.git`.
Read `neurocontainers/AGENTS.md` before changing those files.

- Keep GitHub Actions disabled on Vbitz/neurocontainers at repository level.
  Do not remove upstream workflows or enable the fork's CI.
- Commit and push recipe/test changes to a branch in that fork first, then
  commit and push the updated submodule pointer here. Never push to upstream.
- Build one recipe per manual dispatch in this repository. Use native ARM64
  and require deploy checks and fulltest to pass against the newly built image.
- Keep one issue per recipe/variant and post the result of every finished run,
  including failures and links to the source, run logs, and artifacts.
- Do not mark recipes ARM64 compatible solely because they generate a
  Dockerfile. Use actual build and runtime results, and document failures.
- Validate orchestration with `uv run --project neurocontainers --frozen python
  -m unittest discover -s tests` and `actionlint` when available.

Example dispatch:

```sh
gh workflow run build-arm64.yml -R Vbitz/neurocontainers-arm64 \
  -f recipe=dcm2niix -f neurocontainers_ref=arm64/dcm2niix
```
