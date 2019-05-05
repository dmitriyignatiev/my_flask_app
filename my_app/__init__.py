from flask import Flask, render_template, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
mail = Mail(app)

from my_app import routes, models


