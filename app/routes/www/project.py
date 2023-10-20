# app/routes/www/project.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import current_user
from app.models import WritingProject, ProjectTemplate
from app.services import project_manager, token_manager
from app.forms import ProjectEditForm

project_blueprint = Blueprint("project", __name__)


@project_blueprint.route("/create", methods=["GET", "POST"])
def new():
    form = ProjectEditForm()

    templates_by_category = {}
    for project_template in ProjectTemplate.query.all():
        templates_by_category.setdefault(project_template.category, []).append(
            (str(project_template.id), project_template.project_template_name)
        )

    # Convert the dictionary to the list format
    choices = [(key, value) for key, value in templates_by_category.items()]
    form.project_template.choices = choices

    if form.validate_on_submit():
        # Convert form data as necessary
        project_info = {
            "title": form.title.data,
            "description": form.description.data,
            "owner_id": current_user.id,  # Assuming you're using Flask-Login or similar
            "visibility": form.visibility.data,
            "project_type": form.project_template.data,  # This would be the ID of the selected project template
            "tags": form.tags.data,  # Assuming this would be a list of tag strings, or perhaps tag IDs
            # The following fields will likely not be part of the form, but I'm including them for completeness
            "created": datetime.utcnow(),
            "last_modified": datetime.utcnow(),
        }

        # Using project_manager to create the project
        new_project = project_manager.create_new_project(project_info)

        flash("Project successfully created!", "success")
        return redirect(url_for("project.project_detail", project_id=new_project.id))

    # If GET, show login page
    return render_template(
        "create_project.html",
        form=form,
        show_ai_toolbox=True,
    )


@project_blueprint.route("/search", methods=["GET"])
def search():
    pass


@project_blueprint.route("/<int:project_id>", methods=["GET"])
def project_detail(project_id):
    project = WritingProject.query.get_or_404(project_id)
    return render_template(
        "project_detail.html",
        project=project,
        show_ai_toolbox=True,
    )


@project_blueprint.route("/<int:project_id>/update", methods=["GET", "POST"])
def update_project(project_id):
    project = WritingProject.query.get_or_404(project_id)
    if request.method == "POST":
        # Logic to update the project goes here
        pass
    return render_template(
        "update_project.html",
        project=project,
        show_ai_toolbox=True,
    )


@project_blueprint.route("/<int:project_id>/delete", methods=["GET", "POST"])
def delete_project(project_id):
    project = WritingProject.query.get_or_404(project_id)

    # For GET request, render the confirmation page
    if request.method == "GET":
        token = token_manager.generate_delete_token()
        return render_template("delete_confirm.html", project=project, token=token)

    # For POST request, handle the delete action
    elif request.method == "POST":
        # Check if the provided token matches the session token and isn't expired
        token = request.form.get("token")

        if token != session.get("delete_token") or (
            token_expiry and token_expiry < datetime.utcnow()
        ):
            flash("Invalid or expired token. Please try again.", "danger")
            return redirect(url_for("project.project_detail", project_id=project.id))

        # Logic to delete the project
        # Assuming you have a db session and commit the changes after deleting
        db.session.delete(project)
        db.session.commit()

        flash("Project successfully deleted!", "success")
        return redirect(url_for("project.list_projects"))

    # In the unlikely event it's neither a GET nor a POST
    return redirect(url_for("project.list_projects"))
