# app/routes/www/project_template.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from app import db
from app.models import ProjectTemplate
from app.services import project_template_manager
from app.forms.project_template_edit_form import EditProjectTemplateForm

project_template_blueprint = Blueprint("project_template", __name__)


@project_template_blueprint.route("/", methods=["GET"])
def index():
    project_templates = (
        ProjectTemplate.query.all()
    )  # Fetch all templates from the database
    return render_template(
        "project_template_index.html",
        project_templates=project_templates,
        show_ai_toolbox=True,
    )


@project_template_blueprint.route("/", methods=["POST"])
def create():
    if request.method == "POST":
        template_info = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "methodology": request.form.get("methodology"),
            # Add any other required fields from the form here.
        }

        # You may want to handle tags, genres, etc. separately if they are included in the form.
        # For instance, using request.form.getlist() for multi-select fields.

        try:
            new_template = project_template_manager.create_template(template_info)
            flash("Project project_template successfully created!", "success")
            return redirect(
                url_for(
                    "project_template.project_template_detail",
                    project_template_id=new_template.id,
                )
            )
        except Exception as e:
            flash(f"Error creating project project_template: {str(e)}", "danger")
            return render_template("create_template.html")

    return render_template(
        "create_template.html",
        show_ai_toolbox=True,
    )


@project_template_blueprint.route("/<int:project_template_id>", methods=["GET"])
def detail(project_template_id):
    project_template = ProjectTemplate.query.get_or_404(
        project_template_id
    )  # Fetch project_template by ID or return 404
    return render_template(
        "project_template_detail.html",
        project_template=project_template,
        show_ai_toolbox=True,
    )


@project_template_blueprint.route(
    "/<int:project_template_id>/edit", methods=["GET", "POST"]
)
def edit(project_template_id):
    # Retrieve the project project_template by its ID
    project_template = ProjectTemplate.query.get_or_404(project_template_id)

    form = EditProjectTemplateForm(obj=project_template)
    form.category.choices = project_template_manager.load_categories()

    if form.validate_on_submit():
        # Update the project project_template's fields based on the form data
        form.populate_obj(project_template)

        # Save the changes to the database
        db.session.commit()

        flash("Project project_template updated successfully!", "success")
        return redirect(url_for("project_template.list"))

    ai_toolbox_actions = [
        {
            "caption": "Update Description",
            "icon": "fas fa-comment",
            "js_function": "update_description",
        },
        {
            "caption": "Update Methodology",
            "icon": "fas fa-comment",
            "js_function": "update_methodology",
        },
    ]

    return render_template(
        "project_template_edit.html",
        form=form,
        project_template=project_template,
        show_ai_toolbox=True,
        ai_toolbox_actions=ai_toolbox_actions,
    )
