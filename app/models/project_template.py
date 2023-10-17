# app/models/project_template.py

import json
from datetime import datetime

from app import db
from app.models.relationships import (
    project_template_tags_link,
    project_template_genres_link,
)


class ProjectTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    methodology = db.Column(db.Text, nullable=False)
    length = db.Column(db.String(255), nullable=False)
    tags = db.relationship(
        "Tag",
        secondary="project_template_tags",
        back_populates="project_templates",
    )
    genres = db.relationship(
        "Genre",
        secondary="project_template_genres",
        back_populates="project_templates",
    )
    links = db.Column(db.Text, nullable=False)

    structure = db.Column(db.Text, nullable=True)  # Stores serialized JSON structure

    imageref = db.Column(db.String(255))
    created = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    modified = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    usage_count = db.Column(db.Integer, default=0)

    def set_structure(self, structure_dict):
        self.structure = json.dumps(structure_dict)

    def get_structure(self):
        return json.loads(self.structure) if self.structure else {}

    def set_links(self, links_list):
        self.links = ";".join(links_list)

    def get_links(self):
        return self.links.split(";") if self.links else []
