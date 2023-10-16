# app/services/story_manager.py

from app import db
from app.models import StoryPart


def create_story_part(story_part_data):
    """
    Create a new StoryPart based on the provided data.

    Args:
    - story_part_data (dict): Dictionary containing the new story part's details.

    Returns:
    - (StoryPart): The newly created StoryPart instance.
    """
    story_part = StoryPart(**story_part_data)
    db.session.add(story_part)
    db.session.commit()
    return story_part


def get_story_part_by_id(story_part_id):
    """
    Retrieve a StoryPart by its ID.

    Args:
    - story_part_id (int): The ID of the StoryPart to retrieve.

    Returns:
    - (StoryPart): The retrieved StoryPart instance or None if not found.
    """
    return StoryPart.query.get(story_part_id)


def update_story_part(story_part_id, updated_data):
    """
    Update an existing StoryPart based on provided data.

    Args:
    - story_part_id (int): The ID of the StoryPart to update.
    - updated_data (dict): Dictionary containing updated data for the StoryPart.

    Returns:
    - (StoryPart): The updated StoryPart instance or None if update was unsuccessful.
    """
    story_part = get_story_part_by_id(story_part_id)
    if story_part:
        for key, value in updated_data.items():
            setattr(story_part, key, value)
        db.session.commit()
        return story_part
    return None


def delete_story_part(story_part_id):
    """
    Delete a StoryPart by its ID.

    Args:
    - story_part_id (int): The ID of the StoryPart to delete.

    Returns:
    - bool: True if the deletion was successful, otherwise False.
    """
    story_part = StoryPart.query.get(story_part_id)
    if story_part:
        db.session.delete(story_part)
        db.session.commit()
        return True
    return False


def get_child_story_parts(parent_id):
    """
    Retrieve all child StoryParts of a given StoryPart.

    Args:
    - parent_id (int): The ID of the parent StoryPart.

    Returns:
    - List[StoryPart]: List of child StoryPart instances.
    """
    parent = get_story_part_by_id(parent_id)
    if parent:
        return parent.children.all()
    return []


def get_story_parts_for_project(writing_project_id):
    """
    Retrieve all StoryParts associated with a given WritingProject.

    Args:
    - writing_project_id (int): The ID of the WritingProject.

    Returns:
    - List[StoryPart]: List of StoryPart instances associated with the WritingProject.
    """
    return StoryPart.query.filter_by(writing_project_id=writing_project_id).all()
