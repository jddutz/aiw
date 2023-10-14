# models.chat_history.py

from app import db
from models import ChatMessage

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    messages = db.relationship('ChatMessage', backref='chat_history', lazy=True)

    def add_message(self, message: ChatMessage):
        message.chat_history_id = self.id
        self.messages.append(message)

    def to_dict(self):
        return {
            "id": self.id,
            "messages": [message.to_dict() for message in self.messages]
        }

    @classmethod
    def from_dict(cls, data):
        history = cls()
        history.messages = [ChatMessage.from_dict(msg_data) for msg_data in data["messages"]]
        return history
