---
type: Requirement
title: Corpus releases need a clean network audit
description: A corpus release passes only when audit_sensitive_network_info.py reports zero sensitive findings; no script enforces this gate.
tags: [release, security, audit]
code_refs: ["src/data_maintenance/audit_sensitive_network_info.py", "scripts/build_transfer_release.sh"]
sources: ["src/DATA_CORPUS_METHOD.md", "docs/codebase/chapters/repo-ops-data.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Requirement

`src/DATA_CORPUS_METHOD.md:776-778`: a release passes only when `sensitive_finding_count` is zero. The audit report stores only redacted previews and SHA-256 values, never the suspected secrets.

## Status

No script or CI runs the audit as part of `scripts/build_transfer_release.sh`, so the gate is a manual step. The sanitizer does not touch `source_material/`, which ships in the source-material archive (`docs/codebase/chapters/repo-ops-data.md`).

# Related Concepts
- [Data maintenance scripts](../architecture/data-maintenance.md): The audit script is this gate's check.
- [Data and release lifecycle](../architecture/data-release-lifecycle.md): Gates every corpus release.
