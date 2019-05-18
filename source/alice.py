# coding: utf-8
"""
Yandex.Alice skill
"""
from models import Session
from bull_cows import BullCows


class Button:  # pylint: disable=too-few-public-methods,no-init,old-style-class
    """
    dialog buttons
    """
    CANCEL = "cancel"
    HELP = "help"
    AGAIN = "again"
    EXIT = "exit"


LABELS = {
  Button.CANCEL: "Сдаюсь",
  Button.HELP: "Помощь",
  Button.AGAIN: "Да",
  Button.EXIT: "Нет",
}

HELP_COMMANDS = ["помощь", "что ты умеешь"]
CANCEL_COMMANDS = ["сдаюсь", "надоело", "не знаю"]

HELP_MESSAGE = ''.join((
  "Этот навык умеет играть в логическую игру быки и коровы.", ' ',
  "Нужно отгадать число из четырех разных цифр.", ' ',
  "Навык будет сообщать число быков и коров в вашем ответе.", ' ',
  "Быки - сколько цифр в ответе находятся на правильном месте в загаданном числе.", ' ',
  "Коровы - сколько цифр в ответе есть в загаданном числе, но находятся на неверном месте.", ' ',
  "Игра закончится, когда вы угадаете четырех быков или ответите словом сдаюсь.", '\n\n',
))

START_MESSAGE = ''.join((
  "Я загадала число из четырех разных цифр.", ' ',
  "Тебе нужно его угадать.", '\n\n',
))

PROMPT_MESSAGE = "Продиктуй число из четырех разных цифр."
PROMPT_AGAIN = "Сыграем еще раз?"
ERROR_MESSAGE = "Ошибка. Попробуйте начать новую игру."


def remove_chars(text, chars):
    """
    remove chars from text
    """
    for char in chars:
        text = text.replace(char, '')

    return text


def normalize(text):
    """
    remove whitespaces, punctuation, cast to lower case
    """
    text = remove_chars(text, ',!?-')
    return ' '.join(text.lower().split())


def prompt(req, answer, prefix):
    """
    return prompt for Alice user
    """
    answer['text'] = prefix + PROMPT_MESSAGE
    if "screen" in req["meta"]["interfaces"]:
        answer['buttons'] = [
          {
            "title": LABELS[Button.CANCEL],
            "hide": True,
            "payload": {Button.CANCEL: True},
          },
          {
            "title": LABELS[Button.HELP],
            "hide": False,
            "payload": {Button.HELP: True},
          },
        ]

    return answer


def prompt_again(req, answer, prefix):
    """
    return prompt for Alice user
    """
    answer['text'] = prefix + PROMPT_AGAIN
    if "screen" in req["meta"]["interfaces"]:
        answer['buttons'] = [
          {
            "title": LABELS[Button.AGAIN],
            "hide": True,
            "payload": {Button.AGAIN: True},
          },
          {
            "title": LABELS[Button.EXIT],
            "hide": True,
            "payload": {Button.EXIT: True},
          },
        ]

    return answer


def handle_button(req, answer, session):
    """
    button pressed
    """
    payload = req['request']['payload']

    if Button.HELP in payload:
        return prompt(req, answer, HELP_MESSAGE)

    if Button.CANCEL in payload:
        return finish(req, answer, session)

    if Button.EXIT in payload:
        return exit_session(answer, session)

    if Button.AGAIN in payload:
        return new_game(req, answer, "Отлично, сыграем еще раз.", session)

    answer['text'] = ERROR_MESSAGE
    answer['end_session'] = True

    return answer


def finish(req, answer, session):
    """
    user cancel current game
    """
    session.is_game_over = True
    session.put()
    prefix = "Сделано {} попыток угадать число {}\n\n".format(session.attempts_count, session.puzzle)

    return prompt_again(req, answer, prefix)


def exit_session(answer, session):
    """
    Alice user exit session
    """
    session.key.delete()
    answer['text'] = "Возвращайся, поиграем еще."
    answer['end_session'] = True

    return answer


def new_game(req, answer, prefix, session):
    """
    start new game in session
    """
    session.is_game_over = False
    session.puzzle = BullCows().puzzle
    session.attempts_count = 0
    session.put()

    return prompt(req, answer, prefix + START_MESSAGE)


def new_session(req, answer):
    """
    alice user start new session
    """
    # get optional command for new session
    command = normalize(req['request'].get('command', ''))
    prefix = ""

    if command in ["ping"]:
        # Alice check for your skill availability
        answer['text'] = "pong"
        answer['end_session'] = True
        return answer

    if command:
        # handle on start commands
        if command in HELP_COMMANDS:
            prefix = HELP_MESSAGE

    session_id = req['session']['session_id']
    session = Session.get_by_id(session_id)
    if not session:
        session = Session(id=session_id)

    return new_game(req, answer, prefix, session)


def dialog(req):
    """
    alice request handler
    """
    answer = {"end_session": False}

    if req['session']['new']:
        return new_session(req, answer)

    session_id = req['session']['session_id']
    session = Session.get_by_id(session_id)
    if not session:
        # deleted session?
        answer['text'] = ERROR_MESSAGE
        answer['end_session'] = True
        return answer

    if req['request']['type'] == 'ButtonPressed':
        return handle_button(req, answer, session)

    text = normalize(req['request']['original_utterance'])
    if text in HELP_COMMANDS:
        return prompt(req, answer, HELP_MESSAGE)

    if text in CANCEL_COMMANDS:
        return finish(req, answer, session)

    return answer
