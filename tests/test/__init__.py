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

    def execute_backend_tasks(self, queue_name='default'):
        """
        run all tasks for given GAE taskqueue
        """
        tasks = self.gae_tasks(queue_name=queue_name, flush_queue=True)
        for task in tasks:
            # print "#->", task['method'], task['url'], task['body']
            if task['method'] == 'GET':
                response = self.client.get(task['url'])
            elif task['method'] == 'POST':
                response = self.client.post(task['url'], data=task['body'])
            else:
                response = 'Wrong taskqueue method: {}'.format(task['method']), 500, {}

            self.assertEqual(response.status_code, 200)
