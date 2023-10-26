# app/models/base_model.py

from abc import abstractmethod
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime

from app import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    @declared_attr
    def created(cls):
        return db.Column(db.TIMESTAMP, default=datetime.utcnow)

    @declared_attr
    def created_by_id(cls):
        return db.Column(db.Integer, db.ForeignKey("users.id"))

    @declared_attr
    def modified(cls):
        return db.Column(
            db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow
        )

    @declared_attr
    def modified_by_id(cls):
        return db.Column(db.Integer, db.ForeignKey("users.id"))

    @abstractmethod
    def caption(self):
        pass

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "created": self.created.isoformat(),
            "created_by": self.created_by.to_dict()
            if self.created_by
            else None,  # assuming UserModel model also has to_dict()
            "modified": self.modified.isoformat(),
            "modified_by": self.modified_by.to_dict()
            if self.modified_by
            else None,  # assuming UserModel model also has to_dict()
        }

    @classmethod
    def from_dict(cls, data: dict) -> "BaseModel":
        instance = cls()
        instance.id = data.get("id", None)

        created = data.get("created", None)
        if created:
            try:
                instance.created = datetime.fromisoformat(created)
            except ValueError:
                instance.created = datetime.utcnow()

        instance.created_by_id = data.get("created_by_id", None)

        modified = data.get("modified", None)
        if modified:
            try:
                instance.modified = datetime.fromisoformat(modified)
            except ValueError:
                instance.modified = datetime.utcnow()

        instance.modified_by_id = data.get("modified_by_id", None)

        return instance

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"
