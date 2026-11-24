# SPEC: Render pipeline — interlinear LaTeX/PDF + Markdown

## 1. Intent and Executive Summary

**Problem Statement:** The joined columns need their delivery surfaces: interlinear LaTeX/PDF works and Markdown books/units ('for now, tex/PDF; markdown').

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Emitter from the registry's joined rows into the unit PDFs and Markdown books; glyphs from the corpus contract's glyph inventories; LaTeX byproducts excluded from git (the exact ignore set already carries them).

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** Delivery targets fixed by the 2026-11-23 ruling; apparatus integration is roadmap item 7; nothing in the render path bypasses the joined data.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

Apparatus/provenance marks (roadmap item 7); content editing.

## 3. Requirements

- **R-1:** The emitter SHALL produce a PDF per declared work and Markdown per book/unit from registry targets.
- **R-2:** Rendered verse text SHALL match the joined rows for every verse — the outputs and the rows agree completely.
- **R-3:** Glyph coverage SHALL run against the contract's inventories; uncovered glyphs SHALL fail loudly with a named report.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Every declared target emits its PDF + Markdown | structural | run full build; artifact set == target set (R-1) |
| SC-2 | Verse text matches joined rows for every verse | structural | extract all verse strings from outputs; compare against the rows; zero differences (R-2) |
| SC-3 | Uncovered glyph aborts with a named report | structural | feed an uncovered glyph; assert the named failure (R-3) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Roadmap item 5's join | the joined rows this pipeline renders (its ticket) | pending |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1 |
| R-2 | SC-2 |
| R-3 | SC-3 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (the corpus/ submodule — Brothertown-Language/algonquian-library) | read, 2026-11-23 |


## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
