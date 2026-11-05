# Lab 6 — Code and Branch Coverage Analysis

**Name:** Kashvi Madhu
**SRN:** PES1UG24CS221
**Assigned task:** `L6_L7_34_tennis_scoring`

## Files

| File | Description |
|------|-------------|
| `tennis_scoring.py` | Module under test (unchanged, as given) |
| `test_tennis_scoring.py` | Starter test file as given (2 tests) |
| `CodeCoverageTest_PES1UG24CS221_tennis_scoring.py` | Test cases written for **line coverage** (19 tests) |
| `BranchCoverageTest_PES1UG24CS221_tennis_scoring.py` | Test cases written for **branch coverage** (31 tests) |
| `coverage_report_code.txt` | Terminal output — line coverage, before and after |
| `coverage_report_branch.txt` | Terminal output — branch coverage, before and after |

## How to run

```bash
pip install coverage pytest

# Line (code) coverage
coverage run -m pytest CodeCoverageTest_PES1UG24CS221_tennis_scoring.py
coverage report -m

# Branch coverage
coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS221_tennis_scoring.py
coverage report -m
```

## Results

| Run | Tests | Coverage of `tennis_scoring.py` |
|-----|-------|--------------------------------|
| Starter tests, line coverage | 2 | **37%** (24 of 38 statements missed) |
| Starter tests, branch coverage | 2 | **32%** (8 partial branches) |
| `CodeCoverageTest_...py`, line coverage | 19 | **100%** |
| `BranchCoverageTest_...py`, branch coverage | 31 | **100%** (30 of 30 branches) |

Both targets exceed the required 90%.

## Analysis — line coverage vs branch coverage

The starter file only called `game_score(0, 0)` and `set_winner(3, 2)`, so most of the
module never ran: every `game_score` decision past the `POINTS` lookup, all of
`match_status`, and the `ValueError` guard. Line coverage was 37%.

Writing one test per **outcome** of the module (`deuce`, `game A`/`game B`,
`advantage A`/`advantage B`, the `POINTS` string, the negative-points guard, each
`set_winner` result, each `match_status` result) walks every statement once and
takes line coverage to 100%.

Line coverage at 100% is not enough, which is exactly the point of the lab. Line
coverage only asks *"did this line run?"*; branch coverage asks *"did this decision
go both True and False?"*. The decisions that hide behind 100% line coverage here are
the ones where a `False` outcome falls straight through to a later `if`:

- `if a >= 3 and b >= 3:` — needs the False side from **both** directions,
  `game_score(3, 2)` (b below 3) and `game_score(2, 3)` (a below 3).
- `if a >= 6 and a - b >= 2:` in `set_winner` — False can mean "fewer than 6 games"
  (`set_winner(5, 5)`) or "6 games but only a one-game lead" (`set_winner(6, 5)`).
- `if sets_a == needed - 1 and sets_b == needed - 1:` — False when only one player is
  one set away (`match_status(0, 1, 3)`), not just when neither is.
- `if a < 0 or b < 0:` — both operands exercised, `game_score(-1, 2)` and
  `game_score(2, -3)`.

`BranchCoverageTest_PES1UG24CS221_tennis_scoring.py` labels each test with the
decision outcome it pins down, and also covers the boundary values (`3`, `6`, `7`
games, `best_of` 3 and 5) where off-by-one bugs would live. That is what moves the
module from 8 partially-taken branches to 30 of 30 branches covered.

## Screenshots

The two `coverage_report_*.txt` files hold the exact terminal output of the
before/after runs of each metric. The handout asks for screenshots of that terminal
output, so run the two commands above locally and save the screenshots in this folder
as `screenshot_code_coverage.png` and `screenshot_branch_coverage.png`.
