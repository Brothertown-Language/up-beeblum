# SPEC: Stage 1 — orthography→IPA conversion engine

## 1. Intent and Executive Summary

**Problem Statement:** Text 1's derivation needs the hard stage: colonial orthography to pronunciation segments on 66,863 attested forms with context-dependent ambiguity (preaspiration/unheard h, accent interchange, schwa-class vowels, the four values of the oo ligature).

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Segmentation against the component inventory (roadmap item 2) + rule-class candidate nomination + the constrained ML assist: a torch subproject in the corrector pattern that ranks and corrects within legal phoneme space, confidence-gated, weights regenerable, output provisional until the per-form review layer rules.

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** Per the 2026-11-24 ruling this lives in this repo ('place into the new repo along side the rest of the new'); the chain is /original/=>/IPA/=>Wampanoag; ML never free-generates — decoding is constrained to valid segmentations/phoneme sequences.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

Stage-2 letter rendering (roadmap item 4); rendering/apparatus; training-data acquisition beyond tracked anchors.

## 3. Requirements

- **R-1:** The engine SHALL consume the item-2 derivation data + the corpus lexicon and emit per-form IPA candidates, each with a confidence value.
- **R-2:** ML-assisted outputs SHALL be marked provisional until a reviewed verdict lands in the per-form data.
- **R-3:** No regex SHALL be used anywhere in the conversion path.
- **R-4:** Segmentation SHALL precede rewriting — the rewrite stage consumes segmentation output (segment objects/trace), and every emitted phoneme sequence SHALL decode to a legal sequence per the phonotactics record.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Sampled/whole-form runs emit candidates each carrying a confidence value | structural | run over a form set; assert every row carries candidate(s) + confidence (R-1) |
| SC-2 | ML-assisted rows carry the provisional flag until reviewed | structural | read output states; assert flag presence on model-touched rows (R-2) |
| SC-3 | No regex use in the conversion path | structural | grep conversion modules for re-module conversions; zero (R-3) |
| SC-4 | Emitted sequences are legal; the rewrite consumes segmentation output | structural | run the validator over emitted candidates (zero illegal); assert the engine's trace shows segmentation objects feeding the rewrite stage (R-4) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Roadmap item 2's derivation data | the item-2 data this engine consumes (its ticket) | pending |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1 |
| R-2 | SC-2 |
| R-3 | SC-3 |
| R-4 | SC-4 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (the corpus/ submodule — Brothertown-Language/algonquian-library) | read, 2026-11-23 |
| Phonotactics record | card | snea-phonetics docs/research/phonotactics.md | read, 2026-11-24 |

## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
