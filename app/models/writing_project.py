# app/models/writing_project.py

from app import db
from datetime import datetime

class WritingProject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f"WritingProject({self.id}, {self.title})"

    def __repr__(self):
        return f'<WritingProject {self.title}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "timestamp": self.timestamp
        }
