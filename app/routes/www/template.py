# app/routes/www/template.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from app import db
from app.models import ProjectTemplate
from app.services import project_template_manager
from app.forms.edit_project_template_form import EditProjectTemplateForm

template_blueprint = Blueprint("template", __name__)


@template_blueprint.route("/", methods=["GET"])
def index():
    templates = ProjectTemplate.query.all()  # Fetch all templates from the database
    return render_template("template_index.html", templates=templates)


@template_blueprint.route("/create", methods=["GET", "POST"])
def new():
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
            flash("Project template successfully created!", "success")
            return redirect(
                url_for("template.template_detail", template_id=new_template.id)
            )
        except Exception as e:
            flash(f"Error creating project template: {str(e)}", "danger")
            return render_template("create_template.html")

    return render_template("create_template.html")


@template_blueprint.route("/<int:template_id>", methods=["GET"])
def detail(template_id):
    template = ProjectTemplate.query.get_or_404(
        template_id
    )  # Fetch template by ID or return 404
    return render_template("template_detail.html", template=template)


@template_blueprint.route("/<int:template_id>/edit", methods=["GET", "POST"])
def edit(template_id):
    # Retrieve the project template by its ID
    project_template = ProjectTemplate.query.get_or_404(template_id)

    form = EditProjectTemplateForm(obj=project_template)
    form.category.choices = project_template_manager.load_categories()

    if form.validate_on_submit():
        # Update the project template's fields based on the form data
        form.populate_obj(project_template)

        # Save the changes to the database
        db.session.commit()

        flash("Project Template updated successfully!", "success")
        return redirect(url_for("project_template.list"))

    ai_toolbox_actions = [
        {
            "caption": "Say Hello",
            "icon": "fas fa-icon1",
            "js_function": "say_hello",
        },
        {
            "caption": "Help",
            "icon": "fas fa-icon2",
            "js_function": "help_chat",
        },
    ]

    return render_template(
        "edit_project_template.html",
        form=form,
        template=project_template,
        ai_toolbox_actions=ai_toolbox_actions,
    )
