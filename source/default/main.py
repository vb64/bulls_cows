"""Default GAE service."""
import logging
import json
from flask import Flask, request
from alice.dialog import dialog

app = Flask(__name__)


@app.route('/')
def main():
    """Root page."""
    return "Yandex Alice Bulls&Cows game lives here"


@app.route('/alice', methods=['POST'])
def alice_webhook():
    """Frontend."""
    # check for correct  skill ID
    # if request.json['session']['skill_id'] != 'Your_Alice_Skill_ID':
    #     from flask import abort
    #     abort(404)
    logging.info('Request: %r', request.json)

    return json.dumps(
      {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": dialog(request.json),
      },
      encoding='utf8',
      ensure_ascii=False,
      indent=2
    )


if __name__ == '__main__':  # pragma: no cover
    app.run(host='127.0.0.1', port=8080, debug=True)
