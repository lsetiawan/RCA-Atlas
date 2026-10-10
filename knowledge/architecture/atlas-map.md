---
type: Architecture
title: Atlas map website
description: "The React and three.js website that draws the seafloor off Oregon in 3D with every located sensor, live panels and the Ask Atlas sidebar."
tags: [web-app, react, threejs, map]
code_refs: ["src/atlas_map/**", "docs/superpowers/specs/**"]
sources: ["src/atlas_map/README.md", "docs/superpowers/specs/2026-09-23-atlas-map-design.md", "docs/codebase/chapters/atlas-map-scene.md", "docs/codebase/chapters/atlas-map-panels.md", "docs/codebase/chapters/ask-atlas.md", "docs/codebase/flows/live-panel.md", "docs/codebase/flows/ask-atlas.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

`src/atlas_map/` is a Vite app (`npm run dev` on 127.0.0.1:5175). `App.jsx` loads the bundle from `public/atlas/` and builds the `AtlasScene` (terrain, cable, moorings, 1 m summit tiles), the DOM overlay, the HUD dock, the side panels and the Ask Atlas sidebar with its evidence layer. Live data goes through `api/gateway.js`: the Vite `/api` proxy in development and the Worker's `/v1/live` in production. Only `public/atlas/auv/` is committed. Its design specs are in `docs/superpowers/specs/`.

## Talks to

- The static bundle.
- The Cloudflare Worker.
- The gateway, directly in development.

## More

Chapter: `docs/codebase/chapters/atlas-map-scene.md`, `docs/codebase/chapters/atlas-map-panels.md`, `docs/codebase/chapters/ask-atlas.md`. Flows: `docs/codebase/flows/live-panel.md`, `docs/codebase/flows/ask-atlas.md`.

# Related Concepts
- [Atlas map data bundle](atlas-map-data.md): Loads the static bundle at startup.
- [RCA Atlas Worker](atlas-worker.md): Sends Ask Atlas questions and production live-data requests through the Worker.
