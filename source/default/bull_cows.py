"""Bull&Cows game."""
import sys
import random

PUZZLE_LENGTH = 4


def make_puzzle():
    """Return random string from 4 different digits."""
    puzzle = []
    while len(puzzle) < PUZZLE_LENGTH:
        digit = str(random.choice(range(10)))
        if digit not in puzzle:  # pragma: no cover
            puzzle.append(digit)

    return ''.join(puzzle)


def is_unique_chars(text):
    """Return True, if text consist from unique chars."""
    for i in range(len(text) - 1):
        if text[i] in text[i + 1:]:
            return False

    return True


def is_valid(text):
    """Return True, if user input follow formal criteria."""
    if len(text) != PUZZLE_LENGTH:
        return False

    try:
        int(text)
    except ValueError:
        return False

    if not is_unique_chars(text):
        return False

    return True


class BullCows:
    """Bull&Cows quest."""

    def __init__(self, puzzle=None):
        """Can use predefined puzzle."""
        self.try_count = 0
        self.puzzle = puzzle
        if self.puzzle is None:
            self.puzzle = make_puzzle()

    def check(self, answer):
        """Check answer string for cows and bulls."""
        if not is_valid(answer):
            return (None, None)

        self.try_count += 1
        position, cows, bulls = 0, 0, 0
        for digit in answer:
            if digit in self.puzzle:
                if position == self.puzzle.index(digit):
                    bulls += 1
                else:
                    cows += 1

            position += 1

        return (cows, bulls)


def main(argv, puzzle=None):
    """Standalone app."""
    quest = BullCows(puzzle=puzzle)
    cows, bulls = None, None
    if (len(argv) > 1) and (argv[1] == 'imcheater'):
        print("my puzzle:", quest.puzzle)

    while bulls != PUZZLE_LENGTH:
        cows, bulls = quest.check(input('enter 4 digits:'))
        if cows is None:
            print('need {} different digits!'.format(PUZZLE_LENGTH))
        else:
            print('cows:', cows, 'bulls:', bulls)

    print('Done!')
    print('Quest solved with {} tries'.format(quest.try_count))


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv)
