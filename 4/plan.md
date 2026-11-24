# PLAN: Text-copy regeneration tooling — up-beeblum#4

## 1. Goal

Implements the up-beeblum#4 spec: a package tool that reads the corpus
exports contract surfaces (alignment store, per-row Eliot provenance flags)
at a recorded `corpus/` pin and regenerates the committed text copies —
`data/editions/<edition>/<BOOK>/<column>.tsv` per the fixed layout rule —
with per-copy build manifests under `data/manifests/`. Delivers the
regenerated copies for edition `1663-first` at pin `bf375015` (the only
pin-supported edition/column set at that pin: coverage-driven, `wlp` and the
`1685-second` columns have no export surface there and are not fabricated).

## 2. Execution surface

- Repository: this repo (up-beeblum); feature branch `feature/4-text-copy-regeneration`
  cut from trunk at its verified remote tip.
- The `corpus/` submodule is the pinned data seam (recorded pin `bf37501584...`);
  the tool reads it through its imports at emission time only. Tests never
  depend on the submodule content — they run against a fixture corpus slice
  under `test/fixtures/corpus/`.
- Toolchain: `uv run pytest test/` (smoke tier, default), `uvx ruff check`,
  `uvx pyright src/`. No new runtime dependencies (stdlib only).

## 3. Items — one item per success criterion

**Item 1 (SC-1) — tool entry point + deterministic emission**

- **Deliverable:** `src/up_beeblum/regenerate.py` exposing `main(argv)` and
  runnable as `python -m up_beeblum.regenerate` (`uv run python -m ...`).
  It takes corpus root and output roots and emits the edition's copies and
  manifests into the output roots. Emission is deterministic by construction:
  rows in alignment-store order (spine order), UTF-8, `\n` line endings,
  header `verse_id\tflag\ttext`, no timestamps.
- **RED:** a test calls `main()` twice against the fixture corpus into two
  temp output roots and asserts the two output trees are byte-identical and
  contain the expected copy files. Fails today: the module does not exist.
- **GREEN:** implement the emission pass. Minimal: no flags/manifest
  semantics yet beyond emitting the copies' three columns.
- **Tier marks:** smoke (default tier, unmarked).
- **Instrument:** the test (red → green); then the SC-1 instrument for real:
  `uv run python -m up_beeblum.regenerate` twice into temp output dirs at the
  recorded pin, `diff -r` the two trees — zero differences.

**Item 2 (SC-4) — spine correspondence and emitted file set**

- **Deliverable:** the tool reads every copy's rows from the alignment store
  (`corpus/docs/research/data/eliot-tritext/alignment/alignment.tsv`), mapped
  per the 1663 column set: `eliot1663 → orig`, `geneva1599 → frame`,
  `web → web`; one TSV per book per column; the emitted file set equals the
  store's spine-supported book set (66 books) × the edition's 3 supported
  columns; the `1685-second` edition emits none of its columns at this pin.
- **RED:** a test asserting, per book and column, the emitted copy's rows
  equal the fixture store's rows and that the emitted file set equals the
  fixture store's book set × the supported columns. Fails today (no
  store-driven emission).
- **GREEN:** store-driven enumeration and per-row mapping; the layout rule
  `data/editions/<edition>/<BOOK>/<column>.tsv` under the output root.
- **Tier marks:** smoke.
- **Instrument:** the test; then the real-pin run: every emitted copy's rows
  compared row-by-row against `alignment.tsv` for its book/column; file-set
  equality against the store's book set.

**Item 3 (SC-3) — per-row provenance flags**

- **Deliverable:** every copy row carries a flag in `ok/uncertain/gap`:
  the corpus per-book flag file (`sources/eliot1663/<book>_full.tsv`, column
  `flag`) overrides for the `orig` column where a row exists; every other
  flag is presence-derived from the alignment-store cell (text present →
  `ok`, empty → `gap`). No row's flag is dropped silently; the rule is
  recorded in the copy's manifest.
