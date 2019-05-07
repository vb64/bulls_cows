"""
Bull&Cows game
"""
import random

PUZZLE_LENGTH = 4


def make_puzzle():
    """
    return random string from 4 different digits
    """
    puzzle = ''
    while len(puzzle) < PUZZLE_LENGTH:
        digit = str(int(random.random() * 10))
        if digit not in puzzle:  # pragma: no cover
            puzzle = puzzle + digit

    return puzzle


def is_unique_chars(text):
    """
    return True, if text consist from unique chars
    """
    for i in range(len(text) - 1):
        if text[i] in text[i + 1:]:
            return False

    return True


def is_valid(text):
    """
    return True, if user input follow formal criteria
    """
    if len(text) != PUZZLE_LENGTH:
        return False

    try:
        int(text)
    except ValueError:
        return False

    if not is_unique_chars(text):
        return False

    return True


class BullCows(object):  # pylint: disable=too-few-public-methods
    """
    Bull&Cows quest
    """
    def __init__(self, puzzle=None):
        self.try_count = 0
        self.puzzle = puzzle
        if self.puzzle is None:
            self.puzzle = make_puzzle()

    def check(self, answer):
        """
        check answer string for cows and bulls
        """
        if not is_valid(answer):
            return (None, 'need {} different digits!'.format(PUZZLE_LENGTH))

        position, cows, bulls = 0, 0, 0
        for digit in answer:
            if digit in self.puzzle:
                if position == self.puzzle.index(digit):
                    bulls += 1
                else:
                    cows += 1

            position += 1

        return (cows, bulls)


def main(puzzle=None):
    """
    entry point
    """
    quest = BullCows(puzzle=puzzle)
    cows, bulls = None, None

    while bulls != PUZZLE_LENGTH:
        cows, bulls = quest.check(raw_input('enter 4 digits:'))
        if cows is None:
            print bulls  # bulls contain error description
        else:
            print 'cows:', cows, 'bulls:', bulls

    print 'Done!'
    print 'Quest solved with {} tries'.format(quest.try_count)


if __name__ == "__main__":  # pragma: no cover
    main()
