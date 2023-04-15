"""Flask app endpoints.

make test T=test_urls.py
"""
from . import TestDefault


class TestCaseUrl(TestDefault):
    """Common web endpoints."""

    def test_home(self):
        """Root page."""
        response = self.simple_view('main')
        assert response.status_code == 200

    def test_alice_webhook(self):
        """Alice webhook must be POST."""
        response = self.simple_view('alice_webhook', return_code=405)
        assert response.status_code == 405
