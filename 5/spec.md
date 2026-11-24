# SPEC: Derivation data — component/allomorph inventory + per-form map

## 1. Intent and Executive Summary

**Problem Statement:** Stage-1 conversion needs its knowledge layer: the Wampanoag component/allomorph inventory and a per-unique-form derivation map over the corpus lexicon.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Build the component/allomorph table on the Nisinoon schema columns (Allomorph-A/Condition-A) from Fermino 2000 pp. 14-58 conditioning rules, conditioning-rule calibration to attested forms is stage-1's calibration task (roadmap item 3); seed the per-form map over the corpus lexicon's 66,863 forms with provenance classes (rule-derived / human-verdict / flagged).

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** The conditioning system is Fermino's (stem-initial classes: consonant / dependent-vowel / 8-initial / non-dependent-vowel + intrusive t / 3rd-before-labial); Hicks 2006 contributes initials/finals segmentation classes; every form carries a provenance flag from birth.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

- The conversion engine itself — roadmap item 3's deliverable; this item produces only the data it consumes.
- ML machinery — the assist belongs to the engine stage (item 3); the data layer declares provenance classes only.
- Rendering — edition output is roadmap item 6's deliverable.

## 3. Requirements

- **R-1:** The component/allomorph data SHALL encode Fermino's conditioning system + prefix paradigms such that the table's rules reproduce Fermino's attested example paradigm rows (nuhkôt/kuhkôt/wuhkôt per uhkôt; n8sh/k8sh/8shah per 8sh; nutapun per apun).
- **R-2:** The per-form map SHALL carry every form of the corpus lexicon (66,863 match_keys) with a provenance class.
- **R-3:** No form SHALL be silently assigned — unmapped forms SHALL carry the `flagged` class.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | The table's rules reproduce Fermino's attested paradigm rows | structural | run the encoded conditioning rules over Fermino's example set (uhkôt/8sh/apun paradigms); outputs match the thesis forms (R-1) |
| SC-2 | Map keys cover the corpus lexicon 1:1 (66,863) | structural | set-compare lexicon match_keys vs map keys; zero missing (R-2) |
| SC-3 | No form is silently assigned: every non-flagged row carries the provenance marker its class claims; rows lacking the marker carry `flagged` | structural | read the map; for each non-flagged row assert the stated rule/verdict provenance marker exists; assert every marker-less row carries `flagged` (R-3) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Fermino 2000 + Hicks 2006 | the derivation authority the data encodes | satisfied |
| Corpus store (lexicon word-forms.tsv at the recorded pin) | the input SC-2's set-compare consumes | pending |

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
| Fermino 2000 (Baird), Introduction to Wampanoag Grammar | reference PDF | snea-phonetics docs/research/reference-pdfs/ | tracked + sha-recorded 2026-11-24 |
| Hicks 2006, A List of Initials and Finals in Wôpanâak | reference PDF | snea-phonetics docs/research/reference-pdfs/ | tracked + sha-recorded 2026-11-24 |

## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
