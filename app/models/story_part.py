# app/models/story_part.py

from enum import Enum

from app import db
from .base_model import BaseModel


class StoryPartType(Enum):
    TEXT = "text"
    COLLECTION = "collection"
    IMAGE = "image"
    IMAGEREF = "imageref"


class StoryPartModel(BaseModel):
    __tablename__ = "story_parts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Foreign key linking back to WritingProjectModel
    writing_project_id = db.Column(
        db.Integer, db.ForeignKey("writing_projects.id"), nullable=False
    )

    parent_id = db.Column(db.Integer, db.ForeignKey("story_parts.id"), nullable=True)
    children = db.relationship(
        "StoryPartModel",
        back_populates="parent",
        lazy="dynamic",
    )
    parent = db.relationship(
        "StoryPartModel",
        back_populates="children",
        remote_side=[id],
    )

    # Attributes for the StoryPartModel
    part_type = db.Column(
        db.Enum(StoryPartType), default=StoryPartType.TEXT, nullable=False
    )
    title = db.Column(db.String(120), nullable=False)
    summary = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=True)

    def caption(self):
        return f"{self.title}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "writing_project_id": self.writing_project_id,
                "parent_id": self.parent_id,
                "children": [child.to_dict() for child in self.children],
                "part_type": self.part_type.value,
                "title": self.title,
                "summary": self.summary,
                "content": self.content,
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "StoryPartModel":
        instance = super().from_dict(data)

        instance.writing_project_id = data.get("writing_project_id", None)
        instance.parent_id = data.get("parent_id", None)

        try:
            instance.part_type = StoryPartType(data.get("part_type"))
        except ValueError:
            instance.part_type = None

        instance.title = data.get("title", "")
        instance.summary = data.get("summary", None)
        instance.content = data.get("content", None)

        return instance
