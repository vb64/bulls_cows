"""Skill messages."""
import random

# button labels
LABEL_CANCEL = "Сдаюсь"
LABEL_HELP = "Помощь"
LABEL_AGAIN = "Да"
LABEL_EXIT = "Нет"
LABEL_LIKE = "Поставь лайк, если понравилось."

START = "Я загадала число из четырех разных цифр. Тебе нужно его угадать.\n"
PROMPT = "Введи число из четырех разных цифр."
PROMPT_AGAIN = "Сыграем еще раз?"
ERROR = "Ошибка. Попробуйте начать новую игру."
AGAIN = "Отлично, сыграем еще раз. "
STATS_CANCEL = "Я загадывала число {}. Сделано попыток угадать: {} "
BYE = "Возвращайся, - поиграем еще."
DONT_UNDERSTAND = "Не понимаю ответ. "
VICTORY = "Задача решена, попыток: {} "
BULLS_COWS = "Коров: {} быков: {}\n"
HELP = (
  "Этот навык умеет играть в логическую игру быки и коровы. "
  "Нужно отгадать число из четырех разных цифр. "
  "Навык будет сообщать число быков и коров в вашем ответе. "
  "Быки - сколько цифр в ответе находятся на правильном месте в загаданном числе. "
  "Коровы - сколько цифр в ответе есть в загаданном числе, но находятся на неверном месте. "
  "Игра закончится, когда вы угадаете четырех быков или ответите словом сдаюсь.\n"
)

HELP_COMMANDS = ["помощь", "что ты умеешь"]
CANCEL_COMMANDS = ["сдаюсь", "надоело", "не знаю"]
AGAIN_COMMANDS = ["да", "окей", "сыграем", "давай", "еще"]
EXIT_COMMANDS = ["нет", "не хочу", "не надо"]

TTS_COWS = (("кор+ова", "кор+овы", "кор+ов"), "f")
TTS_BULLS = (("бык", "бык+а", "бык+ов"), "m")

MENTIONS = [
  (
    # first level - AND, second level - OR
    [["богомолова"], ["юля ", "юлечка ", "юляка ", "юлек ", "юлька"]],
    # answers for mention
    ["Юля Богомолова - так зовут девочку, которая научила меня этой игре."],
    # sound for mention
    ["alice-sounds-game-powerup-2.opus"],
  ),
  (
    [HELP_COMMANDS],
    [HELP],
    ["alice-sounds-game-powerup-2.opus"],
  ),
]


def reply(text):
    """Return reply if text contain MENTIONS items."""
    for items, answers, sounds in MENTIONS:
        if all([any(  # pylint: disable=use-a-generator
          [True for word in words if word in text]
        ) for words in items]):
            return (random.choice(answers), random.choice(sounds))

    return (None, None)
