# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Goddard-1981 attested third-person instrument (up-beeblum#5, SC-4 / R-4).

Every asserted form is Goddard 1981's printed attestation, quoted from the
corpus's proofed phonology lines at pin bf3750158 (line refs noted). The
uhpeteog/wuhpeteog pair is attested by Goddard as mutual spellings of 'his
rib' — the table's rule emits both variant spellings and the instrument asserts
the pair exactly.
"""

from __future__ import annotations

from up_beeblum.conditioning import InflectionClass, inflect, third_person_forms


# g63.36-37 (§15): uhquan 'hook' < PA *wečkwa·ni — stem /hC/-cluster realisation.
def test_uhquan() -> None:
    cls = InflectionClass(NI=True, dependent=False, initial="hC")
    forms = third_person_forms("hquan", cls)
    assert "uhquan" in forms

# 62.1-2 (C 12): wuhpit 'his arm'; wuhpeteog, uhpeteog 'his rib'.
def test_wuhpit() -> None:
    cls = InflectionClass(NI=True, dependent=False, initial="hC")
    assert "wuhpit" in third_person_forms("hpit", cls)

def test_rib_variant_pair() -> None:
    cls = InflectionClass(NI=True, dependent=False, initial="hC")
    forms = third_person_forms("hpeteog", cls)
    assert {"wuhpeteog", "uhpeteog"} <= forms

# 62.1 (C 12): wuhkontash 'his legs' — prefix w- over the dependent u-initial
# stem uhkont (Fermino p.19 conditioning), plural-object -ash.
def test_wuhkontash() -> None:
    cls = InflectionClass(NI=True, dependent=True, initial="vowel")
    assert inflect("uhkont", cls, slots=("3",), pl_obj=True) == {"3": "wuhkontash"}

# 60.12 (§11): wék, week 'his house' < PA *wi·ki — PA *w > Mass /w/, written
# (w, u): the dependent vowel-initial prefix vowel-loss (w-) plus stem ék.
def test_wek() -> None:
    cls = InflectionClass(NI=True, dependent=True, initial="vowel")
    assert inflect("ék", cls, slots=("3",)) == {"3": "wék"}
