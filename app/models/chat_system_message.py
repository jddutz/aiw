# app/models/chat_system_message.py

from app import db
from .base_model import BaseModel


class ChatSystemMessageModel(BaseModel):
    __tablename__ = "chat_system_messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    message_type = db.Column(db.String(50), nullable=True)
    associated_module = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(255), nullable=True)
    version = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    def caption(self):
        return f"Chat System Message {self.id}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "title": self.title,
                "content": self.content,
                "message_type": self.message_type,
                "associated_module": self.associated_module,
                "tags": self.tags,
                "version": self.version,
                "is_active": self.is_active,
                # "created_by_string": self.created_by_string,
                # "updated_by_string": self.updated_by_string
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "ChatSystemMessageModel":
        instance = super().from_dict(data)
        instance.title = data.get("title")
        instance.content = data.get("content")
        instance.message_type = data.get("message_type")
        instance.associated_module = data.get("associated_module")
        instance.tags = data.get("tags")
        instance.version = data.get("version")
        instance.is_active = data.get("is_active", True)
        # If you're using strings for created_by and updated_by, uncomment the next two lines:
        # instance.created_by_string = data.get("created_by_string")
        # instance.updated_by_string = data.get("updated_by_string")
        return instance

    def __repr__(self) -> str:
        return f"<ChatSystemMessageModel id={self.id}, title='{self.title[:20]}'>"
