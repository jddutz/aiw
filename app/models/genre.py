# app/models/genre.py

from app import db
from app.models.relationships import project_template_genres_link


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    imageref = db.Column(db.String(255))
    project_templates = db.relationship(
        "ProjectTemplate",
        secondary=project_template_genres_link,
        back_populates="genres",
    )
