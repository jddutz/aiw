# app/models/chat_history.py

from app import db
from .chat_message import ChatMessage
from datetime import datetime


class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Association with WritingProject
    writing_project_id = db.Column(
        db.Integer, db.ForeignKey("writing_project.id"), nullable=True
    )

    # Messages related to this chat history
    messages = db.relationship("ChatMessage", backref="chat_history", lazy=True)

    # Timestamps
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_modified = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def add_message(self, message: ChatMessage):
        message.chat_history_id = self.id
        self.messages.append(message)

    def to_dict(self):
        return {
            "id": self.id,
            "messages": [message.to_dict() for message in self.messages],
        }

    @classmethod
    def from_dict(cls, data):
        history = cls()
        history.messages = [
            ChatMessage.from_dict(msg_data) for msg_data in data["messages"]
        ]
        return history
