# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = Flask(__name__)
flask_app.secret_key = os.getenv('AIW_FLASK_SECRET_KEY', None)

mysql_password = os.getenv('AIW_MYSQL_PASSWORD', None)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="johndutz",
    password=mysql_password,
    hostname="johndutz.mysql.pythonanywhere-services.com",
    databasename="johndutz$aiw",
)
flask_app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
flask_app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

import app.routes
