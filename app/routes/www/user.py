# app/routes/www/user.py

from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from flask_login import login_user, login_required, current_user
from app.services import (
    user_manager,
    notification_manager,
    activity_manager,
    project_manager,
)
from app.exceptions import (
    AuthenticationError,
    InvalidUsernameError,
    InvalidPasswordError,
    UsernameExistsError,
    EmailExistsError,
)


from app.forms import LoginForm, RegistrationForm

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        try:
            # Authenticate user (using a hypothetical authenticate_user function)
            username = form.username.data
            password = form.password.data
            user = user_manager.authenticate_user(username, password)
            if user:
                login_user(
                    user
                )  # Make sure you also call login_user() to log the user in
                return redirect(url_for("home"))
            else:
                flash("Invalid username or password", "danger")
        except AuthenticationError as e:
            flash(e.message, "danger")

    # If GET, show login page
    return render_template("user/login.html", form=form)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            # Create user
            username = form.username.data
            password = form.password.data
            user = user_manager.create_user(username, password)
            login_user(user)
            return redirect(url_for("home"))
        except InvalidUsernameError as e:
            flash(f"Invalid username: {e.message}", "danger")
        except InvalidPasswordError as e:
            flash(f"Invalid password: {e.message}", "danger")
        except UsernameExistsError as e:
            flash(f"Username already exists: {e.message}", "danger")
        except EmailExistsError as e:
            flash(f"Email already exists: {e.message}", "danger")

    # If GET, show sign up page
    return render_template("user/register.html", form=form)
