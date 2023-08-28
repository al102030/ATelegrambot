
from flask import request, Response
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        print("A message received")
        return Response('ok', status=200)
    else:
        return '<h1>Asazoon Telegram Bot</h1>'
