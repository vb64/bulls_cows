"""
Root class for testing
"""
from tester_gae import TestGae
from tester_flask import TestFlask
from tester_coverage import TestCoverage


class TestCase(TestFlask, TestGae, TestCoverage):
    """
    base class
    """
    def setUp(self):  # pylint: disable=arguments-differ
        TestCoverage.setUp(self)  # order of setUp calls is important!

        from appengine_config import PROJECT_DIR
        TestGae.setUp(self, PROJECT_DIR)

        from wsgi import app
        TestFlask.setUp(self, app)

    def tearDown(self):
        TestGae.tearDown(self)
        TestCoverage.tearDown(self)
