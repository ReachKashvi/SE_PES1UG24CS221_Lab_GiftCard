# Lab 7 — Fuzz Testing

**Name:** Kashvi Madhu
**SRN:** PES1UG24CS221
**Assigned task:** `L6_L7_34_tennis_scoring`

## Files

| File | Description |
|------|-------------|
| `tennis_scoring_original.py` | The module exactly as given (kept for comparison) |
| `tennis_scoring.py` | Hardened module after the fuzzing findings were fixed |
| `FuzzTest_PES1UG24CS221_tennis_scoring.py` | Hypothesis fuzz suite + regression tests (25 tests) |
| `fuzz_before.txt` | Terminal output — fuzz suite against the original module (9 failures) |
| `fuzz_after.txt` | Terminal output — same suite against the hardened module (25 passed) |
| `starter_test_reference.py.txt` | The starter test stubs as given (incomplete function bodies) |

## How to run

```bash
pip install hypothesis pytest

pytest FuzzTest_PES1UG24CS221_tennis_scoring.py -v
```

## The property being fuzzed

The three functions all parse untrusted text. The property asserted is a
robustness contract: for **any** input, each function must either

1. return a well-formed result (a pair of non-negative ints, or an int), or
2. reject the input with `ValueError`.

Any other exception means unvalidated input reached the internals and crashed
there. Hypothesis generates arbitrary text, `None`, and score-shaped near-misses
(`st.from_regex`, digit/comma alphabets) to search for those inputs.

## Results

| Run | Outcome |
|-----|---------|
| Fuzz suite vs `tennis_scoring_original.py` | **9 failed, 16 passed** — 6 distinct crash classes |
| Fuzz suite vs `tennis_scoring.py` (after fixes) | **25 passed** |

## Bugs found by fuzzing

| # | Function | Minimal input Hypothesis found | Crash | Cause |
|---|----------|-------------------------------|-------|-------|
| 1 | `parse_score` | `None` | `AttributeError: 'NoneType' object has no attribute 'split'` | No type check before `.split()` |
| 2 | `parse_score` | `''`, `'6'`, `'6-4-2'` | `ValueError: not enough / too many values to unpack` | `a, b = text.split('-')` assumes exactly two parts |
| 3 | `parse_score` | `'six-four'`, `'-3-2'` | `ValueError: invalid literal for int()` | `int()` called on unvalidated text; no negative-score check |
| 4 | `game_lead` | `'-'`, `'45-30'`, `'40-20'`, `'AD-40'` | `KeyError: ''` / `'45'` / `'20'` / `'AD'` | Dict lookup on a point name that was never validated |
| 5 | `game_lead` | `None`, `'40'`, `'40-30-15'` | `AttributeError`, `ValueError` on unpack | Same two problems as 1 and 2 |
| 6 | `set_spread` | `None`, `''`, `'6,,4'`, `'6, four'`, `','` | `AttributeError`, `ValueError: invalid literal for int()` | No type check, empty fields and non-numeric fields both reach `int()` |

Note on #2, #3 and #6: `ValueError` is the exception type the contract allows, but
the original raised it *by accident* from tuple unpacking and `int()`, with
messages like `not enough values to unpack (expected 2, got 1)` that tell the
caller nothing about tennis scores. The fix makes the rejection deliberate and
the message useful.

## Fixes applied in `tennis_scoring.py`

- Added a shared `_split_pair()` helper that type-checks the input, requires
  exactly two `-`-separated parts, and requires both sides to be non-empty —
  this closes bugs 1, 2 and 5 for both `parse_score` and `game_lead`.
- `parse_score`: `int()` conversion wrapped, raising a `ValueError` that names the
  offending input; negative tallies rejected explicitly (bug 3).
- `game_lead`: both point names validated against `POINT_NAMES` before the dict
  lookup, with an error listing the legal values (bug 4).
- `set_spread`: type-checked, empty input rejected, every field checked for
  emptiness, numeric form and non-negativity before `max`/`min` (bug 6).
- Every rejection path now raises `ValueError` with a message naming the bad
  value, so the caller can report the problem instead of guessing.
- `main()` kept, so the interactive demo still works.

The crashing inputs are kept as `@pytest.mark.parametrize` regression tests at the
bottom of the fuzz file, so these bugs cannot come back silently.

## Screenshots

`fuzz_before.txt` and `fuzz_after.txt` hold the exact terminal output of the
before/after runs. For screenshot deliverables, run the command above locally and
save them here as `screenshot_fuzz_before.png` and `screenshot_fuzz_after.png`.
