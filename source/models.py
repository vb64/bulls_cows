"""
GAE Datastore tables definition
"""
from google.appengine.ext import ndb


class Session(ndb.Model):  # pylint: disable=too-few-public-methods
    """
    key.id: alice session_id
    """
    last_attempt = ndb.DateTimeProperty(auto_now=True)
    attempts_count = ndb.IntegerProperty(default=None, indexed=False)
