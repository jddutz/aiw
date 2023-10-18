# app/__init__.py

import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = Flask(__name__)
flask_app.secret_key = os.getenv("AIW_FLASK_SECRET_KEY", None)

app_env = os.getenv(
    "APP_ENV", "PROD"
)  # default to 'PROD', set APP_ENV var to 'DEV' for local development

if app_env == "DEV":
    mysql_user = "root"
    mysql_hostname = "localhost"
    mysql_dbname = "aiw"
else:  # PROD
    mysql_user = "johndutz"
    mysql_hostname = "johndutz.mysql.pythonanywhere-services.com"
    mysql_dbname = "johndutz$aiw"

mysql_password = os.getenv("AIW_MYSQL_PASSWORD", None)

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_hostname}/{mysql_dbname}"

flask_app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
flask_app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.init_app(flask_app)

# Initialize OpenAI API
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", None)

import app.routes
