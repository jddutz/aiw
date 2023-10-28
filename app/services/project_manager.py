# app/services/project_manager.py

from datetime import datetime
from app import db
from app.models import WritingProjectModel, ProjectTemplateModel


def create_new_project(project_info):
    """
    Create a new WritingProjectModel based on the provided project_info.

    Args:
    - project_info (dict): Dictionary containing the new project's details.

    Returns:
    - (WritingProjectModel): The newly created WritingProjectModel instance.
    """
    # Load the template using the ID from the project_info
    template = ProjectTemplateModel.query.get(project_info["project_type"])

    # Validate if the template exists
    if not template:
        raise ValueError("Invalid template provided")

    # Combine template tags with project_info tags, if available
    combined_tags = []
    if hasattr(template, "tags"):
        combined_tags.extend(template.tags)

    # Create a new WritingProjectModel
    new_project = WritingProjectModel(
        owner_id=project_info["owner_id"],
        title=project_info["title"],
        description=project_info["description"],
        project_type=template.name,
        visibility=project_info["visibility"],
        tags=combined_tags,
    )

    # TODO: Handle structure expansion and parsing from the ProjectTemplateModel.
    # This will involve parsing the structure JSON, and using the parsed
    # data to add collections and story parts to the new project.

    # Add and commit the new project
    db.session.add(new_project)
    db.session.commit()

    return new_project


def get_project_by_id(project_id):
    """
    Fetch a WritingProjectModel based on its ID.

    Args:
    - project_id (int): ID of the project to fetch.

    Returns:
    - (WritingProjectModel): The requested WritingProjectModel instance or None if not found.
    """
    return WritingProjectModel.query.get(project_id)


def get_recent_projects_for_user(user_id, limit=10):
    """
    Fetch all projects associated with a user.

    Args:
    - user_id (int): ID of the user.

    Returns:
    - List[WritingProjectModel]: A list of all WritingProjectModel instances associated with the user.
    """
    query = WritingProjectModel.query.filter_by(owner_id=user_id).order_by(
        WritingProjectModel.created.desc()
    )
    if limit:
        query = query.limit(limit)
    return query.all()


def update_project(project_id, update_info):
    """
    Update a WritingProjectModel's details.

    Args:
    - project_id (int): ID of the project to update.
    - update_info (dict): Dictionary containing fields and new values to update.

    Returns:
    - (WritingProjectModel): The updated WritingProjectModel instance or None if update failed.
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
    Delete a WritingProjectModel based on its ID.

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
