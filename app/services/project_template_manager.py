# app/services/project_template_manager.py


from app import db
from app.models import ProjectTemplate, Tag, Genre

# app/services/project_template_manager.py

from app import db
from app.models import ProjectTemplate, Tag, Genre


def create_template(data):
    tags = [Tag.query.get_or_404(tag_id) for tag_id in data.get("tags", [])]
    genres = [Genre.query.get_or_404(genre_id) for genre_id in data.get("genres", [])]
    template = ProjectTemplate(
        name=data["name"],
        description=data["description"],
        methodology=data["methodology"],
        length=data["length"][:254],
        tags=tags,
        genres=genres,
        imageref=data.get("imageref", ""),
        created=data.get("created", None),
        modified=data.get("modified", None),
        usage_count=data.get("usage_count", 0),
    )
    template.set_links(data.get("links", []))
    template.set_structure(data.get("structure", {}))
    db.session.add(template)
    db.session.commit()
    return template


def update_template(template_id, data):
    template = ProjectTemplate.query.get_or_404(template_id)

    for key, value in data.items():
        if key == "tags":
            template.tags = [Tag.query.get_or_404(tag_id) for tag_id in value]
        elif key == "genres":
            template.genres = [Genre.query.get_or_404(genre_id) for genre_id in value]
        else:
            setattr(template, key, value)

    db.session.commit()
    return template


def get_template(template_id):
    return ProjectTemplate.query.get_or_404(template_id)


def delete_template(template_id):
    template = ProjectTemplate.query.get_or_404(template_id)
    db.session.delete(template)
    db.session.commit()
    return True


def list_templates():
    return ProjectTemplate.query.all()
