# models.chat_message.py

from app import db
from typing import Optional

from datetime import datetime
import uuid

class ChatMessage(db.Model):
    id: Optional[str] = str(uuid.uuid4())
    role: Optional[str] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        chat_message = cls()
        chat_message.id = data["id"]
        chat_message.role = data["role"]
        chat_message.content = data["content"]
        chat_message.created_at = datetime.fromisoformat(data["created_at"])
        return chat_message
