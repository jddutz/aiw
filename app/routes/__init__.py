# app.routes module __init__.py

from flask import render_template, redirect, url_for, request
from app import flask_app
from app.models import WritingProject

# UI blueprints
from app.routes.webui.user import user_blueprint
from app.routes.webui.chat import chat_blueprint
from app.routes.webui.project import project_blueprint
flask_app.register_blueprint(user_blueprint, url_prefix='/user')
flask_app.register_blueprint(chat_blueprint, url_prefix='/chat')
flask_app.register_blueprint(project_blueprint, url_prefix='/project')

# API blueprints
from app.routes.api.v1.user_api_v1 import user_api_v1
from app.routes.api.v1.chat_api_v1 import chat_api_v1
from app.routes.api.v1.project_api_v1 import project_api_v1
flask_app.register_blueprint(user_api_v1, url_prefix='/api/v1/user')
flask_app.register_blueprint(chat_api_v1, url_prefix='/api/v1/chat')
flask_app.register_blueprint(project_api_v1, url_prefix='/api/v1/project')

# Home/index page
@flask_app.route('/')
def index():
    PER_PAGE = 10
    page = request.args.get('page', default=1, type=int)
    projects = WritingProject.query.paginate(page=page, per_page=PER_PAGE, error_out=False).items
    return render_template('index.html', projects=projects, page=page)
