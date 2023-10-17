import os

from dotenv import load_dotenv

project_folder = os.path.expanduser("~/aiw")  # adjust as appropriate
load_dotenv(os.path.join(project_folder, ".env"))

import json
from app import flask_app, db
from app.models.project_template import ProjectTemplate
from app.models.genre import Genre
from app.models.tag import Tag
from datetime import datetime


def load_template_data():
    # Load data from JSON file
    with open("project_templates.json", "r") as file:
        data = json.load(file)
        templates = data["templates"]

    # Loop through each template in the file
    for template_data in templates:
        print(template_data["name"])
        existing = ProjectTemplate.query.filter_by(name=template_data["name"]).first()
        if not existing:
            # Tags: Create if not exists and get Tag objects
            tags = []
            for tag_name in template_data["tags"]:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name, description=tag_name)
                    db.session.add(tag)
                    db.session.commit()
                tags.append(tag)

            # Genres: Create if not exists and get Genre objects
            genres = []
            for genre_name in template_data["genres"]:
                genre = Genre.query.filter_by(name=genre_name).first()
                if not genre:
                    genre = Genre(name=genre_name, description=genre_name)
                    db.session.add(genre)
                    db.session.commit()
                genres.append(genre)

            # Create the template object
            new_template = ProjectTemplate(
                name=template_data["name"],
                description=template_data["description"],
                methodology=template_data["methodology"],
                length=template_data["length"][:254],
                imageref=template_data.get(
                    "imageref", ""
                ),  # Get the attribute with default as empty string
                created=datetime.utcnow()
                if not template_data.get("created")
                else datetime.fromisoformat(template_data["created"]),
                modified=datetime.utcnow()
                if not template_data.get("modified")
                else datetime.fromisoformat(template_data["modified"]),
                usage_count=template_data["usage_count"],
                tags=tags,
                genres=genres,
            )
            new_template.set_links(template_data["links"])
            db.session.add(new_template)

    # Commit all changes to the database
    db.session.commit()


if __name__ == "__main__":
    with flask_app.app_context():
        load_template_data()
