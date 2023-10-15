# app/db/projects.py

from typing import Dict, List

TABLE_NAME = "projects"

def get(project_id: str) -> Dict:
    return load_data(TABLE_NAME, lambda x: x["project_id"] == project_id)[0]

def load_projects() -> List[Dict]:
    return load_data(TABLE_NAME)

def save_project(project: Dict):
    projects = load_projects()
    projects.append(project)
    save_data(TABLE_NAME, projects)
