"""Module num2words.

make test T=test_default/test_num2words.py
"""
from . import TestDefault


class TestInt2words(TestDefault):
    """Function num2words.int2words."""

    def test_units(self):
        """Check units."""
        from num2words import int2words

        assert int2words(0) == 'ноль'
        assert int2words(1) == 'один'
        assert int2words(9) == 'девять'

        assert int2words(1000) == 'одна тысяча'
        assert int2words(2000) == 'две тысячи'
        assert int2words(1000000) == 'один миллион'
        assert int2words(2000000) == 'два миллиона'

        assert int2words(10) == 'десять'
        assert int2words(11) == 'одиннадцать'
        assert int2words(19) == 'девятнадцать'

        assert int2words(20) == 'двадцать'
        assert int2words(90) == 'девяносто'

        assert int2words(100) == 'сто'
        assert int2words(900) == 'девятьсот'

        assert int2words(1000) == 'одна тысяча'
        assert int2words(2000) == 'две тысячи'
        assert int2words(5000) == 'пять тысяч'
        assert int2words(1000000) == 'один миллион'
        assert int2words(2000000) == 'два миллиона'
        assert int2words(5000000) == 'пять миллионов'
        assert int2words(1000000000) == 'один миллиард'
        assert int2words(2000000000) == 'два миллиарда'
        assert int2words(5000000000) == 'пять миллиардов'

        assert int2words(1100) == 'одна тысяча сто'
        assert int2words(2001) == 'две тысячи один'
        assert int2words(5011) == 'пять тысяч одиннадцать'
        assert int2words(1002000) == 'один миллион две тысячи'
        assert int2words(2020000) == 'два миллиона двадцать тысяч'
        assert int2words(5300600) == 'пять миллионов триста тысяч шестьсот'
        assert int2words(1002000000) == 'один миллиард два миллиона'
        assert int2words(2030000000) == 'два миллиарда тридцать миллионов'

        assert int2words(1234567891) == 'один миллиард двести тридцать четыре миллиона '\
            'пятьсот шестьдесят семь тысяч восемьсот девяносто один'

    def test_main_units(self):
        """Check  main_units."""
        from num2words import int2words

        male_units = (('рубль', 'рубля', 'рублей'), 'm')
        female_units = (('копейка', 'копейки', 'копеек'), 'f')

        assert int2words(101, male_units) == 'сто один рубль'
        assert int2words(102, male_units) == 'сто два рубля'
        assert int2words(105, male_units) == 'сто пять рублей'

        assert int2words(101, female_units) == 'сто одна копейка'
        assert int2words(102, female_units) == 'сто две копейки'
        assert int2words(105, female_units) == 'сто пять копеек'

        assert int2words(0, male_units) == 'ноль рублей'
        assert int2words(0, female_units) == 'ноль копеек'
        assert int2words(0, female_units, zero_not=True) == 'нет копеек'

        assert int2words(3000, male_units) == 'три тысячи рублей'

    def test_negative(self):
        """Negative."""
        from num2words import int2words

        assert int2words(-12345) == "минус двенадцать тысяч триста сорок пять"
