# coding: utf-8
"""Screen dialog without buttons.

make test T=test_default/test_alice/test_no_screen.py
"""
from . import TestAlice


class TestNoScreen(TestAlice):
    """Screen dialog without buttons."""

    def setUp(self):
        """With session."""
        super().setUp()
        self.alice = self.skill.new_session('1234567890', [])
        assert not self.alice.buttons

    def test_creator(self):
        """Creator mention."""
        self.alice.clear()
        self.alice.send("Меня зовут Юлька Богомолова!")

        assert self.alice.contain(self.creator_message)
        assert not self.alice.buttons

    def test_help(self):
        """Help command."""
        self.alice.clear()
        self.alice.send("помощь")

        assert self.alice.contain(self.help_message)
        assert not self.alice.buttons

    def test_cancel(self):
        """Cancel command."""
        self.alice.clear()
        self.alice.send("сдаюсь")

        assert self.alice.contain(self.stat_fail_message)
        assert not self.alice.buttons

        self.alice.clear()
        self.alice.send("да")
        assert self.alice.contain(self.again_message)
        assert self.alice.contain(self.start_message)

        self.alice.send("сдаюсь")

        self.alice.clear()
        self.alice.send("тру-ля-ля")
        assert self.alice.contain(self.dont_understand_message)
        assert self.alice.contain(self.stat_fail_message)

        self.alice.clear()
        self.alice.send("нет")
        assert not self.alice.contain(self.prompt_message)
        assert self.alice.contain(self.bye_message)

    def test_puzzle(self):
        """Solve puzzle."""
        self.db_sessions(1)

        from alice.models import SessionYA as Session
        session = Session.query().fetch(1)[0]

        self.alice.clear()
        self.alice.send("xxxx xxxx")
        assert self.alice.contain(self.dont_understand_message)
        assert self.alice.contain(self.prompt_message)

        self.alice.clear()
        self.alice.send("1234")
        assert self.alice.contain(self.cows_message)
        assert self.alice.contain(self.prompt_message)

        self.alice.clear()
        self.alice.send(session.puzzle)
        assert self.alice.contain(self.win_message)
        assert not self.alice.contain(self.prompt_message)
