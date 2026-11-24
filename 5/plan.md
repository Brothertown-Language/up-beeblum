<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# PLAN — Derivation data: component/allomorph inventory + per-form map (up-beeblum#5)

## 1. Goal

Implement up-beeblum#5's spec: encode Fermino 2000's Wampanoag prefix-conditioning
system as a component/allomorph inventory verified against the thesis's attested
paradigm rows and the corpus's Goddard-1981 attested third-person forms, and seed
a per-form provenance map over all 66,863 corpus-lexicon match_keys. Deliverables
land in `data/derivations/` (inventory + map) and `src/up_beeblum/` (the rule
engine and map builder), with pytest instruments under `test/`. The `corpus/`
submodule is consumed read-only at its recorded pin; nothing outside this repo's
tracked tree is written.

## 2. Execution surface

- Repository: the root repo (up-beeblum); work lands on branch
  `feature/5-derivation-data` cut from the verified trunk tip (stated live by the
  `git-workflow-branch` freshness step at branch creation — main == origin/main
  at session start, corpus submodule at-tip).
- Environment facts the items depend on:
  - Source of record for conditioning content: Fermino 2000 PDF at
    `snea-phonetics/docs`-recorded location `private/Wampanoak/` of the
    snea-phonetics workspace (read-only reference; the spec's §7 row).
  - **Hicks 2006 is not currently locatable locally** (the snea-phonetics
    reference-pdfs directory is empty; the thesis bitstream is recorded as
    unlocated in the snea-phonetics calibration notes). No SC tests Hicks
    content; Hicks's initials/finals segmentation classes are **not fabricated** —
    the inventory encodes what the in-hand sources (Fermino + the Goddard-1981
    attested lines) support, per spec §9's edge case. If the PDF is re-acquired
    mid-cycle, the inventory extends under the same provenance discipline.
  - Corpus lexicon: `corpus/docs/research/data/eliot-tritext/lexicon/word-forms.tsv`
    (66,863 match_keys) at the recorded pin `bf3750158bfaf30227c301418f228de44b110872`.
  - Python toolchain runs through `uv` only (`uv run pytest test/`, `uvx ruff`,
    `uvx pyright`) per the root AGENTS.md build table.

## 3. Items — one item per success criterion

### Item 1 (SC-1)

- **Deliverable**: `data/derivations/components.tsv` — the component/allomorph
  inventory on the Nisinoon schema columns (Form; Component Type; Allomorph-A;
  Condition-A; stem-occurrence columns A-set), encoding Fermino's stem-initial
  classes (consonant / dependent-vowel / 8-initial / non-dependent-vowel +
  intrusive-t / 3rd-before-labial) and the noun/verb prefix paradigms her
  examples attest; plus `src/up_beeblum/conditioning.py` — the rule engine that
  takes (prefix slot, stem initial) and produces the conditioned prefix allomorph.
- **RED**: the authored pytest attested-paradigm suite fails — for each Fermino
  example paradigm (uhkôt: nuhkôt/kuhkôt/wuhkôt; 8sh: n8sh/k8sh/8shah; apun:
  nutapun) the engine's output does not match the thesis forms, because the
  inventory table and engine do not yet exist.
- **GREEN**: transcribe/encode the conditioning rules from the Fermino source
  into the table + implement the engine minimally until the attested paradigms
  pass. No speculative rule classes beyond what the attested examples need.
- **Tier marks**: `test/test_conditioning.py` — `smoke`.
- **Instrument**: `uv run pytest test/test_conditioning.py` — the attested
  paradigm rows are the assertions (SC-1's instrument exactly).

### Item 2 (SC-4)

- **Deliverable**: the third-person conditioning rows of Item 1's table extended
  and the engine's noun-inflection path verified against the corpus's
  Goddard-1981 proofed phonology lines (`corpus/docs/research/sources/
  goddard-1981-mass-phonology-lines.tsv` at the recorded pin).
- **RED**: the authored pytest attested-forms suite fails — the engine cannot
  reproduce uhquan, wuhkontash, wuhpit, uhpeteog (attestant wuhpeteog), wék from
  their documented stems/conditions, because the third-person rows do not yet
  carry those conditions.
- **GREEN**: add/adjust only the third-person conditioning rows the attested
  forms require; every encoded row keeps its source citation (Fermino page or
  Goddard line reference) in the table's condition/provenance columns.
- **Tier marks**: `test/test_conditioning.py` (extended) — `smoke`.
- **Instrument**: `uv run pytest test/test_conditioning.py` — the attested
  Goddard forms are the assertions (SC-4's instrument exactly).

### Item 3 (SC-2)

- **Deliverable**: `src/up_beeblum/derivation_map.py` + `data/derivations/
  form-map.tsv` — the per-form map carrying every corpus-lexicon match_key
  (1:1 with word-forms.tsv) with a provenance class. Seeding: a form receives
  `rule-derived` only where Item 1/2's engine actually derives its shape
  (rule_id recorded in the marker column); every other form carries `flagged`
  — never silently assigned. Build is deterministic per corpus pin.
- **RED**: the authored pytest coverage test fails — the map file does not
  exist / does not cover the lexicon's match_keys 1:1 (set-compare nonempty).
- **GREEN**: implement the map builder (reads word-forms.tsv at the pin, assigns
  classes per the seeding rule above, writes form-map.tsv) until coverage is
  total with zero missing keys.
- **Tier marks**: `test/test_derivation_map.py` — `smoke` (set-compare +
  determinism re-run on a fixture slice); the full 66,863-key set-compare and
  pin-determinism check runs at cycle time as the recorded instrument.
- **Instrument**: `uv run pytest test/test_derivation_map.py` plus the
  set-compare run over the committed map vs the full lexicon (executed at cycle
  time; output recorded in the issue's validation record).

### Item 4 (SC-3)

- **Deliverable**: `test/test_provenance.py` — the provenance-integrity audit:
  every non-flagged row of form-map.tsv carries the provenance marker its class
  claims (rule_id for rule-derived; verdict id for human-verdict); every
  marker-less row carries `flagged`.
- **RED**: the audit fails as authored — the invariant is not yet asserted and
  no map satisfies it yet in this cycle's run order (Item 3's map becomes the
  audited artifact once committed).
- **GREEN**: the audit passing over Item 3's committed map; any row the audit
  exposes as marker-less is corrected to `flagged` — the derive-and-flag
  discipline's data-side guarantee, never relaxed to make the audit pass.
- **Tier marks**: `test/test_provenance.py` — `smoke`.
- **Instrument**: `uv run pytest test/test_provenance.py` (SC-3's instrument
  exactly).

## 4. Dependency order

1 → 2 → 3 → 4. Item 2 extends Item 1's table and engine (its RED is Item 1's
commit precondition). Item 3's rule-derived seeding invokes Items 1–2's engine —
the map cannot claim rule-derived rows the engine cannot derive. Item 4 audits
Item 3's map artifact. Each item commits before the next item's RED.

## 5. Traceability

| Item | SC(s) | Requirements |
|------|-------|--------------|
| 1 | SC-1 | R-1 |
| 2 | SC-4 | R-4 |
| 3 | SC-2 | R-2 |
| 4 | SC-3 | R-3 |

All four SCs covered; no orphan in either direction.

## 6. Verification summary

- Authored tests, all `smoke` tier: `test/test_conditioning.py` (Items 1–2),
  `test/test_derivation_map.py` (Item 3), `test/test_provenance.py` (Item 4).
- Default gate at cycle time and PR-check time: `uv run pytest test/` (smoke
  tier, the AGENTS.md default) plus `uvx ruff check src/ test/` and
  `uvx pyright src/`.
- Recording instruments (executed at cycle time, output recorded in the issue's
  validation record): the full set-compare (SC-2) and the pin-determinism re-run.
- No heavy-tier or pr-validation-tier tests are planned; no behavioral SCs exist
  in this spec, so no harness dispatch (implement §11) applies.
- A sub-agent transcription dispatch (Fermino source → conditioning-rule notes)
  may be used during Item 1's GREEN; its output is working input, not a test
  artifact.

## 7. Status boundary

No status fields in this plan; implementation state lives in the pipeline and
the issue's validation record.

<!-- Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash) -->
