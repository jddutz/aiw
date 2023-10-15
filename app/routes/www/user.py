# app/routes/www/user.py

from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from flask_login import login_required, current_user
from app.models.user import User
from app.services.user_manager import (
    create_user,
    authenticate_user,
)
from app.exceptions import (
    AuthenticationError,
    InvalidUsernameError,
    InvalidPasswordError,
    UsernameExistsError,
    EmailExistsError,
)


from app.forms import RegistrationForm

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["GET"])
@login_required
def home():
    return render_template("dashboard.html")


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    # If POST, handle login logic
    if request.method == "POST":
        try:
            # Authenticate user (using a hypothetical validate_user function)
            user = authenticate_user(
                request.form.get("username"), request.form.get("password")
            )
            if user:
                # Set user as logged in
                return redirect(url_for("user.home"))
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
            username = request.form.get("username")
            password = request.form.get("password")
            user = create_user(username, password)
            # Set user as logged in
            return redirect(url_for("user.home"))
        except (
            InvalidUsernameError,
            InvalidPasswordError,
            UsernameExistsError,
            EmailExistsError,
        ) as e:
            flash(e.message, "danger")

    # If GET, show sign up page
    return render_template("register.html", form=form)
