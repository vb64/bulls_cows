# coding: utf-8
"""
make test T=test_alice.test_dialog
"""
from . import TestAlice


class TestDialog(TestAlice):
    """
    functions from alice.dialog module
    """
    def test_july_mention(self):
        """
        july_mention
        """
        from alice.dialog import july_mention
        self.assertTrue(july_mention("меня зовут юля богомолова."))
        self.assertTrue(july_mention("привет юляка богомолова."))
        self.assertFalse(july_mention("кто такая богомолова?"))

    def test_to_int(self):
        """
        to_int
        """
        from alice.dialog import to_int
        self.assertEqual(to_int('12 37.'), '1237')
        self.assertEqual(to_int('55,666'), '55666')

    def test_dialog(self):
        """
        dialog
        """
        from alice.dialog import dialog

        req = {
          'session': {
            'new': False,
            'session_id': 'xxx',
          },
        }
        answer = dialog(req)
        self.assertEqual(answer['end_session'], True)
        self.assertIn(self.err_message, answer['text'])
