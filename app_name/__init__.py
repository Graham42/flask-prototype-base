from flask import Flask

app = Flask(__name__)
app.config.from_object('app_name.default_config')

from app_name import views
