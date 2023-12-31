# app/services/chat_message_manager.py

from app import db
from app.models import ChatMessageModel, ChatHistoryModel


def create_message(data):
    """
    Create a new ChatMessageModel based on the provided data.

    Args:
    - data (dict): Dictionary containing the message's details.

    Returns:
    - (ChatMessageModel): The newly created ChatMessageModel instance.
    """
    message = ChatMessageModel.from_dict(data)
    db.session.add(message)
    db.session.commit()
    return message


def get_message_by_id(message_id):
    """
    Retrieve a ChatMessageModel by its ID.

    Args:
    - message_id (int): The ID of the ChatMessageModel to retrieve.

    Returns:
    - (ChatMessageModel): The retrieved ChatMessageModel instance or None if not found.
    """
    return ChatMessageModel.query.get(message_id)


def get_all_messages_by_chat_history_id(chat_history_id):
    """
    Retrieve all ChatMessages associated with a particular ChatHistoryModel.

    Args:
    - chat_history_id (int): The ID of the ChatHistoryModel for which to retrieve messages.

    Returns:
    - List[ChatMessageModel]: List of retrieved ChatMessageModel instances.
    """
    return ChatMessageModel.query.filter_by(chat_history_id=chat_history_id).all()


def update_message(message_id, data):
    """
    Update a ChatMessageModel with new data.

    Args:
    - message_id (int): The ID of the ChatMessageModel to update.
    - data (dict): Dictionary containing the updated message's details.

    Returns:
    - (ChatMessageModel): The updated ChatMessageModel instance or None if not found.
    """
    message = ChatMessageModel.query.get(message_id)
    if message:
        for key, value in data.items():
            setattr(message, key, value)
        db.session.commit()
        return message
    return None


def delete_message(message_id):
    """
    Delete a ChatMessageModel by its ID.

    Args:
    - message_id (int): The ID of the ChatMessageModel to delete.

    Returns:
    - bool: True if the deletion was successful, otherwise False.
    """
    message = ChatMessageModel.query.get(message_id)
    if message:
        db.session.delete(message)
        db.session.commit()
        return True
    return False
