# app/services/chat_history_manager.py

from app import db
from app.models import ChatHistory, ChatMessage


def create_history():
    """
    Create a new ChatHistory instance and save it to the database.

    Returns:
    - (ChatHistory): The newly created ChatHistory instance.
    """
    history = ChatHistory()
    db.session.add(history)
    db.session.commit()
    return history


def add_message_to_history(history_id, message_data):
    """
    Add a new message to a specified ChatHistory.

    Args:
    - history_id (int): The ID of the ChatHistory to which the message will be added.
    - message_data (dict): Dictionary containing the message's details.

    Returns:
    - (ChatMessage): The newly added ChatMessage instance.
    """
    history = get_history_by_id(history_id)
    if history:
        message = ChatMessage.from_dict(message_data)
        history.add_message(message)
        db.session.commit()
        return message
    return None


def get_history_by_id(history_id):
    """
    Retrieve a ChatHistory by its ID.

    Args:
    - history_id (int): The ID of the ChatHistory to retrieve.

    Returns:
    - (ChatHistory): The retrieved ChatHistory instance or None if not found.
    """
    return ChatHistory.query.get(history_id)


def get_all_messages_from_history(history_id):
    """
    Retrieve all messages from a specified ChatHistory.

    Args:
    - history_id (int): The ID of the ChatHistory from which to retrieve messages.

    Returns:
    - List[ChatMessage]: List of ChatMessage instances associated with the ChatHistory.
    """
    history = get_history_by_id(history_id)
    if history:
        return history.messages
    return []


def delete_history(history_id):
    """
    Delete a ChatHistory by its ID.

    Args:
    - history_id (int): The ID of the ChatHistory to delete.

    Returns:
    - bool: True if the deletion was successful, otherwise False.
    """
    history = ChatHistory.query.get(history_id)
    if history:
        db.session.delete(history)
        db.session.commit()
        return True
    return False
