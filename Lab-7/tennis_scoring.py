"""Tennis scoring parsers - hardened after Lab 7 fuzz testing.

PES1UG24CS221 - Kashvi Madhu

Fuzzing the original version (kept as tennis_scoring_original.py) with
Hypothesis showed that all three parsers trusted their input and crashed with
whatever exception happened to come out of the internals: AttributeError on
None, KeyError on an unknown point name, ValueError from tuple unpacking.

The contract now is explicit: every parser either returns a well-formed result
or rejects the input with ValueError and a message naming the problem.
"""

POINT_NAMES = {'0': 0, '15': 1, '30': 2, '40': 3}


def _split_pair(text, example):
    """Validate `text` and split it into exactly two non-empty halves on '-'."""
    if not isinstance(text, str):
        raise ValueError(
            "score must be a string like '%s', got %s" % (example, type(text).__name__)
        )
    parts = text.split('-')
    if len(parts) != 2:
        raise ValueError(
            "score must have exactly two parts separated by '-' "
            "(e.g. '%s'), got %r" % (example, text)
        )
    first, second = parts[0].strip(), parts[1].strip()
    if not first or not second:
        raise ValueError("both sides of '-' must be filled in, got %r" % (text,))
    return first, second


def parse_score(text):
    """Parse 'A-B' point tallies into a pair of non-negative ints.

    >>> parse_score('3-2')
    (3, 2)

    Raises ValueError for anything else.
    """
    first, second = _split_pair(text, '3-2')
    try:
        a, b = int(first), int(second)
    except ValueError:
        raise ValueError(
            "both point tallies must be whole numbers, got %r" % (text,)
        )
    if a < 0 or b < 0:
        raise ValueError("point tallies cannot be negative, got %r" % (text,))
    return a, b


def game_lead(text):
    """Return how many points ahead player A is, from a game score like '40-30'.

    >>> game_lead('40-30')
    1

    Raises ValueError unless both sides are one of 0, 15, 30, 40.
    """
    first, second = _split_pair(text, '40-30')
    for name in (first, second):
        if name not in POINT_NAMES:
            raise ValueError(
                "%r is not a tennis point; expected one of %s"
                % (name, ", ".join(sorted(POINT_NAMES, key=POINT_NAMES.get)))
            )
    return POINT_NAMES[first] - POINT_NAMES[second]


def set_spread(games_csv):
    """Return max - min of a comma-separated list of games won per set.

    >>> set_spread('6,4,7')
    3

    Raises ValueError for empty input or any non-numeric / negative entry.
    """
    if not isinstance(games_csv, str):
        raise ValueError(
            "games must be a CSV string like '6,4,7', got %s"
            % (type(games_csv).__name__,)
        )
    fields = [field.strip() for field in games_csv.split(',')]
    if not any(fields):
        raise ValueError("no games given, expected something like '6,4,7'")
    games = []
    for field in fields:
        if not field:
            raise ValueError("empty entry in games list %r" % (games_csv,))
        try:
            value = int(field)
        except ValueError:
            raise ValueError(
                "games won must be whole numbers, got %r in %r" % (field, games_csv)
            )
        if value < 0:
            raise ValueError("games won cannot be negative, got %r" % (field,))
        games.append(value)
    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    print("Points A and B:", parse_score(user_input))

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    print("Lead in Points:", game_lead(user_input))

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    print("Spread:", set_spread(user_input))


if __name__ == "__main__":
    main()
