"""Lab 7 - Fuzz testing of tennis_scoring.py with Hypothesis

PES1UG24CS221 - Kashvi Madhu
Repo task: L6_L7_34_tennis_scoring

Contract being fuzzed
---------------------
Each of the three parsers takes untrusted text. For ANY input, a parser must
either

  * return a well-formed result (a pair of ints / an int), or
  * reject the input with ValueError.

Any other exception (AttributeError, KeyError, TypeError, IndexError, ...) is a
crash: it means bad input escaped validation and blew up deep inside the
function. Those are the bugs this suite hunts for.

Run with:
    pip install hypothesis pytest
    pytest FuzzTest_PES1UG24CS221_tennis_scoring.py -v
"""

import pytest
from hypothesis import given, settings, strategies as st

from tennis_scoring import parse_score, game_lead, set_spread

# Inputs a user could realistically type, plus pure noise.
SCORE_TEXT = st.one_of(
    st.text(),
    st.none(),
    st.text(alphabet="0123456789-, ", max_size=12),
    st.from_regex(r"\A-?\d{0,4}--?\d{0,4}\Z", fullmatch=True),
)
CSV_TEXT = st.one_of(
    st.text(),
    st.none(),
    st.text(alphabet="0123456789, -", max_size=16),
    st.lists(st.integers(min_value=-50, max_value=50), max_size=6).map(
        lambda xs: ",".join(str(x) for x in xs)
    ),
)


# ------------------------------------------------------- fuzz: no hard crash

@settings(max_examples=500)
@given(SCORE_TEXT)
def test_parse_score_no_crash(s):
    try:
        result = parse_score(s)
    except ValueError:
        return  # rejecting bad input is correct behaviour
    a, b = result
    assert isinstance(a, int) and isinstance(b, int)
    assert a >= 0 and b >= 0


@settings(max_examples=500)
@given(SCORE_TEXT)
def test_game_lead_no_crash(s):
    try:
        lead = game_lead(s)
    except ValueError:
        return
    assert isinstance(lead, int)
    assert -3 <= lead <= 3


@settings(max_examples=500)
@given(CSV_TEXT)
def test_set_spread_no_crash(s):
    try:
        spread = set_spread(s)
    except ValueError:
        return
    assert isinstance(spread, int)
    assert spread >= 0


# ------------------------------------------- fuzz: valid input still correct

@given(st.integers(min_value=0, max_value=99), st.integers(min_value=0, max_value=99))
def test_parse_score_roundtrip(a, b):
    assert parse_score("%d-%d" % (a, b)) == (a, b)


@given(st.sampled_from(["0", "15", "30", "40"]), st.sampled_from(["0", "15", "30", "40"]))
def test_game_lead_matches_point_index(first, second):
    index = {"0": 0, "15": 1, "30": 2, "40": 3}
    assert game_lead(first + "-" + second) == index[first] - index[second]


@given(st.lists(st.integers(min_value=0, max_value=7), min_size=1, max_size=5))
def test_set_spread_matches_max_minus_min(games):
    csv = ",".join(str(g) for g in games)
    assert set_spread(csv) == max(games) - min(games)


# --------------------------------------- regression tests for crashes found
# Each input below crashed the original code with something other than
# ValueError. They are kept as plain tests so the fixes stay fixed.

CRASHERS_PARSE_SCORE = [
    None,        # AttributeError: 'NoneType' object has no attribute 'split'
    "",          # ValueError on unpack - now a clean, deliberate ValueError
    "6",         # ValueError: not enough values to unpack
    "6-4-2",     # ValueError: too many values to unpack
    "six-four",  # ValueError: invalid literal for int()
    "-3-2",      # ambiguous minus sign
    " ",
]

CRASHERS_GAME_LEAD = [
    None,        # AttributeError
    "",          # ValueError on unpack
    "40",        # ValueError on unpack
    "40-30-15",  # ValueError on unpack
    "45-30",     # KeyError: '45'
    "40-20",     # KeyError: '20'
    "AD-40",     # KeyError: 'AD'
]

CRASHERS_SET_SPREAD = [
    None,        # AttributeError
    "",          # ValueError: invalid literal for int(): ''
    "6,,4",      # ValueError: invalid literal for int(): ''
    "6, four",   # ValueError: invalid literal for int()
    ",",
]


@pytest.mark.parametrize("bad", CRASHERS_PARSE_SCORE)
def test_parse_score_rejects_cleanly(bad):
    with pytest.raises(ValueError):
        parse_score(bad)


@pytest.mark.parametrize("bad", CRASHERS_GAME_LEAD)
def test_game_lead_rejects_cleanly(bad):
    with pytest.raises(ValueError):
        game_lead(bad)


@pytest.mark.parametrize("bad", CRASHERS_SET_SPREAD)
def test_set_spread_rejects_cleanly(bad):
    with pytest.raises(ValueError):
        set_spread(bad)
