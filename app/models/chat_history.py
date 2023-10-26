# app/models/chat_history.py

from app import db
from .base_model import BaseModel
from .chat_message import ChatMessageModel  # Ensure you import the correct model name


class ChatHistoryModel(BaseModel):
    __tablename__ = "chat_histories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    messages = db.relationship("ChatMessageModel", backref="chat_history", lazy=True)

    def add_message(self, message: ChatMessageModel):
        message.chat_history_id = self.id
        self.messages.append(message)

    def caption(self):
        return f"Chat History {self.id}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data["messages"] = [message.to_dict() for message in self.messages]
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "ChatHistoryModel":
        instance = super(ChatHistoryModel, cls).from_dict(data)

        instance.messages = [
            ChatMessageModel.from_dict(msg_data)
            for msg_data in data.get("messages", [])
        ]

        return instance

    def __repr__(self) -> str:
        return f"<ChatHistoryModel id={self.id}, messages_count={len(self.messages)}>"
