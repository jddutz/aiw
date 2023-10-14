# app.routes.user_routes.py

from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/login')
def login():
    # Logic...
    pass