# app/services/notification_manager.py

from app import db
from app.models import Notification


def create_notification(notification_info):
    """
    Create a new Notification based on the provided notification_info.

    Args:
    - notification_info (dict): Dictionary containing the new notification's details.

    Returns:
    - (Notification): The newly created Notification instance.
    """
    new_notification = Notification(**notification_info)
    db.session.add(new_notification)
    db.session.commit()
    return new_notification


def get_notification_by_id(notification_id):
    """
    Fetch a Notification based on its ID.

    Args:
    - notification_id (int): ID of the notification to fetch.

    Returns:
    - (Notification): The requested Notification instance or None if not found.
    """
    return Notification.query.get(notification_id)


def get_notifications_for_user(user_id, status="unread", limit=10):
    """
    Fetch all notifications associated with a user, filtered by status.

    Args:
    - user_id (int): ID of the user.
    - status (str): The status of the notifications to fetch.

    Returns:
    - List[Notification]: A list of all Notification instances matching the criteria.
    """
    query = Notification.query.filter_by(user_id=user_id, status=status).order_by(
        Notification.created.desc()
    )
    if limit:
        query = query.limit(limit)
    return query.all()


def mark_notification_as_read(notification_id):
    """
    Mark a Notification as read.

    Args:
    - notification_id (int): ID of the notification to mark as read.

    Returns:
    - (bool): True if marking was successful, False otherwise.
    """
    notification = get_notification_by_id(notification_id)
    if not notification:
        return False

    notification.status = "read"
    db.session.commit()
    return True


def delete_notification(notification_id):
    """
    Delete a Notification based on its ID.

    Args:
    - notification_id (int): ID of the notification to delete.

    Returns:
    - (bool): True if deletion was successful, False otherwise.
    """
    notification = get_notification_by_id(notification_id)
    if not notification:
        return False

    db.session.delete(notification)
    db.session.commit()
    return True
