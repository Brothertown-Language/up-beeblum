"""Regeneration-tool tests — up-beeblum#4. Smoke tier."""

import subprocess
from pathlib import Path

from up_beeblum.regenerate import main

FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "corpus"


def _run(out_editions: Path, out_manifests: Path) -> None:
    main(
        [
            "--corpus",
            str(FIXTURE_ROOT),
            "--editions-out",
            str(out_editions),
            "--manifests-out",
            str(out_manifests),
            "--pin-sha",
            "fixture-pin",
        ]
    )


def test_copy_emission_is_deterministic_and_laid_out(tmp_path: Path) -> None:  # SC-1
    """SC-1: two runs at the same pin produce byte-identical outputs."""
    first_ed, first_man = tmp_path / "run1-editions", tmp_path / "run1-manifests"
    second_ed, second_man = tmp_path / "run2-editions", tmp_path / "run2-manifests"
    _run(first_ed, first_man)
    _run(second_ed, second_man)
    diff = subprocess.run(
        ["diff", "-r", str(first_ed), str(second_ed)], check=False, capture_output=True, text=True
    )
    assert diff.returncode == 0, diff.stdout
    diff_man = subprocess.run(
        ["diff", "-r", str(first_man), str(second_man)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert diff_man.returncode == 0, diff_man.stdout
    # the fixed layout rule: data/editions/<edition>/<BOOK>/<column>.tsv
    copy = first_ed / "1663-first" / "GEN" / "orig.tsv"
    assert copy.exists() and copy.stat().st_size > 0


def _fixture_flags() -> dict[str, dict[str, str]]:
    """All fixture flag surfaces keyed by their rows' own book column,
    mirroring the tool's loader."""
    flags: dict[str, dict[str, str]] = {}
    base = FIXTURE_ROOT / "docs" / "research" / "data" / "eliot-tritext" / "sources" / "eliot1663"
    for path in sorted(base.glob("*_full.tsv")):
        lines = path.read_text("utf-8").splitlines()
        header = lines[0].split("\t")
        i_book, i_flag = header.index("book"), header.index("flag")
        i_verse = header.index("verse_id") if "verse_id" in header else None
        for line in lines[1:]:
            if not line:
                continue
            row = line.split("\t")
            key = (
                row[i_verse]
                if i_verse is not None
                else f"{row[i_book]} {row[header.index('chapter')]}:"
                + f"{row[header.index('verse')]}"
            )
            flags.setdefault(row[i_book], {})[key] = row[i_flag]
    return flags


_FIXTURE_FLAGS = _fixture_flags()


def _presence(store_col: str, verse_id: str, cell: str) -> str:
    """Presence-derived flag; the corpus flag surface overrides `orig`."""
    book_code = verse_id.split(" ", 1)[0]
    stated = _FIXTURE_FLAGS.get(book_code, {}).get(verse_id)
    if store_col == "eliot1663" and stated is not None:
        return stated  # the tool's override rule
    return "ok" if cell.strip() else "gap"


def _store_rows() -> tuple[list[str], list[list[str]]]:
    path = (
        FIXTURE_ROOT
        / "docs"
        / "research"
        / "data"
        / "eliot-tritext"
        / "alignment"
        / "alignment.tsv"
    )
    lines = path.read_text("utf-8").splitlines()
    header = lines[0].split("\t")
    return header, [line.split("\t") for line in lines[1:] if line]


def test_copies_match_spine_and_file_set(tmp_path: Path) -> None:
    """SC-4: emitted rows equal the store's rows; file set = books × columns."""
    out_ed, _out_man = tmp_path / "editions", tmp_path / "manifests"
    _run(out_ed, _out_man)
    header, rows = _store_rows()
    position = {name: index for index, name in enumerate(header)}
    books = []
    for row in rows:
        book = row[position["verse_id"]].split(" ", 1)[0]
        if book not in books:
            books.append(book)
    # per-row agreement: every emitted copy's rows match the store's column
    for edition, columns in (
        ("1663-first", {"orig": "eliot1663", "frame": "geneva1599", "web": "web"}),
    ):
        for book in books:
            book_rows = [r for r in rows if r[position["verse_id"]].startswith(book)]
            for copy_code, store_col in columns.items():
                emitted = (out_ed / edition / book / f"{copy_code}.tsv").read_text("utf-8")
                expected = "verse_id\tflag\ttext\n" + "".join(
                    f"{r[position['verse_id']]}\t"
                    f"{_presence(store_col, r[position['verse_id']], r[position[store_col]])}\t"
                    f"{r[position[store_col]]}\n"
                    for r in book_rows
                )
                assert emitted == expected, f"{edition}/{book}/{copy_code}"
    # file-set equality: exactly store books × supported columns for 1663
    expected_files = {
        out_ed / "1663-first" / book / f"{code}.tsv"
        for book in books
        for code in ("orig", "frame", "web")
    }
    actual_files = {p for p in (out_ed).glob("**/*.tsv") if p.is_relative_to(out_ed / "1663-first")}
    assert actual_files == expected_files
    # 1685-second: no column surface at the pin — no copies, nothing fabricated
    assert not (out_ed / "1685-second").exists()


def test_flags_populate_and_override(tmp_path: Path) -> None:
    """SC-3: flags populate for every row; corpus flag rows override."""
    out_ed, _out_man = tmp_path / "editions", tmp_path / "manifests"
    _run(out_ed, _out_man)
    vocabulary = {"ok", "uncertain", "gap"}
    for copy in (out_ed).glob("**/*.tsv"):
        for line in copy.read_text("utf-8").splitlines()[1:]:
            fields = line.split("\t")
            assert len(fields) == 3, copy
            assert fields[1] in vocabulary, f"{copy}:{fields[0]}"
            assert (fields[2] == "") == (fields[1] == "gap"), f"{copy}:{fields[0]}"
    # the corpus flag file's row overrides wherever it exists
    orig = (out_ed / "1663-first" / "GEN" / "orig.tsv").read_text("utf-8")
    gen_1_1 = next(line for line in orig.splitlines()[1:] if line.startswith("GEN 1:1\t"))
    assert gen_1_1.split("\t")[1] == "uncertain", gen_1_1
    # GEN 1:2's geneva cell is empty in the store -> gap
    frame = (out_ed / "1663-first" / "GEN" / "frame.tsv").read_text("utf-8")
    gen_1_2 = next(line for line in frame.splitlines()[1:] if line.startswith("GEN 1:2\t"))
    assert gen_1_2.split("\t")[1] == "gap", gen_1_2


def test_manifests_record_pin_fields(tmp_path: Path) -> None:
    """SC-2: every copy carries a manifest with the ROADMAP anchor fields."""
    out_ed, out_man = tmp_path / "editions", tmp_path / "manifests"
    _run(out_ed, out_man)
    for copy in (out_ed).glob("**/*.tsv"):
        book, column = copy.parent.name, copy.stem
        manifest = out_man / "1663-first" / book / f"{column}.json"
        import json

        record = json.loads(manifest.read_text("utf-8"))
        assert record["corpus_sha"] == "fixture-pin", manifest
        assert "derivation_data_version" in record
        assert record["derivation_data_version"] == "0"  # empty derivations store
    # a non-empty derivations store's VERSION file is recorded
    derivations = tmp_path / "derivations"
    derivations.mkdir()
    (derivations / "VERSION").write_text("42\n")
    out_ed2, out_man2 = tmp_path / "e2", tmp_path / "m2"
    main(
        [
            "--corpus",
            str(FIXTURE_ROOT),
            "--editions-out",
            str(out_ed2),
            "--manifests-out",
            str(out_man2),
            "--pin-sha",
            "fixture-pin",
            "--derivations-dir",
            str(derivations),
        ]
    )
    record = json.loads((out_man2 / "1663-first" / "GEN" / "orig.json").read_text())
    assert record["derivation_data_version"] == "42"


def test_pilot_layout_flag_surface_binds_to_store_code(tmp_path: Path) -> None:
    """R-3 regression: a pilot-layout surface (book/chapter/verse keys, no
    verse_id) whose filename stem diverges from the store's book code still
    carries its stated flags — no silent drop."""
    out_ed, out_man = tmp_path / "editions", tmp_path / "manifests"
    _run(out_ed, out_man)
    # the fixture's rut_full.tsv (pilot layout) states uncertain for both rows
    rut = (out_ed / "1663-first" / "RUT" / "orig.tsv").read_text("utf-8")
    assert all(line.split("\t")[1] == "uncertain" for line in rut.splitlines()[1:]), rut
