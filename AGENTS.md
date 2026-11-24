<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->

# AGENTS.md — up-beeblum

Operating rules for agents working in this repository. The architecture facts
are stated once — in `README.md` (identity, architecture, provenance) and
`ROADMAP.md` (sequencing); this file owns only the rules.

## Build / Test / Lint / Type-check

| Task | Command |
|------|---------|
| Sync dependencies | `uv sync` |
| Run tests | `uv run pytest test/` (smoke tier is the default) |
| Lint | `uvx ruff check src/ test/` |
| Type check | `uvx pyright src/` |

Never bare `python`/`python3`/`pip` — always `uv run`/`uvx`. No build exists
yet beyond the toolchain (the roadmap's render pipeline lands it); the
build never runs against the submodule trees — they are reference-only.

## Workflow discipline

- **Branch before any file modification** — feature branches
  (`feature/<slug>`, or `feature/<issue>-<slug>` when an issue exists),
  cut from `main`; `main` is the trunk; commits never land on `main`
  directly, and `issues-data` (the store branch) is out of feature work.
- **Pipeline** — changes file a spec in the local issue store
  (remote-first via `gh issue create`), then plan → implement →
  PR; PRs are opened only for completed, fully-tested work, and **merges
  are human-only** — the agent never merges and never submits an approving
  review.
- **Issue store** — `.opencode/tools/local-issues` with qualified
  `up-beeblum#N` references; the store commits its own state.
- **Temp files** — throwaway scripts/output go only in `tmp/` (gitignored);
  clean up after the task. `private/` holds rights-restricted material
  only, stays excluded, and its tracked README/AGENTS pair is the manifest
  of record; nothing else under `private/` is ever committed.
- **Attribution** — AI-authored content carries
  `Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)`
  (docstrings, README/AGENTS footers, posted content).

## Notation — the WLRP carve-out

Text 1 of the edition renders in the **Wôpanâak Language Reclamation
Project's modern orthography** (letters `a â u ee 8 ô ay e ch sh q ty …`).
This is the recorded, developer-instructed **exception** to the
parent project's standing ruling that all sources normalize into BL/Costa
orthography (snea-phonetics notation SOP, 2026-11-23): this repository's
edition text is not a BL-notation surface. The derive-and-flag disciplines
apply — the per-form derivation data (under `data/derivations/`) carries
provenance flags for every form; unresolved readings are flagged and
rendered marked, never silently filled; conversion is never regex — it is
segmentation + rule classes + reviewed per-form verdicts, with any ML
output provisional until a reviewed verdict lands.

## Submodules — reference only

`corpus/` (algonquian-library) and `snea-lib/` are provenance seams, never
build dependencies: the committed text copies and derivation data are
regenerated at each `corpus/` pin bump (the evergreen pin-bump procedure —
fetch, checkout the recorded tag/branch, commit the pointer, verify
upstream reachability), and every build manifest records the corpus SHA the
copy was generated from. Pointer-bump commits carry pushed hash-permanence
tags in the submodule repos. Never recursive submodule operations — every
operation is per-path.

<!-- Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash) -->
