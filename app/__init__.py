from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://johndutz:password@localhost/johndutz$mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Avoid importing routes or models here
