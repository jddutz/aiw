# models.input_data.py

from app import db
from typing import Optional

class InputData(db.Model):
    conversation_id: Optional[str] = None
    project_id: Optional[str] = None
    input: str