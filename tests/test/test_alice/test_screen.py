"""
make test T=test_alice.test_screen
"""
from tester_alice_skill_flask import Interface

from . import TestAlice


class TestScreen(TestAlice):
    """
    screen dialog with buttons
    """
    def setUp(self):
        super(TestScreen, self).setUp()
        self.alice = self.skill.new_session('1234567890', [Interface.Screen])
        self.assertEqual(len(self.alice.buttons), 2)

    def test_help(self):
        """
        help button
        """
        self.alice.clear()
        self.alice.send_button(1)

        self.assertFalse(self.alice.contain(self.start_message))
        self.assertTrue(self.alice.contain(self.prompt_message))
        self.assertTrue(self.alice.contain(self.help_message))
        self.assertEqual(len(self.alice.buttons), 2)

    def test_cancel(self):
        """
        cancel button
        """
        self.alice.clear()
        self.alice.send_button(0)

        self.assertFalse(self.alice.contain(self.start_message))
        self.assertFalse(self.alice.contain(self.prompt_message))
        self.assertFalse(self.alice.contain(self.help_message))

        self.assertTrue(self.alice.contain(self.stat_fail_message))
        self.assertTrue(self.alice.contain(self.stat_fail_message))
        self.assertEqual(len(self.alice.buttons), 2)

        self.alice.send_button(0)
        self.alice.send_button(0)
        self.alice.clear()
        self.alice.send_button(1)

        self.assertFalse(self.alice.contain(self.prompt_message))
        self.assertTrue(self.alice.contain(self.bye_message))
        self.assertEqual(len(self.alice.buttons), 1)
        # print self.alice.dump().decode('utf-8')
