
import json
import requests
from flask import request, Response, render_template
from config.secrets import LOCALHOST
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        # bot_methods.send_message(msg, 112042461)
        bot_methods.send_message_with_menu(
            "HI", 112042461, {"1": "One", "2": "Two", "3": "Three", "4": "Four"})
        try:
            text = msg['message']['text']
            chat_id = msg['message']['chat']['id']
        except KeyError as error:
            print("KeyError :", error)
            text = None
        if text is not None:
            user_select_keyboard = []
            if "/start" in text:
                params = {
                    "chat_id": chat_id,
                    "text": text
                }
                response = requests.post(
                    f"{LOCALHOST}/token", params=params, timeout=20)
                if response.text != "Not allowed!":
                    user_select_keyboard = list_maker(response.json())
                    bot_methods.send_message_with_menu(
                        "Please select", chat_id, user_select_keyboard)
                else:
                    print("Wrong User!")
                    bot_methods.send_message(
                        "Wrong URL. You can't access to options.", chat_id)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token():
    if request.method == 'POST':
        text = ((request.args.get('text')).strip()).replace("/start", "")
        if text is not "":
            params = {
                "text": text,
            }
            response = requests.post(
                f"{LOCALHOST}/server", params=params, timeout=20)
            if response.text != "empty":
                return response.json()
            else:
                return "Not allowed!"
        else:
            return "Not allowed!"


@app.route("/server", methods=["GET", "POST"])
def server():
    if request.method == 'POST':
        json_string1 = json.dumps({"1": "A", "2": "B", "3": "C", "4": "D"})
        json_string2 = json.dumps({"5": "E", "6": "F", "7": "G", "8": "H"})
        text = request.args.get('text')
        if "e6fbd60e70962e97" in text:
            return json_string1
        elif "4676de3ae0db1ea7" in text:
            return json_string2
        else:
            return "empty"


def list_maker(server_json):
    user_select_keyboard = []
    for key, value in server_json.items():
        lst = []
        dictionary = {}
        dictionary['text'] = key
        dictionary['callback_data'] = value
        lst.append(dictionary)
        user_select_keyboard.append(lst)
    return user_select_keyboard
