"""Lab 6 - Branch coverage test suite for tennis_scoring.py

PES1UG24CS221 - Kashvi Madhu
Repo task: L6_L7_34_tennis_scoring

Goal of this file: force every decision in tennis_scoring.py to evaluate
to BOTH True and False, i.e. >= 90% branch coverage. Each test below is
labelled with the decision outcome it pins down.

Run with:
    coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS221_tennis_scoring.py
    coverage report -m
"""

import pytest

from tennis_scoring import game_score, set_winner, match_status


# ---------------------------------------------------------------- game_score
# Decisions:
#   D1  a < 0 or b < 0
#   D2  a >= 3 and b >= 3
#   D3  a == b
#   D4  a - b >= 2
#   D5  b - a >= 2
#   D6  a > b
#   D7  a >= 4
#   D8  b >= 4

def test_negative_a_raises():
    """D1 True (left operand)."""
    with pytest.raises(ValueError):
        game_score(-1, 2)


def test_negative_b_raises():
    """D1 True (right operand)."""
    with pytest.raises(ValueError):
        game_score(2, -3)


def test_both_negative_raises():
    """D1 True with both operands negative."""
    with pytest.raises(ValueError):
        game_score(-2, -2)


def test_love_all_is_points_string():
    """D1 False, D2 False, D7 False, D8 False -> POINTS lookup."""
    assert game_score(0, 0) == "0-0"


def test_thirty_fifteen_is_points_string():
    """D2 False via b < 3 -> POINTS lookup."""
    assert game_score(2, 1) == "30-15"


def test_forty_thirty_is_points_string():
    """D2 False via b < 3 while a == 3 (boundary on a)."""
    assert game_score(3, 2) == "40-30"


def test_thirty_forty_is_points_string():
    """D2 False via a < 3 while b == 3 (boundary on b)."""
    assert game_score(2, 3) == "30-40"


def test_deuce_at_three_three():
    """D2 True, D3 True."""
    assert game_score(3, 3) == "deuce"


def test_deuce_after_long_rally():
    """D2 True, D3 True at higher equal scores."""
    assert game_score(6, 6) == "deuce"


def test_game_a_from_advantage():
    """D2 True, D3 False, D4 True."""
    assert game_score(5, 3) == "game A"


def test_game_b_from_advantage():
    """D2 True, D3 False, D4 False, D5 True."""
    assert game_score(3, 5) == "game B"


def test_advantage_a():
    """D2 True, D3/D4/D5 False, D6 True."""
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    """D2 True, D3/D4/D5 False, D6 False -> else branch."""
    assert game_score(3, 4) == "advantage B"


def test_game_a_without_deuce():
    """D2 False, D7 True."""
    assert game_score(4, 1) == "game A"


def test_game_b_without_deuce():
    """D2 False, D7 False, D8 True."""
    assert game_score(1, 4) == "game B"


# --------------------------------------------------------------- set_winner
# Decisions:
#   D1  a >= 6 and a - b >= 2
#   D2  b >= 6 and b - a >= 2
#   D3  a == 7 and b == 6
#   D4  b == 7 and a == 6

def test_set_a_wins_six_four():
    """D1 True."""
    assert set_winner(6, 4) == "A"


def test_set_a_wins_seven_five():
    """D1 True above six games."""
    assert set_winner(7, 5) == "A"


def test_set_b_wins_four_six():
    """D1 False, D2 True."""
    assert set_winner(4, 6) == "B"


def test_set_a_wins_tiebreak():
    """D1 False (lead of one), D2 False, D3 True."""
    assert set_winner(7, 6) == "A"


def test_set_b_wins_tiebreak():
    """D1/D2/D3 False, D4 True."""
    assert set_winner(6, 7) == "B"


def test_set_not_over_at_six_five():
    """D1 False via lead, D2 False via games, D3/D4 False -> None."""
    assert set_winner(6, 5) is None


def test_set_not_over_early():
    """All decisions False with both players below six."""
    assert set_winner(3, 2) is None


def test_set_not_over_at_five_five():
    """D1 False via a < 6, D2 False via b < 6 -> None."""
    assert set_winner(5, 5) is None


# ------------------------------------------------------------- match_status
# Decisions:
#   D1  sets_a == needed
#   D2  sets_b == needed
#   D3  sets_a == needed - 1 and sets_b == needed - 1

def test_match_a_wins_best_of_three():
    """D1 True (needed == 2)."""
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins_best_of_three():
    """D1 False, D2 True."""
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider_best_of_three():
    """D1/D2 False, D3 True."""
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress_best_of_three():
    """D1/D2 False, D3 False (both sides) -> in progress."""
    assert match_status(1, 0, 3) == "in progress"


def test_match_in_progress_one_side_only():
    """D3 False because only sets_b is at needed - 1."""
    assert match_status(0, 1, 3) == "in progress"


def test_match_a_wins_best_of_five():
    """D1 True with needed == 3."""
    assert match_status(3, 1, 5) == "A wins"


def test_match_decider_best_of_five():
    """D3 True with needed == 3."""
    assert match_status(2, 2, 5) == "decider"


def test_match_in_progress_best_of_five():
    """All decisions False with needed == 3."""
    assert match_status(1, 2, 5) == "in progress"
