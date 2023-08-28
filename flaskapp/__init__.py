from flask import Flask
from config.secrets import TOKEN
from bot.Telegram import Telegram


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '876f18f346759c935f2d390e313edd93'
bot_methods = Telegram(TOKEN)

from flaskapp import routes  # noqa: E402
