# app/services/story_manager.py

from app import db
from app.models import StoryPartModel


async def create_story_part(story_part_data):
    """
    Create a new StoryPartModel based on the provided data.

    Args:
    - story_part_data (dict): Dictionary containing the new story part's details.

    Returns:
    - (StoryPartModel): The newly created StoryPartModel instance.
    """
    story_part = StoryPartModel(**story_part_data)
    await db.async_session.add(story_part)
    await db.async_session.commit()
    return story_part


async def get_story_part_by_id(story_part_id):
    """
    Retrieve a StoryPartModel by its ID.

    Args:
    - story_part_id (int): The ID of the StoryPartModel to retrieve.

    Returns:
    - (StoryPartModel): The retrieved StoryPartModel instance or None if not found.
    """
    return StoryPartModel.query.get(story_part_id)


async def update_story_part(story_part_id, updated_data):
    """
    Update an existing StoryPartModel based on provided data.

    Args:
    - story_part_id (int): The ID of the StoryPartModel to update.
    - updated_data (dict): Dictionary containing updated data for the StoryPartModel.

    Returns:
    - (StoryPartModel): The updated StoryPartModel instance or None if update was unsuccessful.
    """
    story_part = get_story_part_by_id(story_part_id)
    if story_part:
        for key, value in updated_data.items():
            setattr(story_part, key, value)
        await db.async_session.commit()
        return story_part
    return None


async def delete_story_part(story_part_id):
    """
    Delete a StoryPartModel by its ID.

    Args:
    - story_part_id (int): The ID of the StoryPartModel to delete.

    Returns:
    - bool: True if the deletion was successful, otherwise False.
    """
    story_part = StoryPartModel.query.get(story_part_id)
    if story_part:
        await db.async_session.delete(story_part)
        await db.async_session.commit()
        return True
    return False


async def get_child_story_parts(parent_id):
    """
    Retrieve all child StoryParts of a given StoryPartModel.

    Args:
    - parent_id (int): The ID of the parent StoryPartModel.

    Returns:
    - List[StoryPartModel]: List of child StoryPartModel instances.
    """
    parent = get_story_part_by_id(parent_id)
    if parent:
        return parent.children.all()
    return []


async def get_story_parts_for_project(writing_project_id):
    """
    Retrieve all StoryParts associated with a given WritingProjectModel.

    Args:
    - writing_project_id (int): The ID of the WritingProjectModel.

    Returns:
    - List[StoryPartModel]: List of StoryPartModel instances associated with the WritingProjectModel.
    """
    return StoryPartModel.query.filter_by(writing_project_id=writing_project_id).all()
