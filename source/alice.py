# coding: utf-8
"""
Yandex.Alice skill
"""
HELP_COMMANDS = ["помощь", "что ты умеешь"]

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


def new_session(req, answer):
    """
    alice user start new session
    """
    # get optional command for new session
    command = normalize(req['request'].get('command', ''))
    answer['text'] = ""

    if command in ["ping"]:
        # Alice check for your skill availability
        answer['text'] = "pong"
        answer['end_session'] = True
        return answer

    if command:
        # handle on start commands
        if command in HELP_COMMANDS:
            answer['text'] = HELP_MESSAGE

    answer['text'] += START_MESSAGE + PROMPT_MESSAGE
    return answer


def dialog(req):
    """
    alice request handler
    """
    answer = {"end_session": False}

    if req['session']['new']:
        return new_session(req, answer)

    return answer
