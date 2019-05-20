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
    prompt_message = "Введи число из четырех разных цифр."
    stat_fail_message = "попыток угадать число"
    stat_fail_message = "Сыграем еще раз?"
    bye_message = "Возвращайся,"
    err_message = "Ошибка. "
    again_message = "Отлично, сыграем еще раз"
    dont_understand_message = "Не понимаю ответ."
    cows_message = "Коров: "
    win_message = "Задача решена"
    creator_message = "которая научила меня этой игре"

    def setUp(self):
        super(TestAlice, self).setUp()
        self.skill = Skill(self.app, 'Your_Alice_Skill_ID', '/alice')

    def db_sessions(self, count):
        """
        new skill session
        """
        from alice.models import SessionYA as Session
        db_state = [
          (Session, count),
        ]
        self.check_db_tables(db_state)
