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
            # Authenticate user (using a hypothetical validate_user function)
            user = user_manager.authenticate_user(
                form.get("username"), form.get("password")
            )
            if user:
                # Set user as logged in
                return redirect(url_for("home"))
            else:
                flash("Invalid username or password", "danger")

        except AuthenticationError as e:
            flash(e.message, "danger")

    # If GET, show login page
    return render_template("login.html")


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            # Create user
            username = form.get("username")
            password = form.get("password")
            user = user_manager.create_user(username, password)
            login_user(user)
            return redirect(url_for("home"))
        except (
            InvalidUsernameError,
            InvalidPasswordError,
            UsernameExistsError,
            EmailExistsError,
        ) as e:
            flash(e.message, "danger")

    # If GET, show sign up page
    return render_template("register.html", form=form)
