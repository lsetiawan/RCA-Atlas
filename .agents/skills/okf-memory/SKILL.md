---
name: okf-memory
description:
  Use before answering any question about this project's design, data, or a past
  decision; before changing code in an area that may carry recorded constraints;
  when a decision or non-obvious discovery from this session should outlive it;
  or when `okf validate` fails. Not for how-to-run questions, which the READMEs
  answer.
---

# OKF Memory

Project memory is the OKF v0.2 bundle at `knowledge/` in the repository root.
Read it and write it only through the `okf` CLI, run as `pixi run okf` (the
binary from the pixi environment; there is no pixi task). Run it from the
repository root, where the bundle path defaults to `knowledge` and can be
omitted; from any other directory okf treats that directory as the bundle.

## Quick reference

| Task                      | Command                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| Find what is recorded     | `pixi run okf search "<keywords>" --limit 3`                                                              |
| Concepts governing a file | `pixi run okf search --for-path <path/to/file>`                                                           |
| Read one concept          | `pixi run okf show <id>`                                                                                  |
| Record                    | `pixi run okf create <area>/<slug> --type <Type> --title "<t>" --desc "<d>" --tags "<a,b>" --body "<md>"` |
| Revise                    | `pixi run okf update <id> --desc "<d>"` (also `--title`, `--body`, `--status`)                            |
| Link two concepts         | `pixi run okf relate <src-id> <tgt-id> --desc "<why they relate>"`                                        |
| Check the bundle          | `pixi run okf validate --strict --drift`                                                                  |

Add `--json` for machine-readable output. `pixi run okf help <command>` lists
the rest. Pass `--actor <harness>:<model>` (for example
`claude-code:claude-opus-5-5`) to `create`, `update`, and `relate`; without it
okf records the generic `agent/cli`.

## Read before write

1. Search first. On a fresh bundle an empty result is normal; go on to create.
   Do not browse `knowledge/` with `find`, `grep`, or `cat` to learn what is
   there; `search` and `show` are the readers. Read a hit's one-line description
   and `show` it only if needed.
2. Before the first edit in a subsystem, run `search --for-path` on the file. A
   hit with `governance: hold` means stop and confirm with the user. A hit with
   `governance: constraint` lists invariants the change must keep.
3. If a concept already covers the topic, `update` it. Do not create a `-v2`.
   Keep superseded reasoning in a "Superseded" section of the same concept.

## What to record

| Persist                                                     | Discard                                         |
| ----------------------------------------------------------- | ----------------------------------------------- |
| Decisions, rejected alternatives, and their trade-offs      | Naming deliberations, momentary thoughts        |
| Requirements, constraints, platform or performance targets  | One-off prompt instructions ("make it shorter") |
| Non-obvious quirks, workarounds, undocumented tool behavior | Anything the official docs already say          |
| Root causes of subtle bugs                                  | Syntax errors fixed in one step                 |
| Explicit, durable directives from the project owner         | Transcripts, scratch notes, chain of thought    |

The test: would an agent starting from a blank context benefit from knowing
this? Concept IDs are `<area>/<slug>`, where area is one of `decisions`,
`architecture`, `facts`, `requirements`, `bugs`. Types are free-form; use
`Decision`, `Architecture`, `Fact`, `Requirement`, or `Bug` unless the concept
is clearly something else. Mark inferences as inferred and name what would
confirm them; do not write a guess as a fact.

## Frontmatter fields with no CLI flag

`show --json` prints them. Opening the one concept file you are changing and
editing these fields by hand is allowed; validate afterwards.

| Field         | Meaning and rules                                                                     |
| ------------- | ------------------------------------------------------------------------------------- |
| `code_refs`   | Paths or globs the concept governs, relative to the repo root. No `..`, no `/` start. |
| `governance`  | `hold`, `constraint`, or `context`; surfaced by `search --for-path`.                  |
| `stale_after` | `YYYY-MM-DD`; `validate --stale` fails the gate once it passes.                       |
| `sources`     | Documents, commits, or URLs the knowledge came from.                                  |
| `verified`    | Human-only. Never write it; `generated` is the agent's provenance and okf sets it.    |

## Repo-specific traps

- Keep `description:` on one line; detail goes in the body. okf reads a
  `description:` folded onto later lines as empty, and `validate` does not flag
  it. Prettier with `--prose-wrap=always` folds long lines this way, so keep
  `knowledge/` out of any formatter or pre-commit hook.
- Write `--body` with real line breaks, for example bash
  `$'## Context\n\nText'`. In a plain `"..."` string, `\n` reaches okf as a
  backslash and an `n`, and okf stores it that way.
- `update --body` replaces the whole body, including the `# Related Concepts`
  list that `relate` appends. Copy that list into the new body or rerun
  `relate`; a concept left with no links fails `validate --strict` as an orphan.
- Point `code_refs` at tracked files. Gitignored paths, such as the
  release-restored `data/`, `runtime_data/`, and `source_material/` trees, are
  absent from a fresh clone, where `validate --drift` warns about them.
- okf stamps `log.md` and `generated.at` in UTC.

## Done

- `pixi run okf validate --strict --drift` reports 0 errors, 0 warnings, and no
  "producer gate failed".
- `pixi run okf show <id>` prints a non-empty Description for each concept
  touched.
- `git status --short` shows no okf files outside `knowledge/`; a stray
  `<area>/` directory or `log.md` means okf ran outside the repository root.

## Rules

- No hand-written concept files. Create and change them through `okf`; the
  hand-edited fields above are the only exception.
- Never forge `verified:`; never persist scratch, transcripts, or speculation.
- A human correction wins. Never restore or re-infer an assumption a human has
  rejected.
- Never "fix" a validation failure by deleting the concept it points at without
  saying so.
