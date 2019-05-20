"""
make test T=test_urls
"""
from . import TestCase


class TestCaseUrl(TestCase):
    """
    common web endpoints
    """
    def test_warmup(self):
        """
        warmup
        """
        response = self.simple_view('warmup')
        self.assertEqual(response.data, 'OK')

    def test_backend_start(self):
        """
        GAE backend start signal
        """
        response = self.simple_view('backend_start')
        self.assertEqual(response.data, 'OK')

    def test_home(self):
        """
        root page
        """
        response = self.simple_view('mainpage')
        self.assertEqual(response.status_code, 200)

    def test_cron(self):
        """
        cron url
        """
        response = self.simple_view('cron_touch')
        self.assertEqual(response.status_code, 200)

        response = self.simple_view('cron_onetime')
        self.assertEqual(response.status_code, 200)

    def test_alice_webhook(self):
        """
        alice webhook must be POST
        """
        response = self.simple_view('alice_webhook', return_code=405)
        self.assertEqual(response.status_code, 405)
