
import requests
import json
from flask import request, Response, render_template
from config.secrets import LOCALHOST
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        print("A Message has received!")
        try:
            text = msg['message']['text']
            chat_id = msg['message']['chat']['id']
        except KeyError as error:
            print("KeyError :", error)
            text = None
        print(text)
        if text is not None:
            user_select_keyboard = []
            if "/start" in text:
                params = {
                    "chat_id": chat_id,
                    "text": text
                }
                response = requests.post(
                    f"{LOCALHOST}/token", params=params, timeout=20)
                print(response.json())
                # user_select_keyboard = list_maker(response.json())
            # bot_methods.send_message_with_menu(
            #     "Please select", chat_id, user_select_keyboard)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token():
    if request.method == 'POST':
        text = ((request.args.get('text')).strip()).replace("/start", "")
        print(text)
        if text is not None:
            params = {
                "text": text,
            }
            response = requests.post(
                f"{LOCALHOST}/server", params=params, timeout=20)
            print(response)
        return response


@app.route("/server", methods=["GET", "POST"])
def server():
    if request.method == 'POST':
        dict1 = dict({"1": "A", "2": "B", "3": "C", "4": "D"})
        dict2 = dict({"5": "E", "6": "F", "7": "G", "8": "H"})
        json_string1 = json.dumps(dict1)
        json_string2 = json.dumps(dict2)
        text = request.args.get('text')
        if "e6fbd60e70962e97" in text:
            return json_string1
        elif "4676de3ae0db1ea7" in text:
            return json_string2
        else:
            return None


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
