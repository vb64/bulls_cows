"""
Yandex.Alice skill dialog functions
"""
from bull_cows import BullCows, PUZZLE_LENGTH
from .models import SessionYA as Session
from .messages import (
  HELP_COMMANDS, CANCEL_COMMANDS, AGAIN_COMMANDS, EXIT_COMMANDS,
  HELP, START, PROMPT, PROMPT_AGAIN, ERROR, AGAIN, STATS_CANCEL, BYE,
  DONT_UNDERSTAND, VICTORY, BULLS_COWS, BULLS_COWS_TTS, JULY, BOGOMOLOVA, CREATOR,
  LABEL_CANCEL, LABEL_HELP, LABEL_AGAIN, LABEL_EXIT, LABEL_LIKE,
)

LANDING = "https://dialogs.yandex.ru/store/skills/44617ce2-bychki-i-korovk"


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
    return ' '.join(text.lower().split()).encode('utf8')


def prompt(req, answer, prefix, tts=None):
    """
    return prompt for Alice user
    """
    answer['text'] = prefix + PROMPT
    if tts:
        answer['tts'] = tts

    if "screen" in req["meta"]["interfaces"]:
        answer['buttons'] = [
          {
            "title": LABEL_CANCEL,
            "hide": True,
          },
          {
            "title": LABEL_HELP,
            "hide": False,
          },
        ]

    return answer


def prompt_again(req, answer, prefix, tts=None):
    """
    return prompt for new game
    """
    if tts:
        answer['tts'] = tts
    answer['text'] = prefix + PROMPT_AGAIN

    if "screen" in req["meta"]["interfaces"]:
        answer['buttons'] = [
          {
            "title": LABEL_AGAIN,
            "hide": True,
          },
          {
            "title": LABEL_EXIT,
            "hide": True,
          },
        ]

    return answer


def finish(req, answer, session):
    """
    user cancel current game
    """
    session.is_game_over = True
    session.put()
    prefix = STATS_CANCEL.format(session.puzzle, session.attempts_count)
    tts = '<speaker audio="alice-sounds-game-loss-1.opus"> {}'.format(prefix)

    return prompt_again(req, answer, prefix, tts=tts)


def exit_session(answer, session):
    """
    Alice user exit session
    """
    session.key.delete()
    answer['end_session'] = True
    answer['text'] = BYE
    answer['buttons'] = [
      {
        "title": LABEL_LIKE,
        "url": LANDING,
        "hide": False,
      },
    ]

    return answer


def new_game(req, answer, prefix, session, with_cow=False):
    """
    start new game in session
    """
    session.is_game_over = False
    session.puzzle = BullCows().puzzle
    session.attempts_count = 0
    session.put()

    tts = None
    if with_cow:
        tts = '<speaker audio="alice-sounds-animals-cow-2.opus"> {}'.format(prefix + START)

    return prompt(req, answer, prefix + START, tts=tts)


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

    return new_game(req, answer, prefix, session, with_cow=True)


def ask_again(req, answer, session, text):
    """
    user answer for new game request
    """
    if text in AGAIN_COMMANDS:
        return new_game(req, answer, AGAIN, session)

    if text in EXIT_COMMANDS:
        return exit_session(answer, session)

    return prompt_again(req, answer, DONT_UNDERSTAND)


def to_int(text):
    """
    extract digits from text
    """
    return ''.join([char for char in text if char.isdigit()])


def july_mention(text):
    """
    return True, if text contain mention of game creator
    """
    return any([True for name in JULY if name in text]) and (BOGOMOLOVA in text)


def handle_answer(req, answer, session, text):
    """
    handle user answer for puzzle
    """
    cows, bulls = BullCows(puzzle=session.puzzle).check(to_int(text))

    if cows is None:
        return prompt(req, answer, DONT_UNDERSTAND)

    if bulls == PUZZLE_LENGTH:
        session.is_game_over = True
        session.put()
        prefix = VICTORY.format(session.attempts_count)
        tts = '<speaker audio="alice-sounds-game-win-1.opus"> {}'.format(prefix)
        return prompt_again(req, answer, prefix, tts=tts)

    session.attempts_count += 1
    session.put()
    tts = BULLS_COWS_TTS.format(cows, bulls)

    return prompt(req, answer, BULLS_COWS.format(cows, bulls), tts=tts)


def dialog(req):  # pylint: disable=too-many-return-statements
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

    text = normalize(req['request'].get('command', ''))
    if not text:
        text = normalize(req['request']['original_utterance'])

    if text in HELP_COMMANDS:
        return prompt(req, answer, HELP)

    if july_mention(text):
        tts = '<speaker audio="alice-sounds-game-powerup-2.opus"> {}'.format(CREATOR)
        return prompt(req, answer, CREATOR, tts=tts)

    if text in CANCEL_COMMANDS:
        return finish(req, answer, session)

    if session.is_game_over:
        return ask_again(req, answer, session, text)

    return handle_answer(req, answer, session, text)