- **RED:** a test asserting every emitted copy row's flag column is
  populated and in the `ok/uncertain/gap` vocabulary, and that an
  `uncertain` row in the fixture store's flag file surfaces in the emitted
  copy. Fails: flags are unimplemented/blank.
- **GREEN:** the flag derivation pass.
- **Tier marks:** smoke.
- **Instrument:** the test; then the real-pin run: assert the flag column is
  non-empty for every row of all 198 emitted copies, and spot-assert the
  corpus ledger's flag counts (e.g. EXO 0/571/642) against the emitted
  `orig` copy for one shipped book.

**Item 4 (SC-2) — per-copy build manifests**

- **Deliverable:** one deterministic manifest
  `data/manifests/<edition>/<BOOK>/<column>.json` per emitted copy,
  recording the ROADMAP anchor's exact fields — `corpus_sha` (the recorded
  pin's SHA of the corpus checkout, read via `git -C <corpus_root>
  rev-parse HEAD`) and `derivation_data_version` (an optional
  `data/derivations VERSION` file's value, else `0` at this skeleton) —
  plus `edition`, `book`, `column`, `rows`, and the flag tally. No
  timestamps.
- **RED:** a test asserting each emitted copy has a manifest whose required
  fields are present and whose `corpus_sha` matches the fixture corpus's
  recorded HEAD. Fails: no manifests.
- **GREEN:** the manifest pass.
- **Tier marks:** smoke.
- **Instrument:** the test; then the real-pin run: read the committed
  manifests, compare `corpus_sha` against the recorded pin and
  `derivation_data_version` against the empty derivation store (`0`).

**Item 5 (SC-1, SC-2, SC-4 — delivery at the recorded pin)**

- **Deliverable:** the regenerated committed copies and manifests at pin
  `bf375015` land in the working tree (`data/editions/`, `data/manifests/`)
  and are committed.
- **RED:** a check asserting `data/editions/1663-first/GEN/orig.tsv` exists
  with content — fails today (the skeleton has no book data).
- **GREEN:** run the tool at the recorded pin against the tree; commit the
  regenerated copies and manifests.
- **Tier marks:** none (delivery run; the SC instruments execute against the
  committed tree).
- **Instrument:** the SC-1/SC-2/SC-4 instruments executed against the
  committed tree (re-run tool to a temp dir, compare against the committed
  tree byte-for-byte — zero differences).

## 4. Dependency order

1 → 2 → 3 → 4 → 5. Emission must exist before its semantics (the file set,
flags, and manifests) can be asserted; manifests come last among the tool
items because they record the completed row semantics (flag tally);
delivery requires the finished tool. Item 5's RED is observable only after
item 4's commit.

## 5. Traceability

| Item | SC(s) |
|------|-------|
| 1 | SC-1 |
| 2 | SC-4 |
| 3 | SC-3 |
| 4 | SC-2 |
| 5 | SC-1, SC-2, SC-4 (execution at the recorded pin) |

Every SC (SC-1..SC-4) is covered; every item traces to at least one SC.

## 6. Verification summary

Authored tests this change, all smoke tier (default run, unmarked — the
fastest fixture-driven checks; the corpus seam is real-data-scale, fixture
tests are the smoke content): item 1 (determinism), item 2 (row/file-set
correspondence, incl. a module-boundary assertion through `main()`), item 3
(flag population + override), item 4 (manifest contract). At cycle time:
`uv run pytest test/` before each commit. The SC instruments themselves run
as direct commands against the real recorded pin (executed runs, `diff -r`,
per-row comparisons) and are recorded in the PR Evidence section — they are
instruments, not test files. At PR-check time: smoke suite plus
`uvx ruff check src/ test/` and `uvx pyright src/`.

## 7. Status boundary

No status fields here; progress lives in the pipeline and the issue's
validation record.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
