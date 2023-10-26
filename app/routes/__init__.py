# app/routes/__init__.py

from flask import session, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import flask_app

from app.services import (
    notification_manager,
    project_manager,
)

# Admin area blueprints
from app.routes.admin.help_context import blueprint as help_context_blueprint
from app.routes.admin.system_message import blueprint as system_message_blueprint
from app.routes.admin.genre import blueprint as genre_blueprint
from app.routes.admin.project_template import blueprint as project_template_blueprint

flask_app.register_blueprint(help_context_blueprint, url_prefix="/admin/help_context")
flask_app.register_blueprint(
    system_message_blueprint, url_prefix="/admin/system_message"
)
flask_app.register_blueprint(genre_blueprint, url_prefix="/admin/genre")
flask_app.register_blueprint(
    project_template_blueprint, url_prefix="/admin/project_template"
)


# UI blueprints
from app.routes.www.user import user_blueprint
from app.routes.www.project import blueprint as project_blueprint
from app.routes.www.story import story_blueprint

flask_app.register_blueprint(user_blueprint, url_prefix="/user")
flask_app.register_blueprint(project_blueprint, url_prefix="/project")
flask_app.register_blueprint(story_blueprint, url_prefix="/story")

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
    if current_user.is_authenticated:
        # If the user is authenticated, redirect them to the home/dashboard page
        return redirect(url_for("home"))
    else:
        # If the user is not authenticated, render the landing page
        return render_template("landing_page.html")


@flask_app.route("/home", methods=["GET"])
@login_required
def home():
    user_id = current_user.id  # Assuming you're using Flask-Login's current_user

    # Gather notifications using the service
    notifications = notification_manager.get_notifications_for_user(user_id, limit=10)

    # Gather projects using the service
    projects = project_manager.get_recent_projects_for_user(user_id, limit=10)

    return render_template(
        "dashboard.html",
        notifications=notifications,
        projects=projects,
    )


@flask_app.route("/admin", methods=["GET"])
@login_required
def admin():
    # If the user is not authenticated, render the landing page
    return render_template("admin/home.html")
