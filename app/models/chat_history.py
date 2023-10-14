# models.chat_history.py

from pydantic import BaseModel
from typing import Optional, List
from models import ChatMessage
import uuid

class ChatHistory(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    messages: List[ChatMessage] = []
    
    def add_message(self, message: ChatMessage):
        self.messages.append(message)

    def to_dict(self):
        return {
            "id": self.id,
            "messages": [message.to_dict() for message in self.messages]
        }

    @classmethod
    def from_dict(cls, data):
        history = cls()
        history.id = data["id"]
        history.messages = [ChatMessage.from_dict(msg_data) for msg_data in data["messages"]]
        return history
