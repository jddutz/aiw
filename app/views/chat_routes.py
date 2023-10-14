from flask import Blueprint

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/')
def login():
    # Logic...
    pass