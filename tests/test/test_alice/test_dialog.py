"""
make test T=test_alice.test_dialog
"""
from . import TestAlice


class TestDialog(TestAlice):
    """
    functions from alice.dialog module
    """
    def test_to_int(self):
        """
        to_int
        """
        from alice.dialog import to_int
        self.assertEqual(to_int('12 37.'), '1237')
        self.assertEqual(to_int('55,666'), '55666')

    def test_handle_button(self):
        """
        handle_button
        """
        from alice.dialog import handle_button

        answer = handle_button({'request': {'payload': {}}}, {}, None)
        self.assertEqual(answer['end_session'], True)
        self.assertIn(self.err_message, answer['text'])

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
