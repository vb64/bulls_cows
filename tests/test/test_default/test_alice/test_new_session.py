# coding: utf-8
"""New Alice session.

make test T=test_alice/test_new_session.py
"""
from tester_alice_skill_flask import Interface

from . import TestAlice


class TestNewSession(TestAlice):
    """Alice new session."""

    def test_session(self):
        """New skill session."""
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [Interface.Screen])
        assert alice.contain(self.start_message)
        assert alice.contain(self.prompt_message)
        assert not alice.contain(self.help_message)
        assert len(alice.buttons) == 2
        self.db_sessions(1)

    def test_command(self):
        """New session with command."""
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [Interface.Screen], command='xxx')
        assert alice.contain('xxx')
        assert not alice.contain(self.help_message)
        assert len(alice.buttons) == 2
        self.db_sessions(1)

        alice = self.skill.new_session('1234567891', [Interface.Screen], command="ПоМощь")
        assert alice.contain(self.help_message)
        assert alice.contain(self.start_message)
        assert alice.contain(self.prompt_message)
        assert len(alice.buttons) == 2
        self.db_sessions(2)

    def test_ping(self):
        """Alice ping."""
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [Interface.Screen], command='ping')
        assert not alice.contain(self.prompt_message)
        assert not alice.contain(self.start_message)
        assert alice.contain('pong')
        assert not alice.buttons
        self.db_sessions(0)

    def test_no_screen(self):
        """No screen device."""
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [])
        assert alice.contain(self.prompt_message)
        assert not alice.contain(self.help_message)
        assert not alice.buttons
        self.db_sessions(1)

    def test_duplicate_session_id(self):
        """Duplicate session id."""
        from alice.models import SessionYA as Session

        session_id = "2eac4854-fce721f3-b845abba-{}".format(self.skill.sessions["current_id"])
        session = Session(id=session_id)
        session.attempts_count = 10
        session.put()

        self.db_sessions(1)
        self.skill.new_session('1234567890', [])
        self.db_sessions(1)
        assert not session.attempts_count
        # print alice.dump().decode('utf-8')
