# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Per-form map instrument (up-beeblum#5, SC-2 / R-2).

The map must carry every corpus-lexicon match_key 1:1 at the recorded pin
(bf3750158), deterministically. The set-compare instrument is exactly the
spec's: lexicon match_keys vs map keys, zero missing.
"""

from __future__ import annotations

from pathlib import Path

from up_beeblum.derivation_map import MAP_HEADER, build_map

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = REPO_ROOT / "corpus"
LEXICON = CORPUS_ROOT / "docs/research/data/eliot-tritext/lexicon/word-forms.tsv"
MAP_PATH = REPO_ROOT / "data/derivations/form-map.tsv"


def _lexicon_keys() -> set[str]:
    rows = LEXICON.read_text("utf-8").splitlines()
    assert rows[0].startswith("match_key")
    return {line.split("\t")[0] for line in rows[1:] if line}


def test_map_covers_lexicon_keys_1_to_1() -> None:
    map_keys = {
        line.split("\t")[0]
        for line in MAP_PATH.read_text("utf-8").splitlines()[len(MAP_HEADER.splitlines()):]
        if line and not line.startswith("#")
    }
    missing = _lexicon_keys() - map_keys
    extra = map_keys - _lexicon_keys()
    assert not missing and not extra, (
        f"missing={len(missing)} extra={len(extra)}"
    )


def test_map_build_deterministic() -> None:
    rebuilt = build_map(CORPUS_ROOT)
    assert rebuilt.strip() == MAP_PATH.read_text("utf-8").strip()
