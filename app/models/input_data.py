# models.input_data.py

from pydantic import BaseModel
from typing import Optional

class InputData(BaseModel):
    conversation_id: Optional[str] = None
    project_id: Optional[str] = None
    input: str