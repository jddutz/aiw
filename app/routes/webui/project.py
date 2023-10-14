# app.routes.project_routes.py

from flask import render_template, redirect, url_for, request, Blueprint
from app.models import WritingProject  # Assuming this is your project model

project_blueprint = Blueprint('project', __name__)

@project_blueprint.route('/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        # Logic to create a new project goes here
        pass
    return render_template('create_project.html')  # The UI for creating a project

@project_blueprint.route('/', methods=['GET'])
def list_projects():
    projects = WritingProject.query.all()
    return render_template('list_projects.html', projects=projects)

@project_blueprint.route('/<int:project_id>', methods=['GET'])
def project_detail(project_id):
    project = WritingProject.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@project_blueprint.route('/<int:project_id>/update', methods=['GET', 'POST'])
def update_project(project_id):
    project = WritingProject.query.get_or_404(project_id)
    if request.method == 'POST':
        # Logic to update the project goes here
        pass
    return render_template('update_project.html', project=project)

@project_blueprint.route('/<int:project_id>/delete', methods=['POST'])
def delete_project(project_id):
    project = WritingProject.query.get_or_404(project_id)
    # Logic to delete the project goes here
    pass
    return redirect(url_for('project.list_projects'))
