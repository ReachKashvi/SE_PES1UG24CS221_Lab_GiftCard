"""Lab 6 - Code (line) coverage test suite for tennis_scoring.py

PES1UG24CS221 - Kashvi Madhu
Repo task: L6_L7_34_tennis_scoring

Goal of this file: execute every executable line of tennis_scoring.py
at least once, i.e. >= 90% line coverage.

Run with:
    coverage run -m pytest CodeCoverageTest_PES1UG24CS221_tennis_scoring.py
    coverage report -m
"""

import pytest

from tennis_scoring import game_score, set_winner, match_status


# ---------------------------------------------------------------- game_score

def test_game_score_start_of_game():
    """Hits the final POINTS lookup line."""
    assert game_score(0, 0) == "0-0"


def test_game_score_mid_game_lookup():
    assert game_score(2, 1) == "30-15"


def test_game_score_negative_points_raise():
    """Hits the `raise ValueError` line."""
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_game_score_deuce():
    """a >= 3 and b >= 3 with a == b."""
    assert game_score(3, 3) == "deuce"


def test_game_score_two_point_lead_a():
    assert game_score(5, 3) == "game A"


def test_game_score_two_point_lead_b():
    assert game_score(3, 5) == "game B"


def test_game_score_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_game_score_advantage_b():
    assert game_score(3, 4) == "advantage B"


def test_game_score_straight_win_a():
    """a >= 4 while b is still below 3."""
    assert game_score(4, 0) == "game A"


def test_game_score_straight_win_b():
    assert game_score(0, 4) == "game B"


# --------------------------------------------------------------- set_winner

def test_set_winner_a_by_two_games():
    assert set_winner(6, 4) == "A"


def test_set_winner_b_by_two_games():
    assert set_winner(4, 6) == "B"


def test_set_winner_a_tiebreak():
    assert set_winner(7, 6) == "A"


def test_set_winner_b_tiebreak():
    assert set_winner(6, 7) == "B"


def test_set_winner_undecided():
    assert set_winner(3, 2) is None


# ------------------------------------------------------------- match_status

def test_match_status_a_wins_best_of_three():
    assert match_status(2, 0, 3) == "A wins"


def test_match_status_b_wins_best_of_three():
    assert match_status(0, 2, 3) == "B wins"


def test_match_status_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_status_in_progress():
    assert match_status(0, 0, 3) == "in progress"
