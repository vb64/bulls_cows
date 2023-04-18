"""Backup app endpoints.

make test T=test_backend/test_main.py
"""
from datetime import datetime, timedelta
from . import TestBackend


class TestBackMain(TestBackend):
    """Backup web endpoints."""

    def test_empty(self):
        """No records."""
        from back import main
        assert 'Deleted: 0' in main()

    def test_filled(self):
        """Filled table case."""
        import back
        from back import SessionYA

        save1 = back.PORTION
        save2 = back.PARTS

        back.PORTION = 3
        back.PARTS = 1
        date = datetime.utcnow() - timedelta(days=back.DAYS_OLD + 1)

        for _i in range(5):
            record = SessionYA()
            record.last_attempt = date
            record.put()

        assert 'Deleted: 3' in back.main()

        back.PORTION = save1
        back.PARTS = save2
