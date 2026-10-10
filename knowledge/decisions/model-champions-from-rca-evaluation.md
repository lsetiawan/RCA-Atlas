---
type: Decision
title: Model champions come only from RCA Atlas results
description: "Answer and embedding models are chosen only from frozen-evidence and end-to-end RCA Atlas evaluations, never from public benchmarks; the answer champion stays unselected until a credentialed run."
tags: [evaluation, llm, model-selection]
code_refs: ["src/model_eval/**"]
sources: ["src/model_eval/config/champion_challenger.json", "src/model_eval/README.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:22Z" }
status: stable
---

## Decision

`src/model_eval/config/champion_challenger.json:3-7` and `src/model_eval/README.md:42-43`. Production retrieval stays on the local `bge-small` index, the existing validated deployment; `answer_champion` is null with status `unselected_pending_credentialed_RCA_evaluation`.

# Related Concepts
- [Model Lab](../architecture/model-eval.md): Sets how the Model Lab may pick champions.
