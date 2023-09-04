
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
                user_hash = (text.strip()).replace("/start", "")
                if user_hash != "":
                    response = requests.post(
                        f"{LOCALHOST}/token", params=params, timeout=20)
                    if response.text != "Not allowed!":
                        user_select_keyboard = list_maker(
                            response.json()["menu"])
                        bot_methods.send_message_with_menu(
                            response.json()["greet"], chat_id, user_select_keyboard)
                    else:
                        print("Wrong User!")
                        bot_methods.send_message(
                            "Wrong URL. Your access code is incorrect!.", chat_id)
                else:
                    print("Not premium user!")
                    bot_methods.send_message(
                        "Wrong URL. To access the bot options, please connect with us.\nThank you.", chat_id)
        return Response('ok', status=200)
    else:
        return render_template("home.html")


@app.route("/token", methods=["GET", "POST"])
def token():
    if request.method == 'POST':
        text = request.args.get('text')
        params = {
            "text": text,
        }
        response = requests.post(
            f"{LOCALHOST}/server", params=params, timeout=20)
        if response.text != "empty":
            return response.json()
        else:
            return "Not allowed!"


@app.route("/server", methods=["GET", "POST"])
def server():
    if request.method == 'POST':
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
            {"menu": {"1": "A", "2": "B", "3": "C", "4": "D"}, "greet": greet_text1})
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


@app.route("/greet", methods=["GET", "POST"])
def greet():
    pass
