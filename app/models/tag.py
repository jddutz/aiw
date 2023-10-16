# app/models/tag.py

from app import db
from app.models.relationships import project_template_tags_link


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    project_templates = db.relationship(
        "ProjectTemplate",
        secondary=project_template_tags_link,
        back_populates="tags",
    )
