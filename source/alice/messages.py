# coding: utf-8
"""
skill messages
"""
# button labels
LABEL_CANCEL = "Сдаюсь"
LABEL_HELP = "Помощь"
LABEL_AGAIN = "Да"
LABEL_EXIT = "Нет"

HELP_COMMANDS = ["помощь", "что ты умеешь"]
CANCEL_COMMANDS = ["сдаюсь", "надоело", "не знаю"]
AGAIN_COMMANDS = ["да", "окей", "сыграем", "давай", "еще"]
EXIT_COMMANDS = ["нет", "не хочу", "не надо"]

HELP = ''.join((
  "Этот навык умеет играть в логическую игру быки и коровы.", ' ',
  "Нужно отгадать число из четырех разных цифр.", ' ',
  "Навык будет сообщать число быков и коров в вашем ответе.", ' ',
  "Быки - сколько цифр в ответе находятся на правильном месте в загаданном числе.", ' ',
  "Коровы - сколько цифр в ответе есть в загаданном числе, но находятся на неверном месте.", ' ',
  "Игра закончится, когда вы угадаете четырех быков или ответите словом сдаюсь.", '\n\n',
))

START = ''.join((
  "Я загадала число из четырех разных цифр.", ' ',
  "Тебе нужно его угадать.", '\n\n',
))

PROMPT = "Введи число из четырех разных цифр."
PROMPT_AGAIN = "Сыграем еще раз?"
ERROR = "Ошибка. Попробуйте начать новую игру."
AGAIN = "Отлично, сыграем еще раз.\n\n"
STATS_CANCEL = "Я загадывала число {}. Сделано попыток угадать: {}\n\n"
BYE = "Возвращайся, поиграем еще."
DONT_UNDERSTAND = "Не понимаю ответ. "
VICTORY = "Задача решена, попыток: {}\n\n"
BULLS_COWS = "Коров: {} быков {}\n\n"
JULY = ["юля ", "юлечка ", "юляка ", "юлек ", "юлька"]
BOGOMOLOVA = "богомолова"
CREATOR = "Юля Богомолова - так зовут девочку, которая научила меня этой игре.\n\n"