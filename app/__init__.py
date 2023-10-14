# app module __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="johndutz",
    password="03132012",
    hostname="johndutz.mysql.pythonanywhere-services.com",
    databasename="johndutz$aiw",
)
flask_app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
flask_app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(flask_app)

import app.routes
