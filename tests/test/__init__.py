"""Root class for testing."""
from google.appengine.ext import testbed
from tester_flask import TestFlask


class TestCase(TestFlask):
    """Base class."""

    def setUp(self):  # pylint: disable=arguments-differ
        """Use Flask app."""
        from main import app

        TestFlask.setUp(self, app)

        self.gae_testbed = testbed.Testbed()
        self.gae_testbed.activate()
        self.gae_testbed.init_datastore_v3_stub()
        self.gae_testbed.init_memcache_stub()

    def tearDown(self):
        """Clear tests."""
        self.gae_testbed.deactivate()
        super().tearDown()

    def check_db_tables(self, db_state):
        """Check record count for given GAE db tables."""
        for table, count in db_state:
            i = len(table.query().fetch(300, keys_only=True))
            assert i == count, "{} items: {} must be {}".format(
              table._get_kind(),  # pylint: disable=protected-access
              i,
              count
            )
