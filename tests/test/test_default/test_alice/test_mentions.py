# coding: utf-8
"""Creator mentions.

make test T=test_default/test_alice/test_mentions.py
"""
from . import TestAlice


class TestMentions(TestAlice):
    """Alice mentions module."""

    @staticmethod
    def test_reply():
        """Alice messages.reply."""
        from alice.messages import reply

        relpy, _sound = reply("меня зовут юля богомолова.")
        assert relpy
        relpy, _sound = reply("привет юляка богомолова.")
        assert relpy
        relpy, _sound = reply("кто такая богомолова?")
        assert not relpy
