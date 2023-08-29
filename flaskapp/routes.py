
from flask import request, Response, render_template, redirect, url_for
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        if "start" in msg:
            return redirect(url_for("token"))
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", method=["GET", "POST"])
def token():
    bot_methods.send_message("it works!", 112042461)
