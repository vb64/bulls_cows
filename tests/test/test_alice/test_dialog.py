# coding: utf-8
"""
make test T=test_alice/test_dialog.py
"""
from . import TestAlice


class TestDialog(TestAlice):
    """Check functions from alice.dialog module."""

    def test_to_int(self):
        """Function to_int."""
        from alice.dialog import to_int
        self.assertEqual(to_int('12 37.'), '1237')
        self.assertEqual(to_int('55,666'), '55666')

    def test_dialog(self):
        """Check dialog."""
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

    def test_command(self):
        """Check original_utterance and command."""
        from alice.dialog import dialog
        from alice.models import SessionYA as Session

        self.skill.new_session('1234567890', [])
        self.db_sessions(1)
        session = Session.query().fetch(1)[0]

        req = {
          'session': {
            'new': False,
            'session_id': session.key.id(),
          },
          'request': {
            'original_utterance': 'xxxx yyyy',
            'command': 'yyy xxx',
          },
          'meta': {
            'interfaces': [],
          },
        }

        answer = dialog(req)
        self.assertEqual(answer['end_session'], False)
