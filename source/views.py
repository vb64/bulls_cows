"""
App endpoint handlers
"""
import json
from flask import request

from wsgi import app
from alice.dialog import dialog


@app.route('/cron/onetime/', methods=['GET', 'POST'])
def cron_onetime():
    """
    for onetime tasks
    """
    return 'OK'


@app.route('/cron/touch/', methods=['GET', 'POST'])
def cron_touch():
    """
    regular cron tasks
    """
    return 'OK'


@app.route('/_ah/warmup')
def warmup():
    """
    warmup request
    """
    return 'OK'


@app.route('/_ah/start')
def backend_start():
    """
    backend start request
    """
    return 'OK'


@app.route('/')
def mainpage():
    """
    root page
    """
    return "Yandex Alice Bulls&Cows game lives here"


@app.route('/alice', methods=['POST'])
def alice_webhook():
    """
    frontend
    """
    return json.dumps(
      {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": dialog(request.json),
      },
      ensure_ascii=False,
      indent=2
    )
