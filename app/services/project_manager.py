from app import db
from app.models import WritingProject

def create_new_project(project_info):
    """
    Create a new WritingProject based on the provided project_info.
    
    Args:
    - project_info (dict): Dictionary containing the new project's details. 

    Returns:
    - (WritingProject): The newly created WritingProject instance.
    """
    new_project = WritingProject(title=project_info['title'], description=project_info['description'])
    db.session.add(new_project)
    db.session.commit()
    return new_project
