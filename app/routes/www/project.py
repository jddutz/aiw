# app/routes/www/project.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import current_user
from sqlalchemy import or_

from app import db
from app.models import WritingProjectModel, ProjectTemplateModel, GenreModel
from app.forms.writing_project_create_form import WritingProjectCreateForm
from app.forms.writing_project_edit_form import WritingProjectEditForm
from app.forms.ai_dialog_form import AIDialogForm
from app.services import ai_interface as ai

MODEL = WritingProjectModel
MODEL_DESC = "Writing Project"
CREATE_FORM = WritingProjectCreateForm
EDIT_FORM = WritingProjectEditForm

ROUTE_NAME = "project"
TEMPLATE_PATH = f"www/{ROUTE_NAME}"

blueprint = Blueprint("project", __name__)


@blueprint.route("/", methods=["GET"])
def list():
    search_term = request.args.get("q", "")
    if search_term:
        text_fields_filter = or_(
            MODEL.title.like(f"%{search_term}%"),
            MODEL.description.like(f"%{search_term}%"),
            MODEL.project_type.like(f"%{search_term}%"),
            MODEL.genre.like(name=f"%{search_term}%"),
        )

        tags_filter = MODEL.tags.any(name=f"%{search_term}%")

        search_filter = or_(text_fields_filter, tags_filter)

        data = MODEL.query.filter(search_filter).all()
    else:
        data = MODEL.query.all()

    return render_template(
        f"{TEMPLATE_PATH}/list.html",
        data=data,
        show_ai_toolbox=True,
        search_term=search_term,
    )


@blueprint.route("/new", methods=["GET", "POST"])
def new():
    ai_dialog = AIDialogForm()

    form = CREATE_FORM()
    form.genre_id.choices = [(genre.id, genre.name) for genre in GenreModel.query.all()]
    form.project_template.choices = [
        (template.id, template.title) for template in ProjectTemplateModel.query.all()
    ]

    if ai_dialog.validate_on_submit():
        project_description = ai_dialog.input_field.data
        form.title.data = ai.get_project_title(project_description)
        form.description.data = ai.get_project_summary(project_description)
        form.project_template.data = ai.get_project_template(project_description)
        form.genre_id.data = ai.get_project_genre(project_description)
        form.tags.data = ai.get_project_tags(project_description)

    return render_template(
        f"{TEMPLATE_PATH}/create.html",
        form=form,
        model=None,
        show_ai_toolbox=True,
        ai_toolbox_actions=[
            {
                "caption": "Update Description",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Description')",
            },
        ],
    )


@blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = CREATE_FORM()
    form.genre_id.choices = [(genre.id, genre.name) for genre in GenreModel.query.all()]
    form.project_template.choices = [
        (template.id, template.title) for template in ProjectTemplateModel.query.all()
    ]

    if form.validate_on_submit():
        model = MODEL()

        if form.project_template.data:
            project_template = ProjectTemplateModel.query.get(
                form.project_template.data
            )
            model.project_type = project_template.title
            # TODO: unpack project_template.structure and create the appropriate sections

        model.owner_id = current_user.id

        if form.genre_id.data:
            model.genre_id = form.genre_id.data

        if form.tags.data:
            model.tags = (
                form.tags.data
            )  # TODO: We need to parse the list of tags and make sure they are comma-separated

        form.populate_obj(obj=model)

        db.session.add(model)
        db.session.commit()

        flash(
            f"{MODEL_DESC}, {model.title}, created successfully!",
            "success",
        )
        return redirect(url_for(f"{ROUTE_NAME}.list"))

    return render_template(
        f"{TEMPLATE_PATH}/create.html",
        form=form,
        model=None,
        show_ai_toolbox=True,
        ai_toolbox_actions=[
            {
                "caption": "Update Description",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Description')",
            },
        ],
    )


@blueprint.route("/<int:id>", methods=["GET"])
def detail(id):
    model = MODEL.query.get_or_404(id)

    return render_template(
        f"{TEMPLATE_PATH}/detail.html",
        model=model,
        show_ai_toolbox=True,
    )


@blueprint.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    model = MODEL.query.get_or_404(id)

    form = EDIT_FORM(obj=model)
    form.genre_id.choices = [(genre.id, genre.name) for genre in GenreModel.query.all()]

    if form.validate_on_submit():
        form.populate_obj(model)
        db.session.commit()

        flash(
            f"{MODEL_DESC}, {model.title} updated successfully!",
            "success",
        )
        return redirect(url_for(f"{ROUTE_NAME}.list"))

    return render_template(
        f"{TEMPLATE_PATH}/edit.html",
        form=form,
        model=model,
        show_ai_toolbox=True,
        ai_toolbox_actions=[
            {
                "caption": "Update Description",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Template Description')",
            },
        ],
    )


@blueprint.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    # Retrieve the model by its ID
    model = MODEL.query.get_or_404(id)
    db.session.delete(model)
    db.session.commit()

    flash(f"{MODEL_DESC}, {model.title}, deleted!", "success")

    return redirect(url_for(f"{ROUTE_NAME}.list"))
