# app/models/chat_message.py

from app import db
from datetime import datetime
from sqlalchemy import Enum


class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    ROLES = (USER, ASSISTANT, SYSTEM)

    role = db.Column(Enum(*ROLES, name="role_types"), nullable=True)

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    ROLES = (USER, ASSISTANT, SYSTEM)

    role = db.Column(Enum(*ROLES, name="role_types"), nullable=True)

    content = db.Column(db.Text, nullable=True)

    # Timestamp for the message
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign keys
    chat_history_id = db.Column(
        db.Integer, db.ForeignKey("chat_history.id"), nullable=False
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=True
    )  # Associate with the sender

    VISIBLE_TO_ALL = "all"
    VISIBLE_TO_COLLABORATORS = "collaborators"
    VISIBILITY_CHOICES = (VISIBLE_TO_ALL, VISIBLE_TO_COLLABORATORS)

    visibility = db.Column(
        Enum(*VISIBILITY_CHOICES, name="visibility_types"), default=VISIBLE_TO_ALL
    )

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role,
            "content": self.content,
            "created_at": self.created_at.isoformat() if self.created_at else "",
            "visibility": self.visibility,
        }

    @classmethod
    def from_dict(cls, data):
        chat_message = cls()
        chat_message.role = data.get("role")
        chat_message.content = data.get("content")
        chat_message.created_at = datetime.fromisoformat(data["created_at"])
        chat_message.visibility = data.get("visibility", cls.VISIBLE_TO_ALL)
        return chat_message
