# app.routes module __init__.py

from flask import render_template, redirect, url_for, request
from app import flask_app
from app.models import WritingProject
from app.routes.user_routes import user_blueprint

flask_app.register_blueprint(user_blueprint, url_prefix='/user')
from app.routes.user_routes import user_blueprint
from app.routes.project_routes import project_blueprint

flask_app.register_blueprint(project_blueprint, url_prefix='/project')

@flask_app.route('/')
@flask_app.route('/page/<int:page>')
def index(page=1):
    PER_PAGE = 10
    projects = WritingProject.query.paginate(page=page, per_page=PER_PAGE, error_out=False).items
    return render_template('index.html', projects=projects, page=page)


