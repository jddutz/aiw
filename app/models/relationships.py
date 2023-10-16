# app/models/relationships.py

from app import db

collaborators_link = db.Table(
    "collaborators",
    db.Column(
        "writing_project_id",
        db.Integer,
        db.ForeignKey("writing_project.id"),
        primary_key=True,
    ),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)

reviewers_link = db.Table(
    "reviewers",
    db.Column(
        "writing_project_id",
        db.Integer,
        db.ForeignKey("writing_project.id"),
        primary_key=True,
    ),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)


storypart_collection_link = db.Table(
    "storypart_collection_link",
    db.Column(
        "story_part_id", db.Integer, db.ForeignKey("story_part.id"), primary_key=True
    ),
    db.Column(
        "collection_id", db.Integer, db.ForeignKey("collection.id"), primary_key=True
    ),
)
