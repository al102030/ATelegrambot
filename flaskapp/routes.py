
import requests
from flask import request, Response, render_template
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        if "start" in msg["message"]["text"]:
            response = requests.get("http://127.0.0.1:5030/token", timeout=20)
            # print(response)
            # token(msg)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token():
    if request.method == 'GET':
        bot_methods.send_message("msg", 112042461)
