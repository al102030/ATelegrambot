
import json
import requests
from flask import request, Response, render_template
from config.secrets import LOCALHOST
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        try:
            text, chat_id = msg['message']['text'], msg['message']['chat']['id']
        except KeyError:
            text = None
        if text is not None:
            user_select_keyboard = []
            if "/start" in text:
                user_hash = (text.strip()).replace("/start", "")
                if user_hash != "":
                    params = {"chat_id": chat_id, "text": user_hash}
                    response = requests.post(
                        f"{LOCALHOST}/start", params=params, timeout=20)
                    if response.text != "Not allowed!":
                        user_select_keyboard = list_maker(
                            response.json()["menu"])
                        bot_methods.send_message_with_menu(
                            response.json()["greet"], chat_id, user_select_keyboard)
                    else:
                        bot_methods.send_message(
                            "Wrong URL. Your access code is incorrect!.", chat_id)
                else:
                    bot_methods.send_message(
                        "Wrong URL. To access the bot options, please connect with us.\nThank you.", chat_id)
            else:
                params = {"action": "text",
                          "chat_id": chat_id, "text": text}
                response = requests.post(
                    f"{LOCALHOST}/server", params=params, timeout=20)
                msg = response.json()
                bot_methods.send_message(
                    msg, chat_id)

        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == 'POST':
        user_hash = request.args.get('text')
        chat_id = request.args.get('chat_id')
        params = {"action": "start", "chat_id": chat_id, "text": user_hash, }
        response = requests.post(
            f"{LOCALHOST}/server", params=params, timeout=20)
        return response.json() if response.text != "empty" else "Not allowed!"


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


# @app.route("/token", methods=["GET", "POST"])
# def token():
#     if request.method == 'POST':
#         chat_id = request.args.get('chat_id')
#         params = {
#             "action": "token",
#             "chat_id": chat_id,
#         }
#         response = requests.post(
#             f"{LOCALHOST}/server", params=params, timeout=20)
#         return response.text if response is not None else "Not exist"


# =======================================================================================

@app.route("/server", methods=["GET", "POST"])
def server():
    if request.method == 'POST':
        action = request.args.get('action')
        if action == "start":
            greet_text1 = """خوش آمد:
                            باسلام خدمت شما دوست گرامی🌹
                            بابت همراهی شما بسیار خرسندیم

                            مجموعه صنایع سنگ نادر ، به جهت راحتی شما این ربات را طراحی نموده تا شما با خیال راحت و هرکجا که هستید ، فعالیت‌ها و نمونه‌کارهای مجموعه را مشاهده بفرمایید


                            اطلاعات مورد نیاز در آیتم ها
                            واحد فروش ۰۳۵۳۶۲۴۲۴۱۴
                            مدیریت ۰۹۱۳۲۵۱۳۰۳۰
                            شماره پاسخگو ۰۹۱۳۳۵۳۳۱۰۶
                            شماره واتساپ
                            ۰۹۱۳۲۵۱۳۰۳۰
                            آیدی تلگرام
                            t.me/naderstone
                            جهت ارتباط ، مشاوره و ثبت سفارش
                            با شماره‌های زیر تماس حاصل فرمایید :
                            ۰۹۱۳۲۵۱۳۰۳۰
                            ۰۹۱۳۳۵۳۳۱۰۶

                            آدرس کانال ایتا و تلگرام مجموعه :
                            t.me/naderstone

                            eitaa.com/naderstone"""
            greet_text2 = "Some text"
            json_string1 = json.dumps(
                {"menu": {"تماس با ما": "A", "درباره ما": "B", "فروشگاه": "C", "مشاهده محصولات": "D"}, "greet": greet_text1})
            json_string2 = json.dumps(
                {"menu": {"5": "E", "6": "F", "7": "G", "8": "H"}, "greet": greet_text2})
            print(json_string1)
            text = request.args.get('text')
            if "e6fbd60e70962e97" in text:
                return json_string1
            elif "4676de3ae0db1ea7" in text:
                return json_string2
            else:
                return "empty"
        elif action == "text":
            chat_id = request.args.get('chat_id')
            text = request.args.get('text')
            if text == "text":
                data = json.dumps(
                    {"type": "inline_keyboard", "text": "Some text to user"})
                return data
            elif text == "menu1":
                dictionary = json.dumps(
                    {"menu": {"A": "O1", "B": "O2", "C": "O3", "D": "O4"}, "type": "inline_keyboard", "text": "Please select one."})
                return dictionary
            elif text == "menu2":
                dictionary = json.dumps(
                    {"menu": {"A": "O1", "B": "O2", "C": "O3", "D": "O4"}, "type": "inline_menu", "text": "Please select one."})
                return dictionary
