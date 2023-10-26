# app/services/chat_history_manager.py

from app import db
from app.models import ChatHistoryModel, ChatMessageModel


async def create_history():
    """
    Create a new ChatHistoryModel instance and save it to the database.

    Returns:
    - (ChatHistoryModel): The newly created ChatHistoryModel instance.
    """
    history = ChatHistoryModel()
    await db.async_session.add(history)
    await db.async_session.commit()
    return history


async def add_message_to_history(history_id, message_data):
    """
    Add a new message to a specified ChatHistoryModel.

    Args:
    - history_id (int): The ID of the ChatHistoryModel to which the message will be added.
    - message_data (dict): Dictionary containing the message's details.

    Returns:
    - (ChatMessageModel): The newly added ChatMessageModel instance.
    """
    history = get_history_by_id(history_id)
    if history:
        message = ChatMessageModel.from_dict(message_data)
        history.add_message(message)
        await db.async_session.commit()
        return message
    return None


async def get_history_by_id(history_id):
    """
    Retrieve a ChatHistoryModel by its ID.

    Args:
    - history_id (int): The ID of the ChatHistoryModel to retrieve.

    Returns:
    - (ChatHistoryModel): The retrieved ChatHistoryModel instance or None if not found.
    """
    return ChatHistoryModel.query.get(history_id)


async def get_all_messages_from_history(history_id):
    """
    Retrieve all messages from a specified ChatHistoryModel.

    Args:
    - history_id (int): The ID of the ChatHistoryModel from which to retrieve messages.

    Returns:
    - List[ChatMessageModel]: List of ChatMessageModel instances associated with the ChatHistoryModel.
    """
    history = get_history_by_id(history_id)
    if history:
        return history.messages
    return []


async def delete_history(history_id):
    """
    Delete a ChatHistoryModel by its ID.

    Args:
    - history_id (int): The ID of the ChatHistoryModel to delete.

    Returns:
    - bool: True if the deletion was successful, otherwise False.
    """
    history = ChatHistoryModel.query.get(history_id)
    if history:
        await db.async_session.delete(history)
        await db.async_session.commit()
        return True
    return False
