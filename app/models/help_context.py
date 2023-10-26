# app/models/help_context.py

from app import db
from .base_model import BaseModel


class HelpContextModel(BaseModel):
    __tablename__ = "help_context"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    context_id = db.Column(db.String(128), nullable=False, unique=True, index=True)
    title = db.Column(db.String(128), nullable=False, unique=True, index=True)
    content = db.Column(db.Text, nullable=False)

    def caption(self):
        return f"{self.title}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "context_id": self.context_id,
                "title": self.title,
                "content": self.content,
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "HelpContextModel":
        instance = super().from_dict(data)
        instance.context_id = data.get("context_id")
        instance.title = data.get("title")
        instance.content = data.get("content")
        return instance

    def __repr__(self) -> str:
        return f"<HelpContextModel id={self.id}, title='{self.title}'>"
