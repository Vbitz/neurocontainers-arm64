# brats: current ARM64 inference blocker

**Assessment: Complete dependency stack unresolved.**

Assessed 2026-10-13T22:21:18.445405+00:00. Package `0.1.13`; recipe baseline `4167b93854b46d07ab7139d80d9d430db5b4c561`.

The Python/Apptainer wrapper is portable and its earlier0.1.8 ARM64 installation/registry suite passed21/21. Current native **scientific inference remains blocked by its downloadable algorithm images**. All16 registered CPU-compatible image tags currently publish only Linux AMD64. The remaining56 registry entries are not CPU-compatible and require a GPU. `force_cpu` changes GPU requests; it cannot make an AMD64 image native ARM64.

See the [complete official metadata snapshot](../upstream/brats-cpu-platform-audit.json), including every queried tag URL/digest/platform, and [durable investigation](https://github.com/Vbitz/neurocontainers-arm64/issues/248). This records missing current assets; it does not claim their algorithms can never be ported from source.

Resume when one same registered CPU algorithm has a native ARM64 image or a documented portable source build with matching weights. Then reuse the known Apptainer1.4.4 ARM source configuration and verify real MRI inference before submitting this recipe's own upstream PR. Preserve existingx86 support and all wrapper tests. Do not substitute another model, use emulation or call a wrapper/help-only pass complete scientific verification.

No current investigation image build was dispatched (0/6). Original start/deadline and clean preflight branch are retained in `upstream/queue.json`. Continue with the next eligible recipe.
