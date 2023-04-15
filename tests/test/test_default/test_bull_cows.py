"""Module bull_cows.py.

make test T=test_default/test_bull_cows.py
"""
from . import TestDefault


class TestCaseBullCows(TestDefault):
    """Test bull_cows."""

    def test_bull_cows(self):
        """Function bull_cows."""
        from bull_cows import BullCows, PUZZLE_LENGTH

        quest = BullCows()
        assert len(quest.puzzle) == PUZZLE_LENGTH

        quest = BullCows(puzzle='1234')
        assert quest.puzzle == '1234'

    def test_is_unique_chars(self):
        """Unique chars test."""
        from bull_cows import is_unique_chars

        assert is_unique_chars('1234')
        assert not is_unique_chars('1233')
        assert not is_unique_chars('3333')

    def test_check(self):
        """Method BullCows.check."""
        from bull_cows import BullCows

        quest = BullCows(puzzle='1234')

        is_valid, _err_text = quest.check('123456')
        assert is_valid is None

        is_valid, _err_text = quest.check('xxxx')
        assert is_valid is None

        is_valid, _err_text = quest.check('1333')
        assert is_valid is None

        cows, bulls = quest.check('5678')
        assert cows == 0
        assert bulls == 0

        cows, bulls = quest.check('4321')
        assert cows == 4
        assert bulls == 0

        cows, bulls = quest.check('1234')
        assert cows == 0
        assert bulls == 4

    def test_main(self):
        """Function main."""
        import bull_cows

        saved = bull_cows.get_input
        answers = ['1234', '']
        bull_cows.get_input = lambda i: answers.pop()

        bull_cows.main([], '1234')

        answers = ['1234', '']
        bull_cows.get_input = lambda i: answers.pop()
        bull_cows.main(['xxx', 'imcheater'], '1234')

        bull_cows.get_input = saved
