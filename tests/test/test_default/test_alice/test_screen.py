"""Screen dialog.

make test T=test_default/test_alice/test_screen.py
"""
from tester_alice_skill_flask import Interface
from . import TestAlice


class TestScreen(TestAlice):
    """Screen dialog with buttons."""

    def setUp(self):
        """With Alice session."""
        super().setUp()
        self.alice = self.skill.new_session('1234567890', [Interface.Screen])
        assert len(self.alice.buttons) == 2

    def test_help(self):
        """Help button."""
        self.alice.clear()
        self.alice.send_button(1)

        assert not self.alice.contain(self.start_message)
        assert self.alice.contain(self.prompt_message)
        assert self.alice.contain(self.help_message)
        assert len(self.alice.buttons) == 2

    def test_cancel(self):
        """Cancel button."""
        self.alice.clear()
        self.alice.send_button(0)

        assert not self.alice.contain(self.start_message)
        assert not self.alice.contain(self.prompt_message)
        assert not self.alice.contain(self.help_message)

        assert self.alice.contain(self.stat_fail_message)
        assert self.alice.contain(self.stat_fail_message)
        assert len(self.alice.buttons) == 2

        self.alice.send_button(0)
        self.alice.send_button(0)
        self.alice.clear()
        self.alice.send_button(1)

        assert not self.alice.contain(self.prompt_message)
        assert self.alice.contain(self.bye_message)
        assert len(self.alice.buttons) == 1
