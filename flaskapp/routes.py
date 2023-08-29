
from flask import request, Response, render_template
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        bot_methods.send_message(msg, 112042461)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token")
def get_token():
    pass
