# coding: utf-8
"""Module num2words.

make test T=test_num2words.py
"""
from . import TestCase


class TestInt2words(TestCase):
    """Function num2words.int2words."""

    def test_units(self):
        """Check units."""
        from num2words import int2words

        self.assertEqual(int2words(0), 'ноль')
        self.assertEqual(int2words(1), 'один')
        self.assertEqual(int2words(9), 'девять')

        self.assertEqual(int2words(1000), 'одна тысяча')
        self.assertEqual(int2words(2000), 'две тысячи')
        self.assertEqual(int2words(1000000), 'один миллион')
        self.assertEqual(int2words(2000000), 'два миллиона')

        self.assertEqual(int2words(10), 'десять')
        self.assertEqual(int2words(11), 'одиннадцать')
        self.assertEqual(int2words(19), 'девятнадцать')

        self.assertEqual(int2words(20), 'двадцать')
        self.assertEqual(int2words(90), 'девяносто')

        self.assertEqual(int2words(100), 'сто')
        self.assertEqual(int2words(900), 'девятьсот')

        self.assertEqual(int2words(1000), 'одна тысяча')
        self.assertEqual(int2words(2000), 'две тысячи')
        self.assertEqual(int2words(5000), 'пять тысяч')
        self.assertEqual(int2words(1000000), 'один миллион')
        self.assertEqual(int2words(2000000), 'два миллиона')
        self.assertEqual(int2words(5000000), 'пять миллионов')
        self.assertEqual(int2words(1000000000), 'один миллиард')
        self.assertEqual(int2words(2000000000), 'два миллиарда')
        self.assertEqual(int2words(5000000000), 'пять миллиардов')

        self.assertEqual(int2words(1100), 'одна тысяча сто')
        self.assertEqual(int2words(2001), 'две тысячи один')
        self.assertEqual(int2words(5011), 'пять тысяч одиннадцать')
        self.assertEqual(int2words(1002000), 'один миллион две тысячи')
        self.assertEqual(int2words(2020000), 'два миллиона двадцать тысяч')
        self.assertEqual(int2words(5300600), 'пять миллионов триста тысяч шестьсот')
        self.assertEqual(int2words(1002000000), 'один миллиард два миллиона')
        self.assertEqual(int2words(2030000000), 'два миллиарда тридцать миллионов')
        self.assertEqual(
          int2words(1234567891),
          'один миллиард двести тридцать четыре миллиона '
          'пятьсот шестьдесят семь тысяч '
          'восемьсот девяносто один'
        )

    def test_main_units(self):
        """
        main_units
        """
        from num2words import int2words

        male_units = (('рубль', 'рубля', 'рублей'), 'm')
        female_units = (('копейка', 'копейки', 'копеек'), 'f')

        self.assertEqual(int2words(101, male_units), 'сто один рубль')
        self.assertEqual(int2words(102, male_units), 'сто два рубля')
        self.assertEqual(int2words(105, male_units), 'сто пять рублей')

        self.assertEqual(int2words(101, female_units), 'сто одна копейка')
        self.assertEqual(int2words(102, female_units), 'сто две копейки')
        self.assertEqual(int2words(105, female_units), 'сто пять копеек')

        self.assertEqual(int2words(0, male_units), 'ноль рублей')
        self.assertEqual(int2words(0, female_units), 'ноль копеек')
        self.assertEqual(int2words(0, female_units, zero_not=True), 'нет копеек')

        self.assertEqual(int2words(3000, male_units), 'три тысячи рублей')

    def test_negative(self):
        """
        negative
        """
        from num2words import int2words

        self.assertEqual(int2words(-12345), "минус двенадцать тысяч триста сорок пять")
