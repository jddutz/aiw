# app/routes/www/project_template.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from app import db
from app.models import ProjectTemplate
from app.services import project_template_manager
from app.forms.project_template_edit_form import ProjectTemplateEditForm

project_template_blueprint = Blueprint("project_template", __name__)


@project_template_blueprint.route("/", methods=["GET"])
def index():
    data = ProjectTemplate.query.all()  # Fetch all templates from the database
    return render_template(
        "admin/project_template/index.html",
        project_templates=data,
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
        "admin/project_template/edit.html",
        show_ai_toolbox=True,
    )


@project_template_blueprint.route("/<int:project_template_id>", methods=["GET"])
def detail(project_template_id):
    data = ProjectTemplate.query.get_or_404(
        project_template_id
    )  # Fetch project_template by ID or return 404
    return render_template(
        "admin/project_template/detail.html",
        project_template=data,
        show_ai_toolbox=True,
    )


@project_template_blueprint.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    # Retrieve the project project_template by its ID
    model = ProjectTemplate.query.get_or_404(id)

    form = ProjectTemplateEditForm(obj=model)
    form.category.choices = project_template_manager.load_categories()

    if form.validate_on_submit():
        # Update the project project_template's fields based on the form data
        form.populate_obj(model)

        # Save the changes to the database
        db.session.commit()

        flash(
            f"Project Template, {model.project_template_name} updated successfully!",
            "success",
        )
        return redirect(url_for("project_template.list"))

    ai_toolbox_actions = [
        {
            "caption": "Update Description",
            "icon": "fas fa-comment",
            "js_function": "update_description()",
        },
        {
            "caption": "Update Methodology",
            "icon": "fas fa-comment",
            "js_function": "update_methodology()",
        },
        {
            "caption": "Update Project Structure",
            "icon": "fas fa-comment",
            "js_function": "update_project_structure()",
        },
    ]

    return render_template(
        "admin/project_template/edit.html",
        form=form,
        model=model,
        show_ai_toolbox=True,
        ai_toolbox_actions=ai_toolbox_actions,
    )