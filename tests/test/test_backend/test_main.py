"""Backup app endpoints.

make test T=test_backend/test_main.py
"""
from . import TestBackend


class TestCaseUrl(TestBackend):
    """Backup web endpoints."""

    def test_main(self):
        """Function main."""
        from back import main
        assert 'Deleted: 0' in main()
