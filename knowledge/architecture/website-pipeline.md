---
type: Architecture
title: Website crawler
description: "Crawls coszo.org, oceanobservatories.org and Interactive Oceans into the websites collection in three stages: discover, build and package."
tags: [corpus, websites, crawler]
code_refs: ["src/website_pipeline/**"]
sources: ["src/website_pipeline/PIPELINE_README.md", "src/website_pipeline/AUDIT.md", "docs/codebase/chapters/corpus-docs-web.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`crawl.py discover|build|package` uses WordPress REST APIs, sitemaps and HTML, keeps COSZO and RCA material, collapses duplicate URLs to a canonical one with aliases, and writes `src/website_pipeline/package/`. Nothing in the repository copies the package into `data/Websites`, which the runtime serves as `websites`. Cached 200 responses never expire. `recover_io_batch.py` was a one-time recovery of a timed-out API batch.

## Talks to

- coszo.org, oceanobservatories.org and interactiveoceans.washington.edu.
- The Graph-RAG runtime.

## More

Chapter: `docs/codebase/chapters/corpus-docs-web.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Its package becomes the websites collection that the runtime serves.
