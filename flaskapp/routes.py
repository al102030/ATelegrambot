
import requests
from config.secrets import LOCALHOST
from flask import request, Response, render_template
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        if "start" in msg["message"]["text"]:
            requests.get(f"{LOCALHOST}/token", timeout=5)
            print(response)
            # token(msg)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token():
    if request.method == 'GET':
        bot_methods.send_message("msg", 112042461)
        return "Message has been sent."
