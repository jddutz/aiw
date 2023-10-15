# app/db/conversations.py

import SQLAlchemy

from typing import Dict, List
from models import ChatHistory

TABLE_NAME = "conversations"

def get_or_create(conversation_id: str) -> ChatHistory:
    data = load_data(TABLE_NAME, lambda x: x["id"] == conversation_id)
    if len(data) == 0:
        chat_history = ChatHistory()
        save_data(TABLE_NAME, chat_history.to_dict())
        return chat_history
    else:
        return ChatHistory.from_dict(data[0])

def get(conversation_id: str) -> ChatHistory:
    data = load_data(TABLE_NAME, lambda x: x["id"] == conversation_id)
    if len(data) == 0:
        raise Exception(f"Conversation with ID {conversation_id} not found.")
    elif len(data) > 1:
        raise Exception(f"Multiple conversations with ID {conversation_id} found.")
    else:
        return ChatHistory.from_dict(data[0])

def save(conversation: ChatHistory):
    save_data(TABLE_NAME, conversation.to_dict())
