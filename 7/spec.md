# SPEC: Stage 2 — IPA→WLRP letter map + loan-class policy

## 1. Intent and Executive Summary

**Problem Statement:** Stage 1's IPA needs its deterministic rendering into WLRP letters, with the loan classes of the Eliot text handled per policy rather than per verse.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Encode the phoneme-letter map (8/uː, ee/iː, u/ə, ô/ã, ch/ʧ, q/kʷ, ty/tʲ, ...) from Baird 2000's phonemic design and the verified correspondence set; the loan-class policy layer (names keep foreign letters; assimilated loans render via allophone classes; unassimilated loans retain and flag) classifies the lexicon's forms and records the per-form loan-class field into the derivation data (an extension of item-2's row schema this stage owns).

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** Stage 2 is deterministic — no ML, no regex; every WLRP letter traces to a segment; loan policy is recorded in the derivation data, not improvised.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

- Stage-1 behavior — this stage renders upstream IPA, never re-derives it (roadmap item 3's deliverable).
- Rendering — the delivered-surface emitters are roadmap item 6's deliverable.
- Dictionary/lexicon data changes — correspondence records are captured tracked anchors, not editable data.

## 3. Requirements

- **R-1:** The stage-2 map SHALL render every legal IPA segment to exactly one WLRP letter/digraph.
- **R-2:** The stage SHALL classify the lexicon's forms into loan classes, record the classification as the derivation data's per-form loan-class field, and apply the policy — names keep loans' letters; unassimilated loans retain and flag.
- **R-3:** Stage-2 output SHALL be deterministic per input — the same input renders the same output across runs.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Map covers the phoneme inventory, no gaps | structural | cross-check map keys vs the stage-1 phoneme set; zero missing (R-1) |
| SC-2 | Loan classes classify + record + render per policy | structural | run the classifier over the lexicon; assert the loan-class field populates for every row; test the policy render paths on known loan forms (R-2) |
| SC-3 | Same input, same output across runs | structural | run twice; diff; zero differences (R-3) |
| SC-4 | Every segment's letter assignment matches the verified correspondence set | structural | cross-check each map entry against the captured correspondence rows + the Fermino 2000 phonemic chart; zero mismatches (R-1) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Up-beeblum#6 (stage-1 engine) | the IPA output this stage renders | pending |
| Up-beeblum#5 derivation data | the map rows this stage extends with the loan-class field | pending |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1, SC-4 |
| R-2 | SC-2 |
| R-3 | SC-3 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Fermino 2000 (Baird) — the phonemic design (p. 9 chart) | reference PDF | snea-phonetics docs/research/reference-pdfs/ | tracked + sha-recorded 2026-11-24 |
| Colonial↔modern correspondence rows | reference | the correspondence capture materialized at snea-phonetics docs/research/phonemic-calibration-sources-wampanoag.md §1.2 | read, 2026-11-23 |

## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
