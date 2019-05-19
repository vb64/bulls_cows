# coding: utf-8
"""
testing Alice code
"""
from tester_alice_skill_flask import Skill
from .. import TestCase


class TestAlice(TestCase):
    """
    Alice skill 'bulls and cows'
    """
    start_message = "Я загадала число"
    help_message = "Этот навык умеет играть в логическую игру быки и коровы."
    prompt_message = "Продиктуй число из четырех разных цифр."
    stat_fail_message = "попыток угадать число"
    stat_fail_message = "Сыграем еще раз?"

    def setUp(self):
        super(TestAlice, self).setUp()
        self.skill = Skill(self.app, 'xxx', '/alice')

    def db_sessions(self, count):
        """
        new skill session
        """
        from alice.models import SessionYA as Session
        db_state = [
          (Session, count),
        ]
        self.check_db_tables(db_state)
