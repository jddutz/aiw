from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Project

@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    PER_PAGE = 10
    projects = Project.query.paginate(page, PER_PAGE, False).items
    return render_template('index.html', projects=projects, page=page)


@app.route('/load_project', methods=['GET', 'POST'])
def load_project():
    # Logic for loading a project from the database goes here
    if request.method == 'POST':
        # Handle form submission, load the project, and redirect to project page
        pass
    return render_template('load_project.html')  # Assuming you'll create this template

@app.route('/new_project', methods=['GET', 'POST'])
def new_project():
    # Logic for creating a new project goes here
    if request.method == 'POST':
        # Handle form submission, create the new project, and redirect to project page
        pass
    return render_template('new_project.html')  # Assuming you'll create this template
