# coding: utf-8
"""
Translate numbers to RU words.
Based on https://github.com/seriyps/ru_number_to_text
"""
UNITS = (
  'ноль',
  ('один', 'одна'), ('два', 'две'),
  'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять'
)
TEENS = (
  'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
  'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
)
TENS = (
  TEENS,
  'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
)
HUNDREDS = (
  'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот'
)
ORDERS = (  # plural forms and gender
  (('тысяча', 'тысячи', 'тысяч'), 'f'),
  (('миллион', 'миллиона', 'миллионов'), 'm'),
  (('миллиард', 'миллиарда', 'миллиардов'), 'm'),
)
ZERO_NOT = 'нет'
MINUS = 'минус'


def thousand(rest, sex):
    """
    Converts numbers from 19 to 999
    """
    prev = 0
    plural = 2
    name = []
    data = ((UNITS, 10), (TENS, 100), (HUNDREDS, 1000))
    use_teens = rest % 100 >= 10 and rest % 100 <= 19

    if use_teens:
        data = ((TEENS, 10), (HUNDREDS, 1000))

    for names, rank in data:
        cur = int(((rest - prev) % rank) * 10 / rank)
        prev = rest % rank
        if rank == 10 and use_teens:
            plural = 2
            name.append(TEENS[cur])
        elif cur == 0:
            continue
        elif rank == 10:
            name_ = names[cur]
            if isinstance(name_, tuple):
                name_ = name_[0 if sex == 'm' else 1]
            name.append(name_)
            if cur >= 2 and cur <= 4:
                plural = 1
            elif cur == 1:
                plural = 0
            else:
                plural = 2
        else:
            name.append(names[cur-1])

    return plural, name


def int2words(num, main_units=((u'', u'', u''), 'm'), zero_not=False):
    """
    http://ru.wikipedia.org/wiki/Gettext#.D0.9C.D0.BD.D0.BE.D0.B6.D0.B5.D1.81.
    D1.82.D0.B2.D0.B5.D0.BD.D0.BD.D1.8B.D0.B5_.D1.87.D0.B8.D1.81.D0.BB.D0.B0_2
    """
    orders = (main_units,) + ORDERS
    if num == 0:
        zero = UNITS[0]
        if zero_not:
            zero = ZERO_NOT
        return ' '.join((zero, orders[0][0][2])).strip()

    rest = abs(num)
    index = 0
    name = []
    while rest > 0:
        plural, nme = thousand(rest % 1000, orders[index][1])
        if nme or index == 0:
            name.append(orders[index][0][plural])
        name += nme
        rest = int(rest / 1000)
        index += 1
    if num < 0:
        name.append(MINUS)
    name.reverse()

    return ' '.join(name).strip()
