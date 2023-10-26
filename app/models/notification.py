# app/models/notification.py

# app/models/notification.py

from app import db
from .base_model import BaseModel


class NotificationModel(BaseModel):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    notification_type = db.Column(db.String(120), nullable=False, default="general")
    status = db.Column(db.String(50), nullable=False, default="unread")

    def caption(self):
        return f"NotificationModel {self.notification_type} {self.id}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "user_id": self.user_id,
                "message": self.message,
                "notification_type": self.notification_type,
                "status": self.status,
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "NotificationModel":
        notification = super().from_dict(data)
        notification.user_id = data.get("user_id")
        notification.message = data.get("message", "")
        notification.notification_type = data.get("notification_type", "general")
        notification.status = data.get("status", "unread")
        return notification

    def __repr__(self):
        return f"<NotificationModel {self.message}>"
