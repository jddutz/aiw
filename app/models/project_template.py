# app/models/project_template.py

import json
from app import db
from .base_model import BaseModel
from .genre import GenreModel


project_template_genres = db.Table(
    "project_template_genres",
    db.Column("project_template_id", db.Integer, db.ForeignKey("project_templates.id")),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id")),
)


class ProjectTemplateModel(BaseModel):
    __tablename__ = "project_templates"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    category = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    methodology = db.Column(db.Text, nullable=False)
    length = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.Text, nullable=True)
    genres = db.relationship(
        "GenreModel",
        secondary="project_template_genres",
        lazy="subquery",
        backref=db.backref("project_templates", lazy=True),
    )
    links = db.Column(db.Text, nullable=False)
    structure = db.Column(db.Text, nullable=True)  # Stores serialized JSON structure
    imageref = db.Column(db.String(255))
    usage_count = db.Column(db.Integer, default=0)

    def set_structure(self, structure_dict):
        self.structure = json.dumps(structure_dict)

    def get_structure(self):
        return json.loads(self.structure) if self.structure else {}

    def set_links(self, links_list):
        self.links = ";".join(links_list)

    def get_links(self):
        return self.links.split(";") if self.links else []

    def set_tags(self, tags_list):
        self.tags = ";".join(tags_list)

    def get_tags(self):
        return self.tags.split(";") if self.tags else []

    def caption(self):
        return f"{self.title}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "category": self.category,
                "title": self.title,
                "description": self.description,
                "methodology": self.methodology,
                "length": self.length,
                "tags": self.get_tags(),
                "genres": [genre.to_dict() for genre in self.genres],
                "links": self.get_links(),
                "structure": self.get_structure(),
                "imageref": self.imageref,
                "usage_count": self.usage_count,
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "ProjectTemplateModel":
        instance = super().from_dict(data)
        instance.category = data.get("category", "")
        instance.title = data.get("title", "")
        instance.description = data.get("description", "")
        instance.methodology = data.get("methodology", "")
        instance.length = data.get("length", "")
        instance.set_tags(data.get("tags", []))
        instance.genres = [
            GenreModel.from_dict(genre) for genre in data.get("genres", [])
        ]
        instance.set_links(data.get("links", []))
        instance.set_structure(data.get("structure", {}))
        instance.imageref = data.get("imageref", "")
        instance.usage_count = data.get("usage_count", 0)
        return instance

    def __repr__(self) -> str:
        return f"<ProjectTemplateModel id={self.id}, name={self.title}>"
