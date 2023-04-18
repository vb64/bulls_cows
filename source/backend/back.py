"""Backend GAE service."""
from datetime import datetime, timedelta
import logging
from flask import Flask
from google.appengine.ext import ndb
from google.appengine.api import wrap_wsgi_app

PORTION = 500
PARTS = 30
DAYS_OLD = 30

app = Flask(__name__)
app.wsgi_app = wrap_wsgi_app(app.wsgi_app)


class SessionYA(ndb.Model):
    """Key.id: alice session_id."""

    last_attempt = ndb.DateTimeProperty()


@app.route('/')
def main():
    """Purge ndb model SessionYA."""
    count = 0
    border_date = datetime.utcnow() - timedelta(days=DAYS_OLD)
    query = SessionYA.query(SessionYA.last_attempt < border_date)

    for _i in range(PARTS):
        keys = query.fetch(PORTION, keys_only=True)
        if not keys:
            return "Complete table 'SessionYA'. Deleted: {}".format(count)
        count += len(keys)
        ndb.model.delete_multi(keys)

    logging.warning("### Table 'SessionYA'. Deleted: %s", count)
    return "Table 'SessionYA' Deleted: {}".format(count)


if __name__ == '__main__':  # pragma: no cover
    app.run(host='127.0.0.1', port=8080, debug=True)
