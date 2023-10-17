# app/services/project_manager.py

from datetime import datetime
from app import db
from app.models import WritingProject, ProjectTemplate, Tag


def create_new_project(project_info):
    """
    Create a new WritingProject based on the provided project_info.

    Args:
    - project_info (dict): Dictionary containing the new project's details.

    Returns:
    - (WritingProject): The newly created WritingProject instance.
    """
    # Load the template using the ID from the project_info
    template = ProjectTemplate.query.get(project_info["project_type"])

    # Validate if the template exists
    if not template:
        raise ValueError("Invalid template provided")

    # Combine template tags with project_info tags, if available
    combined_tags = []
    if hasattr(template, "tags"):
        combined_tags.extend(template.tags)
    if "tags" in project_info:
        for tag_name in project_info["tags"].split("\n"):
            tag_name = tag_name.strip()  # Remove any leading or trailing whitespace
            if not tag_name:  # Skip blank tag names
                continue
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name, description="Default description")
                db.session.add(tag)
            combined_tags.append(tag)

    # Create a new WritingProject
    new_project = WritingProject(
        owner_id=project_info["owner_id"],
        title=project_info["title"],
        description=project_info["description"],
        project_type=template.name,
        visibility=project_info["visibility"],
        tags=combined_tags,
    )

    # TODO: Handle structure expansion and parsing from the ProjectTemplate.
    # This will involve parsing the structure JSON, and using the parsed
    # data to add collections and story parts to the new project.

    # Add and commit the new project
    db.session.add(new_project)
    db.session.commit()

    return new_project


def get_project_by_id(project_id):
    """
    Fetch a WritingProject based on its ID.

    Args:
    - project_id (int): ID of the project to fetch.

    Returns:
    - (WritingProject): The requested WritingProject instance or None if not found.
    """
    return WritingProject.query.get(project_id)


def get_recent_projects_for_user(user_id, limit=10):
    """
    Fetch all projects associated with a user.

    Args:
    - user_id (int): ID of the user.

    Returns:
    - List[WritingProject]: A list of all WritingProject instances associated with the user.
    """
    query = WritingProject.query.filter_by(owner_id=user_id).order_by(
        WritingProject.created.desc()
    )
    if limit:
        query = query.limit(limit)
    return query.all()


def update_project(project_id, update_info):
    """
    Update a WritingProject's details.

    Args:
    - project_id (int): ID of the project to update.
    - update_info (dict): Dictionary containing fields and new values to update.

    Returns:
    - (WritingProject): The updated WritingProject instance or None if update failed.
    """
    project = get_project_by_id(project_id)
    if not project:
        return None

    for key, value in update_info.items():
        setattr(project, key, value)

    db.session.commit()
    return project


def delete_project(project_id):
    """
    Delete a WritingProject based on its ID.

    Args:
    - project_id (int): ID of the project to delete.

    Returns:
    - (bool): True if deletion was successful, False otherwise.
    """
    project = get_project_by_id(project_id)
    if not project:
        return False

    db.session.delete(project)
    db.session.commit()
    return True
