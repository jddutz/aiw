# app/models/chat_system_message.py

from app import db
from datetime import datetime
from sqlalchemy import Enum

from sqlalchemy import (
    create_engine,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class ChatSystemMessage(db.Model):
    __tablename__ = "chat_system_message"

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(255), nullable=False)
    content = db.Column(Text, nullable=False)
    type = db.Column(String(50), nullable=True)
    associated_module = db.Column(String(50), nullable=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = db.Column(String(255), nullable=True)
    version = db.Column(String(50), nullable=True)
    is_active = db.Column(Boolean, default=True)
    created_by = db.Column(String(100), nullable=True)
    updated_by = db.Column(String(100), nullable=True)
