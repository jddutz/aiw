# app.routes module __init__.py

from flask import render_template, redirect, url_for, request
from app import app
from app.models import WritingProject
from app.routes.user_routes import user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/user')
from app.routes.user_routes import user_blueprint
from app.routes.project_routes import project_blueprint

app.register_blueprint(project_blueprint, url_prefix='/project')

@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    PER_PAGE = 10
    projects = WritingProject.query.paginate(page, PER_PAGE, False).items
    return render_template('index.html', projects=projects, page=page)


