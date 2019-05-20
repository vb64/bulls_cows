# coding: utf-8
"""
make test T=test_alice.test_no_screen
"""
from . import TestAlice


class TestNoScreen(TestAlice):
    """
    screen dialog without buttons
    """
    def setUp(self):
        super(TestNoScreen, self).setUp()
        self.alice = self.skill.new_session('1234567890', [])
        self.assertEqual(len(self.alice.buttons), 0)

    def test_creator(self):
        """
        creator mention
        """
        self.alice.clear()
        self.alice.send("Меня зовут Юлька Богомолова!")

        self.assertTrue(self.alice.contain(self.creator_message))
        self.assertEqual(len(self.alice.buttons), 0)

    def test_help(self):
        """
        help command
        """
        self.alice.clear()
        self.alice.send("помощь")

        self.assertTrue(self.alice.contain(self.help_message))
        self.assertEqual(len(self.alice.buttons), 0)

    def test_cancel(self):
        """
        cancel command
        """
        self.alice.clear()
        self.alice.send("сдаюсь")

        self.assertTrue(self.alice.contain(self.stat_fail_message))
        self.assertEqual(len(self.alice.buttons), 0)

        self.alice.clear()
        self.alice.send("да")
        self.assertTrue(self.alice.contain(self.again_message))
        self.assertTrue(self.alice.contain(self.start_message))

        self.alice.send("сдаюсь")

        self.alice.clear()
        self.alice.send("тру-ля-ля")
        self.assertTrue(self.alice.contain(self.dont_understand_message))
        self.assertTrue(self.alice.contain(self.stat_fail_message))

        self.alice.clear()
        self.alice.send("нет")
        self.assertFalse(self.alice.contain(self.prompt_message))
        self.assertTrue(self.alice.contain(self.bye_message))

    def test_puzzle(self):
        """
        solve puzzle
        """
        self.db_sessions(1)

        from alice.models import SessionYA as Session
        session = Session.query().fetch(1)[0]

        self.alice.clear()
        self.alice.send("xxxx xxxx")
        self.assertTrue(self.alice.contain(self.wrong_message))
        self.assertTrue(self.alice.contain(self.prompt_message))

        self.alice.clear()
        self.alice.send("1234")
        self.assertTrue(self.alice.contain(self.cows_message))
        self.assertTrue(self.alice.contain(self.prompt_message))

        self.alice.clear()
        self.alice.send(session.puzzle)
        self.assertTrue(self.alice.contain(self.win_message))
        self.assertFalse(self.alice.contain(self.prompt_message))
        # print self.alice.dump().decode('utf-8')
