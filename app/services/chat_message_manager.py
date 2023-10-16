# app/services/chat_message_manager.py

from app import db
from app.models import ChatMessage, ChatHistory


def create_message(data):
    """
    Create a new ChatMessage based on the provided data.

    Args:
    - data (dict): Dictionary containing the message's details.

    Returns:
    - (ChatMessage): The newly created ChatMessage instance.
    """
    message = ChatMessage.from_dict(data)
    db.session.add(message)
    db.session.commit()
    return message


def get_message_by_id(message_id):
    """
    Retrieve a ChatMessage by its ID.

    Args:
    - message_id (int): The ID of the ChatMessage to retrieve.

    Returns:
    - (ChatMessage): The retrieved ChatMessage instance or None if not found.
    """
    return ChatMessage.query.get(message_id)


def get_all_messages_by_chat_history_id(chat_history_id):
    """
    Retrieve all ChatMessages associated with a particular ChatHistory.

    Args:
    - chat_history_id (int): The ID of the ChatHistory for which to retrieve messages.

    Returns:
    - List[ChatMessage]: List of retrieved ChatMessage instances.
    """
    return ChatMessage.query.filter_by(chat_history_id=chat_history_id).all()


def update_message(message_id, data):
    """
    Update a ChatMessage with new data.

    Args:
    - message_id (int): The ID of the ChatMessage to update.
    - data (dict): Dictionary containing the updated message's details.

    Returns:
    - (ChatMessage): The updated ChatMessage instance or None if not found.
    """
    message = ChatMessage.query.get(message_id)
    if message:
        for key, value in data.items():
            setattr(message, key, value)
        db.session.commit()
        return message
    return None


def delete_message(message_id):
    """
    Delete a ChatMessage by its ID.

    Args:
    - message_id (int): The ID of the ChatMessage to delete.

    Returns:
    - bool: True if the deletion was successful, otherwise False.
    """
    message = ChatMessage.query.get(message_id)
    if message:
        db.session.delete(message)
        db.session.commit()
        return True
    return False
