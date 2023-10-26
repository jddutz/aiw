# app/routes/admin/project_template.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from sqlalchemy import or_

from app import db
from app.models import ProjectTemplateModel
from app.forms.project_template_edit_form import ProjectTemplateEditForm

MODEL = ProjectTemplateModel
MODEL_DESC = "Project Template"
EDIT_FORM = ProjectTemplateEditForm

ROUTE_NAME = "project_template"
TEMPLATE_PATH = f"admin/{ROUTE_NAME}"

CACHED_CATEGORIES = None
UPDATE_CACHE = None


def load_categories():
    global CACHED_CATEGORIES
    global UPDATE_CACHE

    # Use cached categories if available
    if CACHED_CATEGORIES:
        if UPDATE_CACHE and UPDATE_CACHE < datetime.utcnow():
            return CACHED_CATEGORIES

    categories = (
        db.session.query(ProjectTemplateModel.category)
        .distinct()
        .order_by(ProjectTemplateModel.category.asc())
        .all()
    )

    # Convert categories from list of tuples to a list of strings
    CACHED_CATEGORIES = [(category[0], category[0]) for category in categories]
    UPDATE_CACHE = datetime.utcnow() + timedelta(minutes=10)

    return CACHED_CATEGORIES


blueprint = Blueprint(ROUTE_NAME, __name__)


@blueprint.route("/", methods=["GET"])
def list():
    search_term = request.args.get("q", "")
    if search_term:
        text_fields_filter = or_(
            MODEL.project_template_name.like(f"%{search_term}%"),
            MODEL.description.like(f"%{search_term}%"),
            MODEL.methodology.like(f"%{search_term}%"),
            MODEL.length.like(f"%{search_term}%"),
        )

        tags_filter = MODEL.tags.any(name=f"%{search_term}%")
        genres_filter = MODEL.genres.any(name=f"%{search_term}%")

        search_filter = or_(text_fields_filter, tags_filter, genres_filter)

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
    form = EDIT_FORM()
    form.category.choices = load_categories()

    if form.validate_on_submit():
        model = MODEL()
        form.populate_obj(obj=model)
        db.session.add(model)
        db.session.commit()

        flash(
            f"{MODEL_DESC}, {model.project_template_name}, created successfully!",
            "success",
        )
        return redirect(url_for(f"{ROUTE_NAME}.list"))

    return render_template(
        f"{TEMPLATE_PATH}/edit.html",
        form=form,
        model=None,
        show_ai_toolbox=True,
        ai_toolbox_actions=[
            {
                "caption": "Update Description",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Template Description')",
            },
            {
                "caption": "Update Methodology",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Template Methodology')",
            },
            {
                "caption": "Update Project Structure",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Template Structure')",
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
    form.category.choices = load_categories()

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
            {
                "caption": "Update Methodology",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Template Methodology')",
            },
            {
                "caption": "Update Project Structure",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Project Template Structure')",
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
