<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->

# up-beeblum

**up-beeblum** is the quad-text polyglot edition of the Eliot Indian Bible —
*Mamusse Wunneetupanatamwe Up-Beeblum God* — for the Brothertown Language
project. It presents, per verse, four parallel texts across both printed
editions:

- **Modern Wampanoag** — the Eliot text rendered in the Wôpanâak Language
  Reclamation Project's modern orthography, derived best-effort by an
  IPA-mediated conversion chain (colonial orthography → IPA → WLRP letters),
- **Original orthography** — the colonial Massachusett reading per edition
  (1663 first edition; 1685/1680 second edition),
- **English frame** — the text the translation proceeded from (Geneva 1599
  for the first edition; KJV reference frame for the second),
- **World English Bible** — the modern-English control text.

The repository is **self-contained**: the build depends on nothing outside
the tree. The `corpus/` (`algonquian-library`) and `snea-lib/` submodules are
**reference-only** provenance seams — the committed text copies are
regenerated from the corpus contract's exported surfaces at each
`corpus/` pin bump, with every copy's provenance recorded in the build
manifests (corpus SHA, derivation-data version) it carries. Delivery
targets, once the roadmap lands them: interlinear LaTeX/PDF works and
Markdown books — with per-reading provenance carried in the apparatus, so an
unverified reading is never rendered as plain text.

## Editions and column sets

| Edition | Columns |
|---|---|
| 1663 first edition | modern WLRP ‖ eliot1663 ‖ Geneva 1599 ‖ WEB |
| 1685 second edition | modern WLRP ‖ eliot-E2 ‖ KJV ‖ WEB |

Scope is coverage-driven: the build covers both complete editions where the
corpus contract provides them — the second edition arrives near-complete via
 Higgins's 2018 proofed E2 document forms (held in the corpus store), while
the first edition grows book-by-book as the corpus proofing program
progresses; text-copy regeneration will land via roadmap work.

## Provenance and licensing

The biblical texts themselves are public domain — 17th-century works, and
proofed transcriptions of public-domain works are public domain (developer
ruling 2026-11-23); the Wikisource-source column's stated CC BY-SA terms are
quoted in provenance records, with the license class following the ruling.
The derivation's authority works are kept in the research repository —
Jessie Little Doe Fermino's 2000 *Introduction to Wampanoag Grammar* (the
WLRP co-founding grammar; prefix-allomorphy authority) and Nitana Hicks's
2006 *A List of Initials and Finals in Wôpanâak* — tracked at the
snea-phonetics research tree (`docs/research/reference-pdfs/`) and cited
here by reference. The repository name is the modern-orthography rendering
of the Bible's title word (rule-derived 2026-11-23; reconciled if WLRP
publishes an official form of the title).

## Status

Scaffold (PR: up-beeblum#1). What lands next: ROADMAP.md items 1–9 — file
the follow-up specs from the roadmap. Operating rules for agents:
`AGENTS.md`.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
