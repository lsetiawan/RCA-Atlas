---
type: Architecture
title: Data and release lifecycle
description: Versioned corpus data stays out of Git and moves between machines as private GitHub Release assets that scripts/bootstrap_machine.sh verifies and restores.
tags: [releases, data, restore, github-releases]
code_refs: ["scripts/**", "src/DATA_CORPUS_METHOD.md", "data/README.md", "runtime_data/README.md", "source_material/README.md", ".gitignore"]
sources: ["README.md", "docs/codebase/chapters/repo-ops-data.md", "docs/codebase/flows/transfer-release.md", "docs/codebase/flows/restore-and-run.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

The corpus (`data/`), its originals (`source_material/`) and the derived runtime state (`runtime_data/`) are gitignored. `scripts/build_transfer_release.sh` packs them into three zstd archives named with the catalog fingerprint, plus `release-manifest.json`. `scripts/build_runtime_overlay_release.sh` packs the literature full-text cache as a supplemental release. `scripts/bootstrap_machine.sh` downloads the assets with `gh`, checks each byte count and SHA-256, and extracts base archives before the overlay into the current directory.

## Talks to

- GitHub Releases, through the `gh` CLI.
- The Graph-RAG runtime: its catalog fingerprint names the archives, and the restored `runtime_data/GraphRAG/` feeds its loader.
- The data-maintenance scripts, which clean `data/` and audit it before a release.

## More

Chapter: `docs/codebase/chapters/repo-ops-data.md`. Flows: `docs/codebase/flows/transfer-release.md`, `docs/codebase/flows/restore-and-run.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Release archives are named by the runtime's catalog fingerprint, and the restored runtime_data feeds its loader.
