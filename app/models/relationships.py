# app/models/relationships.py

from app import db


project_template_tags_link = db.Table(
    "project_template_tags",
    db.Column(
        "project_template_id",
        db.Integer,
        db.ForeignKey("project_template.id"),
        primary_key=True,
    ),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)

project_template_genres_link = db.Table(
    "project_template_genres",
    db.Column(
        "project_template_id",
        db.Integer,
        db.ForeignKey("project_template.id"),
        primary_key=True,
    ),
    db.Column("genre_id", db.Integer, db.ForeignKey("genre.id"), primary_key=True),
)

writing_project_tags_link = db.Table(
    "writing_project_tags",
    db.Column(
        "writing_project_id",
        db.Integer,
        db.ForeignKey("writing_project.id"),
        primary_key=True,
    ),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)

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
