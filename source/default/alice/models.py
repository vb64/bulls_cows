"""GAE Datastore tables definition."""
from google.appengine.ext import ndb


class SessionYA(ndb.Model):
    """Key.id: alice session_id."""

    puzzle = ndb.TextProperty(default=None)
    last_attempt = ndb.DateTimeProperty(auto_now=True)
    attempts_count = ndb.IntegerProperty(default=None, indexed=False)
    is_game_over = ndb.BooleanProperty(default=False, indexed=False)
