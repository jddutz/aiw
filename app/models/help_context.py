# app/models/help_context.py

from app import db


class HelpContext(db.Model):
    __tablename__ = "help_context"

    id = db.Column(db.Integer, primary_key=True)
    context_id = db.Column(db.String(128), nullable=False, unique=True, index=True)
    content = db.Column(db.Text, nullable=False)
