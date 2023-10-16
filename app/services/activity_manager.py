# app/services/activity_manager.py

from app import db
from app.models import Activity


def log_activity(activity_info):
    """
    Create and log a new Activity based on the provided activity_info.

    Args:
    - activity_info (dict): Dictionary containing the new activity's details.

    Returns:
    - (Activity): The newly logged Activity instance.
    """
    new_activity = Activity(**activity_info)
    db.session.add(new_activity)
    db.session.commit()
    return new_activity


def get_activity_by_id(activity_id):
    """
    Fetch an Activity based on its ID.

    Args:
    - activity_id (int): ID of the activity to fetch.

    Returns:
    - (Activity): The requested Activity instance or None if not found.
    """
    return Activity.query.get(activity_id)


def get_recent_activities_for_user(user_id, limit=10):
    """
    Fetch all activities associated with a user.

    Args:
    - user_id (int): ID of the user.
    - limit (int): The maximum number of results to return.

    Returns:
    - List[Activity]: A list of all Activity instances associated with the user.
    """
    query = Activity.query.filter_by(user_id=user_id).order_by(Activity.created.desc())
    if limit:
        query = query.limit(limit)
    return query.all()


def delete_activity(activity_id):
    """
    Delete an Activity based on its ID.

    Args:
    - activity_id (int): ID of the activity to delete.

    Returns:
    - (bool): True if deletion was successful, False otherwise.
    """
    activity = get_activity_by_id(activity_id)
    if not activity:
        return False

    db.session.delete(activity)
    db.session.commit()
    return True
