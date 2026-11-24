# SPEC: Derivation data — component/allomorph inventory + per-form map

## 1. Intent and Executive Summary

**Problem Statement:** Stage-1 conversion needs its knowledge layer: the Wampanoag component/allomorph inventory and a per-unique-form derivation map over the corpus lexicon.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Build the component/allomorph table on the Nisinoon schema columns (Allomorph-A/Condition-A) from Fermino 2000 pp. 14-58 conditioning rules, cross-anchored to corpus Goddard-1981 proofed lines; seed the per-form map over the corpus lexicon's 66,863 forms with provenance classes (rule-derived / human-verdict / flagged).

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** The conditioning system is Fermino's (stem-initial classes: consonant / dependent-vowel / 8-initial / non-dependent-vowel + intrusive t / 3rd-before-labial); Hicks 2006 contributes initials/finals segmentation classes; every form carries a provenance flag from birth.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

The conversion engine itself (roadmap item 3); ML machinery; rendering.

## 3. Requirements

- **R-1:** The component/allomorph data encodes Fermino's conditioning system + prefix paradigms in the Nisinoon-compatible schema.
- **R-2:** The per-form map carries every one of the corpus lexicon's forms with a provenance class.
- **R-3:** No form is silently assigned — unmapped forms carry the 'flagged' class.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Allomorph table rows cite their Fermino/Goddard anchors (R-1) | structural | read the table; assert per-row anchor fields |
| SC-2 | Map keys cover the corpus lexicon 1:1 (R-2) | structural | set-compare the lexicon's match_keys against the map's keys; zero missing |
| SC-3 | Every map row carries exactly one provenance class (R-3) | structural | read the map; assert class membership on every row |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Fermino 2000 + Hicks 2006 | derivation authority | snea-phonetics docs/research/reference-pdfs/ | satisfied |

## 6. Traceability

Each requirement names the SCs verifying it (in §4's criterion wording); each SC names its R-x. No orphans in either direction.

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (snea-phonetics submodule tree) | read, 2026-11-23 |
| Goddard-1981 proofed phonology | data | corpus docs/research/sources/goddard-1981-mass-phonology-lines.tsv | read, 2026-11-24 |

## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
