# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Text-copy regeneration tool — up-beeblum#4.

Reads the corpus exports-contract surfaces (the eliot-tritext alignment
store) at a recorded ``corpus/`` pin and regenerates the committed text
copies under ``data/editions/<edition>/<BOOK>/<column>.tsv``. Regeneration
is deterministic per pin: the same pin yields byte-identical output (
spine-ordered rows, UTF-8, no timestamps).

Column-set mapping per edition (the fixed layout; coverage-driven — a
column is emitted only when the corpus store's spine carries it at the
pin, nothing is fabricated): 1663-first = wlp/eliot1663/geneva1599/web;
1685-second = wlp/eliot-E2/kjv.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ELIOT_STORE_REL = Path("docs/research/data/eliot-tritext/alignment/alignment.tsv")
ELIOT_SOURCES_REL = Path("docs/research/data/eliot-tritext/sources/eliot1663")

# edition dir name -> column code -> corpus alignment-store column
EDITION_COLUMNS: dict[str, dict[str, str]] = {
    "1663-first": {
        "wlp": "wlp",
        "orig": "eliot1663",
        "frame": "geneva1599",
        "web": "web",
    },
    "1685-second": {
        "wlp": "wlp",
        "orig": "eliot-E2",
        "frame": "kjv",
    },
}

# Copy-row provenance vocabulary carried from the corpus's per-row flag surface.
FLAGS = ("ok", "uncertain", "gap")


def _read_tsv(path: Path) -> tuple[list[str], list[list[str]]]:
    """Read a header'd TSV without quoting (plain split on tabs)."""
    rows = [line.rstrip("\n").split("\t") for line in path.read_text("utf-8").splitlines() if line]
    return rows[0], rows[1:]


def _corpus_sha(corpus_root: Path, pin_sha: str | None) -> str:
    if pin_sha:
        return pin_sha
    result = subprocess.run(
        ["git", "-C", str(corpus_root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def regenerate(
    corpus_root: Path,
    editions_out: Path,
    manifests_out: Path | None = None,
    pin_sha: str | None = None,
    derivations_dir: Path | None = None,
) -> None:
    """Regenerate every spine-supported copy for the declared editions."""
    corpus_sha = _corpus_sha(corpus_root, pin_sha)  # the recorded pin anchors the run
    if manifests_out is not None:
        manifests_out.mkdir(parents=True, exist_ok=True)
    derivation_version = _derivation_version(derivations_dir)
    header, rows = _read_tsv(corpus_root / ELIOT_STORE_REL)
    position = {name: index for index, name in enumerate(header)}
    spine_column = position["verse_id"]
    flags = _load_flags(corpus_root)
    books: dict[str, list[list[str]]] = {}
    for row in rows:
        books.setdefault(_field(row, spine_column).split(" ", 1)[0], []).append(row)
    for edition, mapping in (
        ("1663-first", EDITION_COLUMNS["1663-first"]),
        ("1685-second", EDITION_COLUMNS["1685-second"]),
    ):
        for book, book_rows in books.items():
            book_flags: dict[str, dict[str, str]] = flags.get(book, {})
            for column_code, corpus_column in mapping.items():
                if corpus_column not in position:
                    continue  # coverage-driven: no spine support at this pin
                    # never fabricated — see module docstring
                # the per-book flag surface rows describe the Eliot (orig) text;
                # other columns take presence-derived flags only
                column_flags = book_flags if corpus_column == "eliot1663" else {}
                index = position[corpus_column]
                rows_out = [
                    (
                        _field(row, spine_column),
                        _derive_flag(
                            _field(row, index), column_flags.get(_field(row, spine_column))
                        ),
                        _field(row, index),
                    )
                    for row in book_rows
                ]
                target = editions_out / edition / book / f"{column_code}.tsv"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    "verse_id\tflag\ttext\n"
                    + "".join(f"{verse_id}\t{flag}\t{text}\n" for verse_id, flag, text in rows_out),
                    encoding="utf-8",
                )
                if manifests_out is not None:
                    _emit_manifest(
                        manifests_out,
                        edition,
                        book,
                        column_code,
                        corpus_sha,
                        derivation_version,
                        dict(sorted(Counter(flag for _, flag, _ in rows_out).items())),
                    )


def _load_flags(corpus_root: Path) -> dict[str, dict[str, dict[str, str]]]:
    """Per-book flag surfaces keyed by each surface's own ``book`` column —
    the rows' keys are canonical book codes; filename stems are not (the
    pilot surfaces' stems, e.g. ``matthew``, diverge from the store's codes).
    Pilot layouts without ``verse_id`` compose the spine key from
    ``<book> <chapter>:<verse>``."""
    flags_root = corpus_root / ELIOT_SOURCES_REL
    if not flags_root.is_dir():
        return {}
    flag_sets: dict[str, dict[str, dict[str, str]]] = {}
    for entry in sorted(flags_root.glob("*_full.tsv")):
        header, rows = _read_tsv(entry)
        index = {name: index for index, name in enumerate(header)}
        verse_key = index.get("verse_id")
        book_key = index["book"]
        for row in rows:
            key = (
                _field(row, verse_key)
                if verse_key is not None
                else f"{_field(row, book_key)} "
                + f"{_field(row, index['chapter'])}:{_field(row, index['verse'])}"
            )
            book = _field(row, book_key)
            flag_sets.setdefault(book, {}).setdefault(key, dict(zip(header, row)))
    return flag_sets


def _derive_flag(cell: str, flag_row: dict[str, str] | None) -> str:
    """The corpus flag surface's row overrides where it exists; otherwise
    presence-derived (text present -> ok, empty -> gap) — never fabricated."""
    if flag_row is not None:
        stated = flag_row.get("flag", "").strip()
        if stated in FLAGS:
            return stated
    return "ok" if cell.strip() else "gap"


def _derivation_version(derivations_dir: Path | None) -> str:
    if derivations_dir is None:
        return "0"
    version_file = derivations_dir / "VERSION"
    return version_file.read_text("utf-8").strip() if version_file.is_file() else "0"


def _emit_manifest(
    manifests_dir: Path,
    edition: str,
    book: str,
    column: str,
    corpus_sha: str,
    derivation_version: str,
    flag_tally: dict[str, int],
) -> None:
    """Per-copy build manifest — the ROADMAP anchor's two required fields
    (corpus SHA, derivation-data version) plus the copy's identification and
    flag totals; deterministic content, no timestamps."""
    manifest = {
        "corpus_sha": corpus_sha,
        "derivation_data_version": derivation_version,
        "edition": edition,
        "book": book,
        "column": column,
        "flag_tally": flag_tally,
    }
    target = manifests_dir / edition / book / f"{column}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(manifest, sort_keys=True) + "\n", encoding="utf-8")


def _field(row: list[str], position: int) -> str:
    return row[position] if position < len(row) else ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="up_beeblum.regenerate", description=__doc__)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--editions-out", type=Path, required=True)
    parser.add_argument("--manifests-out", type=Path, required=True)
    parser.add_argument("--pin-sha", default=None)
    parser.add_argument("--derivations-dir", type=Path, default=None)
    args = parser.parse_args(argv)
    regenerate(
        args.corpus,
        args.editions_out,
        args.manifests_out,
        args.pin_sha,
        args.derivations_dir,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
