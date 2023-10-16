# app/models/activity.py

from app import db
from datetime import datetime


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    entity_type = db.Column(
        db.String(120), nullable=True
    )  # e.g., 'WritingProject', 'StoryPart'
    entity_id = db.Column(db.Integer, nullable=True)  # The ID of the associated entity
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Activity {self.description}>"
