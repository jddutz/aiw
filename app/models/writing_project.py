# app/models/writing_project.py

from app import db
from datetime import datetime
from .relationships import collaborators_link, reviewers_link


class WritingProject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    collaborators = db.relationship(
        "User",
        secondary=collaborators_link,
        lazy="subquery",
        backref=db.backref("writing_projects", lazy=True),
    )
    reviewers = db.relationship(
        "User",
        secondary=reviewers_link,
        lazy="subquery",
        backref=db.backref("reviewing_projects", lazy=True),
    )
    visibility = db.Column(db.String(120), nullable=False)
    project_template_id = db.Column(
        db.Integer, db.ForeignKey("project_template.id"), nullable=True
    )
    project_type = db.Column(db.String(120), nullable=False)
    tags = db.relationship(
        "Tag",
        secondary="writing_project_tags",
        back_populates="writing_projects",
    )
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=True)
    genre = db.relationship("Genre", backref=db.backref("writing_projects", lazy=True))

    # Relationship for StoryParts (no need to mention foreign key here as it's already handled in StoryPart model)
    stories = db.relationship("StoryPart", backref="writing_project", lazy=True)

    # Relationship for Collections
    collections = db.relationship(
        "StoryPartCollection", backref="writing_project", lazy=True
    )

    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f"WritingProject({self.id}, {self.title})"

    def __repr__(self):
        return f"<WritingProject {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "timestamp": self.created,  # Updating timestamp to 'created' as it seems more accurate.
        }
