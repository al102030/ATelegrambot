
from flask import request, Response
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        bot_methods.send_message(msg, 112042461)
        return Response('ok', status=200)
    else:
        return '<h1>Asazoon Telegram Bot</h1>'
