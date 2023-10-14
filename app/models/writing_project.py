# models.writing_project.py

from app import db
import json

class WritingProject(db.Model):
    """
    Represents a writing project.
    """

    def __init__(self, project_id: str, title: str, description: str, prompt: str):
        """
        Initializes a new writing project.

        :param project_id: The ID of the project.
        :param title: The title of the project.
        :param description: The description of the project.
        :param prompt: The prompt of the project.
        """
        self.project_id = project_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"WritingProject({self.project_id}, {self.title})"

    def __repr__(self):
        return str(self)
    
    def to_dict(self):
        return {
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())