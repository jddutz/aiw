# app/routes/www/project.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import current_user
from sqlalchemy import or_

from app import db
from app.models import WritingProjectModel, ProjectTemplateModel, GenreModel
from app.forms.writing_project_create_form import WritingProjectCreateForm
from app.forms.writing_project_edit_form import WritingProjectEditForm

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


@blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = CREATE_FORM()
    form.genre_id.choices = [(genre.id, genre.name) for genre in GenreModel.query.all()]
    form.project_template.choices = [
        (template.id, template.project_template_name)
        for template in ProjectTemplateModel.query.all()
    ]

    if form.validate_on_submit():
        model = MODEL()

        project_template_id = form.project_template.data
        if project_template_id:
            project_template = ProjectTemplateModel.query.get(project_template_id)
            model.project_type = project_template.project_template_name
            # TODO: unpack project_template.structure

        tags_str = [tag.strip() for tag in form.tags.data.split(",")]
        tags_obj = [Tag(name=tag_name) for tag_name in tags_str if tag_name != ""]
        model.tags = tags_obj

        model.owner_id = current_user.id

        # remove the tags field, if we leave it in, populate_obj will throw a TypeError
        del form.tags
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
    form.category.choices = load_genres()

    if form.validate_on_submit():
        form.populate_obj(model)
        db.session.commit()

        flash(
            f"{MODEL_DESC}, {model.project_template_name} updated successfully!",
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

    flash(f"{MODEL_DESC}, {model.project_template_name}, deleted!", "success")

    return redirect(url_for(f"{ROUTE_NAME}.list"))
