# coding: utf-8
"""
make test T=test_alice
"""
from tester_alice_skill_flask import Interface, Skill

from . import TestCase


class TestAlice(TestCase):
    """
    Alice skill 'bulls and cows'
    """
    start_message = "Я загадала число"
    help_message = "Этот навык умеет играть в логическую игру быки и коровы."
    prompt_message = "Продиктуй число из четырех разных цифр."

    def setUp(self):
        super(TestAlice, self).setUp()
        self.skill = Skill(self.app, 'xxx', '/alice')


class TestNewSession(TestAlice):
    """
    Alice new session
    """
    def test_session(self):
        """
        new skill session
        """
        alice = self.skill.new_session('1234567890', [Interface.Screen])
        self.assertTrue(alice.contain(self.start_message))
        self.assertTrue(alice.contain(self.prompt_message))
        self.assertFalse(alice.contain(self.help_message))

    def test_command(self):
        """
        new session with command
        """
        alice = self.skill.new_session('1234567890', [Interface.Screen], command='xxx')
        self.assertTrue(alice.contain('xxx'))
        self.assertFalse(alice.contain(self.help_message))

        alice = self.skill.new_session('1234567891', [Interface.Screen], command="ПоМощь")
        self.assertTrue(alice.contain(self.help_message))
        self.assertTrue(alice.contain(self.start_message))
        self.assertTrue(alice.contain(self.prompt_message))

    def test_ping(self):
        """
        Alice ping
        """
        alice = self.skill.new_session('1234567890', [Interface.Screen], command='ping')
        self.assertFalse(alice.contain(self.prompt_message))
        self.assertFalse(alice.contain(self.start_message))
        self.assertTrue(alice.contain('pong'))
        # print alice.dump().decode('utf-8')
