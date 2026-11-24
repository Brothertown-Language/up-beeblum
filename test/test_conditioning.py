# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Attested-paradigm instrument for the conditioned prefix system (up-beeblum#5,
SC-1 / R-1). Every asserted form is Fermino 2000's printed attestation
(book page noted); nothing is asserted that the source does not print. The
p.20 apun 12-sg row ('kutapun', a probable misprint flagged in the source
transcription) is excluded from the instrument accordingly."""

from __future__ import annotations

import pytest

from up_beeblum.conditioning import InflectionClass, inflect

# Fermino pp. 14-24 noun possession paradigms (attested rows, verbatim).
ATTESTED_NOUN_PARADIGMS: dict[str, tuple[InflectionClass, dict[str, str]]] = {
    # -uhkôt NId 'leg' — dependent vowel-initial NI stem (p.19)
    "uhkôt": (
        InflectionClass(NI=True, dependent=True, initial="vowel"),
        {
            "1": "nuhkôt",
            "2": "kuhkôt",
            "3": "wuhkôt",
            "1p": "nuhkôtun",
            "12": "kuhkôtun",
            "2p": "kuhkôtuw",
            "3p": "wuhkôtuw",
            "X": "muhkôt",
        },
    ),
    # -8sh NAd 'father' — 8-initial dependent NA stem (p.22)
    "8sh": (
        InflectionClass(NI=False, dependent=True, initial="8"),
        {
            "1": "n8sh",
            "2": "k8sh",
            "3": "8shah",
            "1p": "n8shun",
            "12": "k8shun",
            "2p": "k8shuw",
            "3p": "8shuwôwah",
        },
    ),
    # apun NI 'bed, table' — non-dependent vowel-initial NI, intrusive -t- (p.20)
    "apun": (
        InflectionClass(NI=True, dependent=False, initial="vowel"),
        {
            "1": "nutapun",
            "2": "kutapun",
            "3": "wutapun",
            "1p": "nutapunun",
            "2p": "kutapunuw",
            "3p": "wutapunuw",
        },
    ),
    # mush8n NI 'boat' — consonant-initial NI, full prefixes (p.21)
    "mush8n": (
        InflectionClass(NI=True, dependent=False, initial="consonant"),
        {
            "1": "numush8n",
            "2": "kumush8n",
            "3": "umush8n",
            "1p": "numush8nun",
            "12": "kumush8nun",
            "2p": "kumush8nuw",
            "3p": "umush8nuw",
        },
    ),
    # -m class: ahkee NI 'land' (p.24)
    "ahkee": (
        InflectionClass(NI=True, dependent=False, initial="vowel", pos_theme="m"),
        {
            "1": "nutahkeem",
            "2": "kutahkeem",
            "3": "wutahkeem",
            "1p": "nutahkeemun",
            "12": "kutahkeemun",
            "2p": "kutahkeemuw",
            "3p": "wutahkeemuw",
        },
    ),
    # -neechan NAd 'child' — consonant-initial NA (p.23-24)
    "-neechan": (
        InflectionClass(NI=False, dependent=True, initial="consonant"),
        {
            "1": "nuneechan",
            "2": "kuneechan",
            "3": "wuneechanah",
            "1p": "nuneechanun",
            "12": "kuneechanun",
            "2p": "kuneechanuw",
            "3p": "wuneechanuwôwah",
        },
    ),
}


@pytest.mark.parametrize("stem", sorted(ATTESTED_NOUN_PARADIGMS))
def test_fermino_noun_paradigm_rows(stem: str) -> None:
    cls, expected = ATTESTED_NOUN_PARADIGMS[stem]
    got = inflect(stem, cls)
    for slot, surface in expected.items():
        assert got[slot] == surface, f"{stem}[{slot}]: got {got[slot]!r}, attested {surface!r}"
