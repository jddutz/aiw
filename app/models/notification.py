# app/models/notification.py

from app import db
from datetime import datetime


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    notification_type = db.Column(db.String(120), nullable=False, default="general")
    status = db.Column(
        db.String(50), nullable=False, default="unread"
    )  # or use Boolean
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_modified = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Notification {self.message}>"
