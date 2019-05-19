"""
Yandex.Alice skill dialog functions
"""
from bull_cows import BullCows
from . import Button
from .models import SessionYA as Session
from .messages import (
  HELP_COMMANDS, CANCEL_COMMANDS, HELP, START, PROMPT, PROMPT_AGAIN, ERROR, AGAIN, STATS_CANCEL, BYE,
  LABEL_CANCEL, LABEL_HELP, LABEL_AGAIN, LABEL_EXIT,

)


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
    answer['text'] = prefix + PROMPT
    if "screen" in req["meta"]["interfaces"]:
        answer['buttons'] = [
          {
            "title": LABEL_CANCEL,
            "hide": True,
            "payload": {Button.CANCEL: True},
          },
          {
            "title": LABEL_HELP,
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
            "title": LABEL_AGAIN,
            "hide": True,
            "payload": {Button.AGAIN: True},
          },
          {
            "title": LABEL_EXIT,
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
        return prompt(req, answer, HELP)

    if Button.CANCEL in payload:
        return finish(req, answer, session)

    if Button.EXIT in payload:
        return exit_session(answer, session)

    if Button.AGAIN in payload:
        return new_game(req, answer, AGAIN, session)

    answer['text'] = ERROR
    answer['end_session'] = True

    return answer


def finish(req, answer, session):
    """
    user cancel current game
    """
    session.is_game_over = True
    session.put()
    prefix = STATS_CANCEL.format(session.attempts_count, session.puzzle)

    return prompt_again(req, answer, prefix)


def exit_session(answer, session):
    """
    Alice user exit session
    """
    session.key.delete()
    answer['text'] = BYE
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

    return prompt(req, answer, prefix + START)


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
            prefix = HELP

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
        answer['text'] = ERROR
        answer['end_session'] = True
        return answer

    if req['request']['type'] == 'ButtonPressed':
        return handle_button(req, answer, session)

    text = normalize(req['request']['original_utterance'])
    if text in HELP_COMMANDS:
        return prompt(req, answer, HELP)

    if text in CANCEL_COMMANDS:
        return finish(req, answer, session)

    return answer
