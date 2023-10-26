# app/models/user.py

from app import db
from flask_login import UserMixin
from sqlalchemy import event
from datetime import datetime
import bcrypt


class UserModel(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=True, unique=True, index=True)
    username_normalized = db.Column(db.String(50), index=True)
    email = db.Column(db.String(255), nullable=True, unique=True, index=True)
    email_normalized = db.Column(db.String(255), index=True)
    pw_hash = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    is_active = db.Column(db.Boolean, default=True)
    is_email_verified = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime, nullable=True)
    failed_login_count = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.pw_hash.encode("utf-8"))


# This will automatically set the normalized fields before inserting a new record.
@event.listens_for(UserModel, "before_insert")
def set_normalized_fields_before_insert(mapper, connection, user):
    user.username_normalized = user.username.lower() if user.username else None
    user.email_normalized = user.email.lower() if user.email else None


# This will automatically set the normalized fields before updating an existing record.
@event.listens_for(UserModel, "before_update")
def set_normalized_fields_before_update(mapper, connection, user):
    user.username_normalized = user.username.lower() if user.username else None
    user.email_normalized = user.email.lower() if user.email else None
