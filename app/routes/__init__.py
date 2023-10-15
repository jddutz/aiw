# app/routes/__init__.py

from flask import session, render_template, redirect, url_for, request
from app import flask_app
from app.models import User, WritingProject

# UI blueprints
from app.routes.www.user import user_blueprint
from app.routes.www.chat import chat_blueprint
from app.routes.www.project import project_blueprint

flask_app.register_blueprint(user_blueprint, url_prefix="/user")
flask_app.register_blueprint(chat_blueprint, url_prefix="/chat")
flask_app.register_blueprint(project_blueprint, url_prefix="/project")

# API blueprints
from app.routes.api.v1.user import user_api_v1
from app.routes.api.v1.chat import chat_api_v1
from app.routes.api.v1.project import project_api_v1

flask_app.register_blueprint(user_api_v1, url_prefix="/api/v1/user")
flask_app.register_blueprint(chat_api_v1, url_prefix="/api/v1/chat")
flask_app.register_blueprint(project_api_v1, url_prefix="/api/v1/project")


# Home/index page
@flask_app.route("/")
def index():
    # Check if user_id is in session
    if not session.get("user_id"):
        # If user_id is not in session, render the landing page
        return render_template("landing_page.html")

    # If user_id is in session, continue to load projects and render the index page
    PER_PAGE = 10
    page = request.args.get("page", default=1, type=int)
    projects = WritingProject.query.paginate(
        page=page, per_page=PER_PAGE, error_out=False
    ).items
    return render_template("index.html", projects=projects, page=page)
