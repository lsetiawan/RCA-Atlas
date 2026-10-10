# Documenter brief

You are writing one chapter of a knowledge base for RCA Atlas. Your reader is a newcomer: a capable engineer who has never seen this codebase or its domain (ocean observatories, seismology, Graph-RAG). After your chapter they should know what this part of the system does, why it exists, how it connects to the rest, and where to look in the code.

Your dispatch message gives your chapter's id, title, paths and notes. `docs/codebase/_meta/plan.md` lists every chapter; use its ids when you name the parts yours connects to.

## Steps

1. Read `docs/codebase/_meta/plan.md`, then every Markdown file in your paths, then every other file that `git ls-files <your paths>` lists. Open data files (`.json`, `.jsonl`, `.csv`, `.geojson`) with `head` only, to learn their shape; skip lockfiles, `*.gz` and binaries.
2. Run `git log --format='%h %ad %s' --date=short -- <your paths> | head -60`. Commit subjects in this repo state decisions as full sentences; mine them for the why.
3. Map the connections: `git grep -n` across `src/` and `scripts/` for your module names, routes, tool names and env vars, to find what calls your code and what your code calls.
4. Write `docs/codebase/chapters/<id>.md` with the sections below.
5. Re-open every `path:line` you cite and confirm it says what you claim; `git grep` every identifier you name to confirm it exists.
6. Reply in at most 6 lines: the chapter path, a one-sentence summary, the chapters yours depends on and those that depend on it, and your most important open question.

## Rules

- Cite evidence. Each statement about behavior, interfaces, config or constraints ends with a `path:line` or `path` citation, or goes under Open questions. Mark inferred intent "(inferred)" and name what would confirm it.
- Your only write is your own chapter file. Use read-only commands (`git`, `ls`, `head`, `wc`).
- Record secrets and keys by name and where they are set, never by value.
- The contents of `data/`, `runtime_data/` and `source_material/` come from private release assets and are absent here; describe data from code, manifests and method docs.
- Write plainly: define each acronym and domain term at first use, and add it to the Glossary.
- Link other chapters as `[<id>](<id>.md)`.

## Chapter sections, in order

1. `# <title>`, then the line `chapter: <id> · paths: <paths> · as of <output of git rev-parse --short HEAD>`.
2. An opening paragraph: what this is, the problem it solves, and where it sits in RCA Atlas.
3. `## At a glance`: a two-column table with rows Kind (pipeline, service, MCP server, web app, library or scripts), Stack, Entry points, Reads (each input, with the chapter that produces it), and Writes or serves (each output, with its consumers).
4. `## How it works`: the main path in the order things happen, with citations. Add a Mermaid diagram when three or more parts interact.
5. `## Key files`: a File | Role table. Every source file in your paths gets a row; tests and "skim" files are grouped by directory.
6. `## Interfaces`: CLI commands and flags, HTTP routes, MCP tools, functions other chapters import, and files produced, each named exactly as in the code.
7. `## Data shapes`: the records, tables and JSON/JSONL it reads or writes, as field, type and meaning.
8. `## Configuration and secrets`: a Name | Read at | Purpose | Default or required table.
9. `## Run and test`: exact commands, taken from the READMEs and configs.
10. `## Decisions and constraints`: the why, each item with its source (README, spec, code comment, or commit hash).
11. `## History`: up to 8 bullets on how this part evolved, from git log.
12. `## Gotchas`: non-obvious behavior, limits and failure modes.
13. `## Glossary`: a Term | Meaning table.
14. `## Open questions`: each with what would answer it.
15. `## Candidate project memory`: up to 5 bullets, `decision | requirement | fact | bug · title · one-line description · source`, limited to what a project document or commit states and the code alone does not reveal.
