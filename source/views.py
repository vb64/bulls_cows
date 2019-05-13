"""
App endpoint handlers
"""
from wsgi import app


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
