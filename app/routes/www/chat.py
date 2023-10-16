# app/routes/www/chat.py

from flask import Blueprint

from typing import Optional
from pydantic import BaseModel

chat_blueprint = Blueprint("chat", __name__)


class InputData(BaseModel):
    conversation_id: Optional[str] = None
    project_id: Optional[str] = None
    input: str
