# app/models/chat_message.py

from app import db
from datetime import datetime

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(50), nullable=True)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    chat_history_id = db.Column(db.Integer, db.ForeignKey('chat_history.id'), nullable=False)

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
        chat_message.role = data.get("role")
        chat_message.content = data.get("content")
        chat_message.created_at = datetime.fromisoformat(data["created_at"])
        return chat_message
