# app/services/user_manager.py

import re
from datetime import datetime

from flask import session
from flask_login import login_user, logout_user

from app.exceptions import (
    InvalidPasswordError,
    InvalidUsernameError,
    UsernameExistsError,
    EmailExistsError,
    AuthenticationError,
)
from app.models.user import User
from app import login_manager, db


def validate_username(username):
    if not username or not isinstance(username, str):
        return False
    # Check length
    if not (3 <= len(username) <= 50):
        return False
    # Alphanumeric check
    if not re.match("^[a-zA-Z0-9]*$", username):
        return False
    return True


def validate_email(email):
    if not email or not isinstance(email, str):
        return False
    # Basic email regex check
    if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    return True


def validate_password(password):
    if not password or not isinstance(password, str):
        return False
    # Minimum length check
    if len(password) < 8:
        return False
    # At least one uppercase letter
    if not any(c.isupper() for c in password):
        return False
    # At least one lowercase letter
    if not any(c.islower() for c in password):
        return False
    # At least one digit
    if not any(c.isdigit() for c in password):
        return False
    # At least one special character
    special_characters = "!@#$%^&*()_-+=<>?/"
    if not any(c in special_characters for c in password):
        return False
    return True


def username_exists(username):
    normalized = username.lower()
    return User.query.filter_by(username=normalized).first() is not None


def email_exists(email):
    normalized = email.lower()
    return User.query.filter_by(email=normalized).first() is not None


def create_user(username_or_email, password):
    if not validate_username(username_or_email):
        raise InvalidUsernameError(username_or_email)

    username = username_or_email.lower()

    if username_exists(username):
        raise UsernameExistsError(username)

    email = username if validate_email(username) else None

    if email and email_exists(email):
        raise EmailExistsError(email)

    if not validate_password(password):
        raise InvalidPasswordError()

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    # TODO: Log the user creation event

    return user


@login_manager.user_loader
def load_user(user_id):
    # User.id is an int
    # Flask-Login uses a string
    # converting to int before querying the database
    # will throw an exception if user_id is not valid
    return User.query.get(int(user_id))


def get_user_by_username(username):
    if not validate_username(username):
        return None
    return User.query.filter_by(username=username.lower()).first()


def get_user_by_email(email):
    if not validate_email(email):
        return None
    return User.query.filter_by(email=email.lower()).first()


def authenticate_user(username_or_email, password):
    try:
        user = get_user_by_username(username_or_email)

        if not user:
            user = get_user_by_email(username_or_email)

        if user:
            if user.check_password(password):
                login(user)
                return user
            else:
                user.failed_login_count += 1
                db.session.commit()

    except Exception as e:
        # TODO: Log the exception
        print(e)

    # We don't want to give any information about why the authentication failed
    # so just raise a generic AuthenticationError
    raise AuthenticationError()


def update_username(user, username):
    if not validate_username(username):
        return False
    if username_exists(username):
        return False
    user.username = username.lower()
    db.session.commit()

    # TODO: Log the username change event

    return True


def update_email(user, email):
    if not validate_email(email):
        return False
    if email_exists(email):
        return False
    user.email = email.lower()
    db.session.commit()

    # TODO: Log the email change event

    return True


def update_password(user, password):
    if not validate_password(password):
        return False
    user.set_password(password)
    db.session.commit()

    # TODO: Log the password change event

    return True


def reset_password(user):
    # TODO: Implement password reset
    pass


def activate_user(user):
    user.is_active = True
    db.session.commit()

    # TODO: Log the activation event


def deactivate_user(user):
    user.is_active = False
    db.session.commit()

    # TODO: Log the deactivation event


def login(user):
    user.failed_login_count = 0
    user.last_login = datetime.utcnow()
    db.session.commit()
    login_user(user)

    # TODO: Log the login event


def logout(user):
    logout_user()

    # TODO: Log the logout event
