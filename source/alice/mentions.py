# coding: utf-8
"""
mentions into user input
"""
import random

MENTIONS = [
  (
    # first level - AND, second level - OR
    [["богомолова"], ["юля ", "юлечка ", "юляка ", "юлек ", "юлька"]],
    # answers for mention
    ["Юля Богомолова - так зовут девочку, которая научила меня этой игре."],
    # sound for mention
    ["alice-sounds-game-powerup-2.opus"],
  ),
]


def reply(text):
    """
    return reply if text contain MENTIONS items or return None
    """
    for items, answers, sounds in MENTIONS:
        if all([any([True for word in words if word in text]) for words in items]):
            return (random.choice(answers), random.choice(sounds))

    return (None, None)
