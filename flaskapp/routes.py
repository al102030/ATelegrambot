
import requests
from flask import request, Response, render_template
from config.secrets import LOCALHOST
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        try:
            text = msg['message']['text']
            chat_id = msg['message']['chat']['id']
        except KeyError as error:
            print("KeyError :", error)
            text = None
        bot_methods.send_message(chat_id, 112042461)
        if text:
            if "/start" in text:
                print(f"text is >>>> {text} and chat_id = >>> {chat_id}")
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json"
                }
                params = {
                    "chat_id": chat_id,
                    "text": text
                }
                requests.get(f"{LOCALHOST}/token", params=params,
                             headers=headers, timeout=5)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token():
    if request.method == 'GET':
        text = request.args.get('text')
        chat_id = request.args.get("chat_id")
        bot_methods.send_message(f"{text} from {chat_id}", 112042461)
        return "Message has been sent."
