# app/models/writing_project.py

from app import db
from .base_model import BaseModel


collaborators_link = None

reviewers_link = None

collaborators_link = db.Table(
    "collaborators_link",
    db.Column(
        "writing_project_id",
        db.Integer,
        db.ForeignKey("writing_projects.id"),
        primary_key=True,
    ),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
)

reviewers_link = db.Table(
    "reviewers_link",
    db.Column(
        "writing_project_id",
        db.Integer,
        db.ForeignKey("writing_projects.id"),
        primary_key=True,
    ),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
)


class WritingProjectModel(BaseModel):
    __tablename__ = "writing_projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(255), index=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    collaborators = db.relationship(
        "UserModel",
        secondary=collaborators_link,
        lazy="subquery",
        backref=db.backref("writing_projects", lazy=True),
    )
    reviewers = db.relationship(
        "UserModel",
        secondary=reviewers_link,
        lazy="subquery",
        backref=db.backref("reviewing_projects", lazy=True),
    )
    visibility = db.Column(db.String(120), nullable=False)
    project_template_id = db.Column(
        db.Integer, db.ForeignKey("project_templates.id"), nullable=True
    )
    project_type = db.Column(db.String(120), nullable=False)
    tags = db.Column(db.Text, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=True)
    genre = db.relationship(
        "GenreModel", backref=db.backref("writing_projects", lazy=True)
    )

    # Relationship for StoryParts
    stories = db.relationship("StoryPartModel", backref="writing_project", lazy=True)

    def caption(self):
        return f"{self.title}"

    def __str__(self):
        return f"WritingProjectModel({self.id}, {self.title})"

    def __repr__(self):
        return f"<WritingProjectModel {self.title}>"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "title": self.title,
                "description": self.description,
                # Removed 'timestamp' since 'created' is already in the base model's to_dict
            }
        )
        return instance_data
