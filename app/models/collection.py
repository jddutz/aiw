# app/models/collection.py

from app import db
from app.models.relationships import storypart_collection_link


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Foreign key linking back to WritingProject
    writing_project_id = db.Column(
        db.Integer, db.ForeignKey("writing_project.id"), nullable=False
    )

    # Attributes for the Collection
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship with StoryParts
    story_parts = db.relationship(
        "StoryPart",
        secondary="storypart_collection_link",
        back_populates="collections",
    )

    created = db.Column(db.DateTime, index=True, default=db.func.now())
    last_modified = db.Column(
        db.DateTime, index=True, default=db.func.now(), onupdate=db.func.now()
    )

    def __str__(self):
        return f"Collection({self.id}, {self.title})"

    def __repr__(self):
        return f"<Collection {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "writing_project_id": self.writing_project_id,
            "created": self.created,
            "last_modified": self.last_modified,
        }
