# coding: utf-8
"""
make test T=test_alice.test_mentions
"""
from . import TestAlice


class TestMentions(TestAlice):
    """
    alice.mentions module
    """
    def test_reply(self):
        """
        alice.messages.reply
        """
        from alice.messages import reply

        relpy, _sound = reply("меня зовут юля богомолова.")
        self.assertTrue(relpy)
        relpy, _sound = reply("привет юляка богомолова.")
        self.assertTrue(relpy)
        relpy, _sound = reply("кто такая богомолова?")
        self.assertFalse(relpy)
