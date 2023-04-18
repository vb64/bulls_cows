"""Root class for testing."""
from tester_flask import TestFlask
from test_helper_gae3 import TestGae3


class TestCase(TestFlask, TestGae3):
    """Base class."""

    def setUp(self, app):
        """Use Flask app."""
        TestFlask.setUp(self, app)
        TestGae3.set_up(self)

    def tearDown(self):
        """Clear tests."""
        TestGae3.tear_down(self)
        super().tearDown()
