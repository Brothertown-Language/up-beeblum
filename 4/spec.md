# SPEC: Text-copy regeneration tooling — corpus pin-bump ingestion

## 1. Intent and Executive Summary

**Problem Statement:** The committed-data skeleton holds no text copies and no machinery to produce them.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** A package tool reads the corpus contract's exported surfaces (alignment store, versification maps, per-row provenance) at a recorded `corpus/` pin and emits `data/editions/<edition>/<BOOK>/<column>.tsv` per the fixed layout rule, with per-copy build manifests.

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** Regeneration over in-place editing (2026-11-23: "Regenerated"; corrections route upstream as corpus-store issues); column codes wlp/orig/frame/web; the layout rule is fixed at the skeleton.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

Derivation stages and rendering (roadmap items 3-7); corpus-repo changes (corrections route to the corpus tracker, issue-store hygiene aside).

## 3. Requirements

- **R-1:** The tool SHALL regenerate all supported copies deterministically per pin — the same pin SHALL yield byte-identical output.
- **R-2:** Every generated copy SHALL carry a build manifest recording (corpus SHA, derivation-data version) — the ROADMAP anchor's exact two-field list.
- **R-3:** Per-row provenance flags (ok/uncertain/gap) SHALL be carried into the copies' metadata — no row's flag is dropped silently.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Two runs at the same pin produce byte-identical outputs | structural | run twice in temp dirs; diff; zero differences (R-1) |
| SC-2 | Manifests record the ROADMAP anchor's field list (corpus SHA, derivation-data version) | structural | read manifests; compare fields against the recorded pin + derivation-data state (R-2) |
| SC-3 | Flags populate for every data row of every copy | structural | read copies; assert flag columns non-empty for all rows (R-3) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Corpus store (materialized at pin) | the .gitmodules-declared reference seam at the recorded pin | pending |

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
