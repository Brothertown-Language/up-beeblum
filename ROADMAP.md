<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->

# ROADMAP — up-beeblum's follow-up work

The quad-text polyglot edition of the Eliot Indian Bible (up-beeblum#3's README
states identity and architecture; this file owns only sequencing). Each item
below names its successor spec's scope; status lives in the issue tracker,
never here. Items are sequenced as the design record orders them
(2026-11-23; quoted in up-beeblum#1) — coverage-driven,
both editions, build what the corpus contract supports.

1. **Text-copy regeneration tooling** — the corpus-contract ingestion that
   regenerates the committed text copies at each `corpus/` pin bump:
   spine-join reads of the alignment store + versification maps (corpus
   exports contract surfaces, per `algonquian-library`'s AGENTS.md), per-book
   column TSVs under `data/editions/<edition>/<BOOK>/<column>.tsv`, and the
   per-copy build manifests under `data/manifests/` recording (corpus SHA,
   derivation-data version). Anchor: up-beeblum#1 spec (architecture), corpus
   AGENTS.md exports contract.

2. **Derivation data: component/allomorph inventory + per-form map** — the
   Wampanoag component inventory (prefix allomorphy conditioned by
   stem-initial class per Fermino 2000 pp. 14–58, cross-anchored to the
   corpus's Goddard-1981 proofed lines) and the per-unique-word-form
   derivation map over the corpus lexicon's 66,863 forms, with
   rule-derived/human-verdict/flagged provenance classes. Anchor: corpus
   Nisinoon components schema (Allomorph-A/Condition-A columns);
   snea-phonetics docs/research/reference-pdfs (Fermino 2000, Hicks 2006);
   the per-form map over the corpus lexicon's 66,863 forms (eliot-tritext
   word-forms, 24 books).

3. **Stage 1 — orthography→IPA conversion** — segmentation against the
   component inventory, rule-class candidate nomination, then the
   constrained ML assist (a torch subproject in the corrector pattern:
   ranks/corrects within legal phoneme space, confidence-gated, weights
   regenerable from tracked training data; ML output is provisional until
   the form map's review layer rules). No regex for conversion; flagged
   gaps are never filled. Anchor: the 2026-11-24 development ruling
   ("/original/=>/IPA/=>Wampanoag ... place into the new repo"); corpus
   corrector precedent.

4. **Stage 2 — IPA→WLRP letter map** — the deterministic phoneme-letter
   rendering (Baird 2000's phonemic design: 8/uː, ee/iː, u/ə, ô/ã, ch/ʧ, q/kʷ,
   ty/tʲ), including the loan-class policy (names keep foreign letters;
   assimilated loans render via the allophone classes; unassimilated loans
   retain and flag). Anchor: Baird 2000 p. 9 chart; the writing-systems
   correspondence set; the modern-Mohegan loan precedent (Fielding's
   dictionaries, 2006/2012 — the Costa-designed alphabet's own treatment).

5. **Works registry + spine join** — the declarative works registry (column
   sets per edition: 1663 = wlp/eliot1663/geneva1599/web; 1685 = wlp/
   eliot-E2/kjv/web) and the build CLI joining columns on the verse-ID spine.
   Anchor: corpus works-registry pattern (`algonquian-library`
   docs/research/data/eliot-tritext/works-registry.yaml).

6. **Render pipeline — LaTeX/PDF + Markdown** — interlinear per-work PDF and
   Markdown books/units from the joined rows; apparatus carries per-row
   provenance (ok/uncertain/gap) so no unverified reading renders as plain
   text. Delivery ruling: "for now, tex/PDF; markdown" (2026-11-23).

7. **Provenance/apparatus rendering** — per-flag mark vocabulary in the
   delivered surfaces and the derivation provenance table (per-form IPA,
   verdict class, confidence) exposed for audit. Anchor: up-beeblum#1 spec
   (design consequence: provenance rides into the edition).

8. **Editions coverage manifest** — the coverage-driven build enumerating
   what the corpus spine supports per edition/book; "covering both complete
   editions if possible" (2026-11-23): E2 near-complete via the Higgins E2
   proofs (corpus era-texts store), E1 growing with corpus proofing.

9. **Ignore-policy hardening** — extend `.gitignore` with Python run debris
   (`__pycache__/`, `*.pyc`) as its own small spec + PR; the current exact
   set (up-beeblum#1 R-5) stays enumerated until then.

<!-- Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash) -->
