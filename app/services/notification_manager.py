# app/services/notification_manager.py

from app import db
from app.models import NotificationModel


async def create_notification(notification_info):
    """
    Create a new NotificationModel based on the provided notification_info.

    Args:
    - notification_info (dict): Dictionary containing the new notification's details.

    Returns:
    - (NotificationModel): The newly created NotificationModel instance.
    """
    new_notification = NotificationModel(**notification_info)
    await db.async_session.add(new_notification)
    await db.async_session.commit()
    return new_notification


async def get_notification_by_id(notification_id):
    """
    Fetch a NotificationModel based on its ID.

    Args:
    - notification_id (int): ID of the notification to fetch.

    Returns:
    - (NotificationModel): The requested NotificationModel instance or None if not found.
    """
    return NotificationModel.query.get(notification_id)


async def get_notifications_for_user(user_id, status="unread", limit=10):
    """
    Fetch all notifications associated with a user, filtered by status.

    Args:
    - user_id (int): ID of the user.
    - status (str): The status of the notifications to fetch.

    Returns:
    - List[NotificationModel]: A list of all NotificationModel instances matching the criteria.
    """
    query = NotificationModel.query.filter_by(user_id=user_id, status=status).order_by(
        NotificationModel.created.desc()
    )
    if limit:
        query = query.limit(limit)
    return query.all()


async def mark_notification_as_read(notification_id):
    """
    Mark a NotificationModel as read.

    Args:
    - notification_id (int): ID of the notification to mark as read.

    Returns:
    - (bool): True if marking was successful, False otherwise.
    """
    notification = get_notification_by_id(notification_id)
    if not notification:
        return False

    notification.status = "read"
    await db.async_session.commit()
    return True


async def delete_notification(notification_id):
    """
    Delete a NotificationModel based on its ID.

    Args:
    - notification_id (int): ID of the notification to delete.

    Returns:
    - (bool): True if deletion was successful, False otherwise.
    """
    notification = get_notification_by_id(notification_id)
    if not notification:
        return False

    await db.async_session.delete(notification)
    await db.async_session.commit()
    return True
