# models.input_data.py

from typing import Optional
from pydantic import BaseModel

class InputData(BaseModel):
    conversation_id: Optional[str] = None
    project_id: Optional[str] = None
    input: str