---
type: Requirement
title: Staged QARTOD output never syncs to the live dashboard
description: "Plots made with staged (homebrew) QARTOD tables may sync only under an archive prefix, because a sync without one would overwrite the live dashboard's plots."
tags: [qaqc, safety, dashboard]
code_refs: ["src/agentic_qaqc/qaqc_agent_tools.py", "src/agentic_qaqc/vendor/rca_data_tools/qaqc/pipeline.py"]
sources: ["src/agentic_qaqc/vendor/rca_data_tools/README.md", "docs/codebase/chapters/agentic-qaqc.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Requirement

`src/agentic_qaqc/vendor/rca_data_tools/README.md:17-22`: publish staged-QARTOD output to a dashboard archive with `--prefix archives/internal/<slug>`; without a prefix a `--homebrew-qartod` sync is refused so live plots are never overwritten. The toolkit repeats the refusal (`src/agentic_qaqc/qaqc_agent_tools.py:353-354`).

## Caveats

The guard only checks that the prefix is non-empty, so `/` passes it. With `QAQC_AGENT_ALLOW_PIPELINE=1`, an ordinary run with `s3_sync` and no prefix writes to the live bucket `ooi-rca-qaqc-prod` (`docs/codebase/chapters/agentic-qaqc.md`, Gotchas).

# Related Concepts
- [Agentic QA/QC tools](../architecture/agentic-qaqc.md): Constrains the vendored plot pipeline's syncs.
