# app/models/story_part.py

from app import db
from app.models.relationships import storypart_collection_link


class StoryPart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Foreign key linking back to WritingProject
    writing_project_id = db.Column(
        db.Integer, db.ForeignKey("writing_project.id"), nullable=False
    )

    # Self-referential relationship for nested story parts
    parent_id = db.Column(db.Integer, db.ForeignKey("story_part.id"), nullable=True)
    children = db.relationship(
        "StoryPart", backref=db.backref("parent", remote_side=[id]), lazy="dynamic"
    )

    # Attributes for the StoryPart
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=True)  # the content of the story part
    imageref = db.Column(db.String(255), nullable=True)  # image reference

    # Relationship with Collections (assuming a story part can belong to multiple collections)
    collections = db.relationship(
        "StoryPartCollection",
        secondary="storypart_collection_link",
        back_populates="story_parts",
    )

    created = db.Column(db.DateTime, index=True, default=db.func.now())
    last_modified = db.Column(
        db.DateTime, index=True, default=db.func.now(), onupdate=db.func.now()
    )

    def __str__(self):
        return f"StoryPart({self.id}, {self.title})"

    def __repr__(self):
        return f"<StoryPart {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "writing_project_id": self.writing_project_id,
            "parent_id": self.parent_id,
            "created": self.created,
            "last_modified": self.last_modified,
        }
