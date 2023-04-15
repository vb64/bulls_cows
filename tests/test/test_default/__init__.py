"""GAE service default."""
from .. import TestCase


class TestDefault(TestCase):
    """Default service."""

    def setUp(self):  # pylint: disable=arguments-differ
        """Use Flask app."""
        from main import app

        TestCase.setUp(self, app)
