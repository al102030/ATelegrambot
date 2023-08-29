
from flask import request, Response, render_template, redirect, url_for
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        if "start" in msg["message"]["text"]:
            # return redirect(url_for("token"))
            token(msg)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token(msg):
    if request.method == 'POST':
        bot_methods.send_message(msg, 112042461)
