# SPEC: Provenance/apparatus rendering

## 1. Intent and Executive Summary

**Problem Statement:** Unverified readings must never render as plain text — the per-row provenance flags and the derivation provenance need their delivered-surface vocabulary.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Flag marks per row in PDF/Markdown outputs; the derivation provenance table (per-form IPA, verdict class, confidence) exposed for audit; marks render from the copies' carried metadata.

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** Marks derive from data already carried in the copies (the regeneration tool's R-3); the mark vocabulary is declared once.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

Derivation data content; rendering engine changes beyond mark rendering.

## 3. Requirements

- **R-1:** Each delivered row renders its provenance mark per the declared vocabulary.
- **R-2:** The derivation provenance table is emitted as part of the build's outputs.
- **R-3:** A row lacking provenance metadata fails the build rather than rendering unmarked.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Marks render per vocabulary for all rows (R-1) | structural | sample outputs across flags; locate the marks |
| SC-2 | The provenance table appears in build outputs (R-2) | structural | build; locate the emitted table |
| SC-3 | Missing metadata aborts with a named error (R-3) | structural | strip a row's metadata; assert the named failure |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Roadmap item 6's render pipeline | upstream | up-beeblum item 6's ticket | pending |

## 6. Traceability

Each requirement names the SCs verifying it (in §4's criterion wording); each SC names its R-x. No orphans in either direction.

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (snea-phonetics submodule tree) | read, 2026-11-23 |


## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
