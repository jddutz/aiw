# app/routes/admin/genre.py

from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from sqlalchemy import or_

from app import db
from app.models import GenreModel
from app.forms.genre_edit_form import GenreEditForm

MODEL = GenreModel
MODEL_DESC = "Genre"
EDIT_FORM = GenreEditForm

ROUTE_NAME = "genre"
TEMPLATE_PATH = f"admin/{ROUTE_NAME}"

CACHED_MODULES = None
UPDATE_CACHE = None


blueprint = Blueprint(ROUTE_NAME, __name__)


@blueprint.route("/", methods=["GET"])
def list():
    search_term = request.args.get("q", "")
    if search_term:
        search_filter = or_(
            MODEL.name.like(f"%{search_term}%"),
            MODEL.description.like(f"%{search_term}%"),
        )

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

    if form.validate_on_submit():
        model = MODEL()
        form.populate_obj(obj=model)
        db.session.add(model)
        db.session.commit()

        flash(
            f"{MODEL_DESC}, {model.title}, created successfully!",
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
                "js_function": "send_instructions('Update Help Context Content')",
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
                "caption": "Update Help Context",
                "icon": "fas fa-comment",
                "js_function": "send_instructions('Update Help Context')",
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
