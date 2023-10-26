# app/models/chat_message.py

from app import db
from .base_model import BaseModel
from enum import Enum


class RoleEnum(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class VisibilityEnum(Enum):
    VISIBLE_TO_ALL = "all"
    VISIBLE_TO_COLLABORATORS = "collaborators"


class ChatMessageModel(BaseModel):
    __tablename__ = "chat_messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    role = db.Column(db.Enum(RoleEnum), nullable=True)
    content = db.Column(db.Text, nullable=True)
    chat_history_id = db.Column(
        db.Integer, db.ForeignKey("chat_histories.id"), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    visibility = db.Column(
        db.Enum(VisibilityEnum),
        default=VisibilityEnum.VISIBLE_TO_ALL,
    )

    def caption(self):
        return f"Chat Message {self.id}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "role": self.role.value if self.role else None,
                "content": self.content,
                "chat_history_id": self.chat_history_id,
                "user_id": self.user_id,
                "visibility": self.visibility.value if self.visibility else None,
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "ChatMessageModel":
        instance = super().from_dict(data)

        try:
            instance.role = RoleEnum(data.get("role"))
        except ValueError:
            instance.role = None

        instance.content = data.get("content", "")
        instance.chat_history_id = data.get("chat_history_id")
        instance.user_id = data.get("user_id")

        try:
            instance.visibility = VisibilityEnum(data.get("visibility"))
        except ValueError:
            instance.visibility = None

        return instance

    def __repr__(self) -> str:
        return f"<ChatMessageModel id={self.id}, content='{self.content[:20]}'>"
