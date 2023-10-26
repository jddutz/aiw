# app/models/genre.py

from app import db
from .base_model import BaseModel


class GenreModel(BaseModel):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    imageref = db.Column(db.String(255))

    def caption(self):
        return f"{self.name}"

    def to_dict(self) -> dict:
        instance_data = super().to_dict()
        instance_data.update(
            {
                "name": self.name,
                "description": self.description,
                "imageref": self.imageref,
            }
        )
        return instance_data

    @classmethod
    def from_dict(cls, data: dict) -> "GenreModel":
        genre_model = super().from_dict(data)
        genre_model.name = data.get("name", "")
        genre_model.description = data.get("description", "")
        genre_model.imageref = data.get("imageref", "")
        return genre_model

    def __repr__(self) -> str:
        return f"<GenreModel id={self.id}, name='{self.name}'>"
