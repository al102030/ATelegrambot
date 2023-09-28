from flask import Flask
from config.secrets import TOKEN
from bot.Telegram import Telegram


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = ''
bot_methods = Telegram(TOKEN)

from flaskapp import routes  # noqa: E402
