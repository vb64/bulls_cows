# coding: utf-8
"""
make test T=test_alice.test_new_session
"""
from tester_alice_skill_flask import Interface

from . import TestAlice


class TestNewSession(TestAlice):
    """
    Alice new session
    """
    def test_session(self):
        """
        new skill session
        """
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [Interface.Screen])
        self.assertTrue(alice.contain(self.start_message))
        self.assertTrue(alice.contain(self.prompt_message))
        self.assertFalse(alice.contain(self.help_message))
        self.assertEqual(len(alice.buttons), 2)
        self.db_sessions(1)

    def test_command(self):
        """
        new session with command
        """
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [Interface.Screen], command='xxx')
        self.assertTrue(alice.contain('xxx'))
        self.assertFalse(alice.contain(self.help_message))
        self.assertEqual(len(alice.buttons), 2)
        self.db_sessions(1)

        alice = self.skill.new_session('1234567891', [Interface.Screen], command="ПоМощь")
        self.assertTrue(alice.contain(self.help_message))
        self.assertTrue(alice.contain(self.start_message))
        self.assertTrue(alice.contain(self.prompt_message))
        self.assertEqual(len(alice.buttons), 2)
        self.db_sessions(2)

    def test_ping(self):
        """
        Alice ping
        """
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [Interface.Screen], command='ping')
        self.assertFalse(alice.contain(self.prompt_message))
        self.assertFalse(alice.contain(self.start_message))
        self.assertTrue(alice.contain('pong'))
        self.assertEqual(len(alice.buttons), 0)
        self.db_sessions(0)

    def test_no_screen(self):
        """
        no screen device
        """
        self.db_sessions(0)
        alice = self.skill.new_session('1234567890', [])
        self.assertTrue(alice.contain(self.prompt_message))
        self.assertFalse(alice.contain(self.help_message))
        self.assertEqual(len(alice.buttons), 0)
        self.db_sessions(1)

    def test_duplicate_session_id(self):
        """
        duplicate session id
        """
        from alice.models import SessionYA as Session

        session_id = "2eac4854-fce721f3-b845abba-{}".format(self.skill.sessions["current_id"])
        session = Session(id=session_id)
        session.attempts_count = 10
        session.put()

        self.db_sessions(1)
        self.skill.new_session('1234567890', [])
        self.db_sessions(1)
        self.assertEqual(session.attempts_count, 0)
        # print alice.dump().decode('utf-8')
