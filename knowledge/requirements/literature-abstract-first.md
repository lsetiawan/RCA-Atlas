---
type: Requirement
title: Literature answers start from abstracts
description: "Agents search the abstract corpus first and fetch full text only when a relevant abstract is insufficient, never bypassing paywalls, logins or access controls."
tags: [literature, full-text, agents]
code_refs: ["src/literature_fulltext/**"]
sources: ["src/literature_pipeline/README.md", "src/literature_fulltext/README.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Requirement

`src/literature_pipeline/README.md:20-22` and `src/literature_fulltext/README.md:3-7`: the agent searches `data/Literature/chunks.jsonl` first; only a relevant but insufficient abstract may trigger `literature_full_text_evidence` with `retrieval_reason=abstract_relevant_but_insufficient`. The tool does not authenticate or evade access controls (`src/literature_fulltext/README.md:21-22`).

## Scope

Bulk acquisition exists only as an operator script gated by `--confirm-open-access`. Answers get at most 10 passages, and passage text is untrusted data.

# Related Concepts
- [Literature full-text tools](../architecture/literature-fulltext.md): Governs when the full-text tool may run.
