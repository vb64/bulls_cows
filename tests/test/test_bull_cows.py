"""
make test T=test_bull_cows
"""

from . import TestCase


class TestCaseBullCows(TestCase):
    """
    bull_cows
    """
    def test_bull_cows(self):
        """
        bull_cows
        """
        from bull_cows import BullCows, PUZZLE_LENGTH

        quest = BullCows()
        self.assertEqual(len(quest.puzzle), PUZZLE_LENGTH)

        quest = BullCows(puzzle='1234')
        self.assertEqual(quest.puzzle, '1234')

    def test_is_unique_chars(self):
        """
        bull_cows
        """
        from bull_cows import is_unique_chars

        self.assertTrue(is_unique_chars('1234'))
        self.assertFalse(is_unique_chars('1233'))
        self.assertFalse(is_unique_chars('3333'))

    def test_check(self):
        """
        BullCows.check
        """
        from bull_cows import BullCows

        quest = BullCows(puzzle='1234')

        is_valid, err_text = quest.check('123456')
        self.assertEqual(is_valid, None)

        is_valid, err_text = quest.check('xxxx')
        self.assertEqual(is_valid, None)

        is_valid, err_text = quest.check('1333')
        self.assertEqual(is_valid, None)

        cows, bulls = quest.check('5678')
        self.assertEqual(cows, 0)
        self.assertEqual(bulls, 0)

        cows, bulls = quest.check('4321')
        self.assertEqual(cows, 4)
        self.assertEqual(bulls, 0)

        cows, bulls = quest.check('1234')
        self.assertEqual(cows, 0)
        self.assertEqual(bulls, 4)
