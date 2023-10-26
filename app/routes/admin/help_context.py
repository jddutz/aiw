# app/routes/admin/help_context.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from sqlalchemy import or_

from app import db
from app.models import HelpContextModel
from app.forms.help_context_edit_form import HelpContextEditForm

MODEL = HelpContextModel
MODEL_DESC = "Help Context"
EDIT_FORM = HelpContextEditForm

ROUTE_NAME = "help_context"
TEMPLATE_PATH = f"admin/{ROUTE_NAME}"

CACHED_MODULES = None
UPDATE_CACHE = None


async def load_modules():
    global CACHED_MODULES
    global UPDATE_CACHE

    # Use cached categories if available
    if CACHED_MODULES:
        if UPDATE_CACHE and UPDATE_CACHE < datetime.utcnow():
            return CACHED_MODULES

    modules = (
        await db.async_session.query(HelpContextModel.id, HelpContextModel.title)
        .distinct()
        .order_by(HelpContextModel.id.asc())
        .all()
    )

    # Convert categories from list of tuples to a list of strings
    CACHED_MODULES = [(module[0], module[0]) for module in modules]
    UPDATE_CACHE = datetime.utcnow() + timedelta(minutes=10)

    return CACHED_MODULES


blueprint = Blueprint(ROUTE_NAME, __name__)


@blueprint.route("/", methods=["GET"])
async def list():
    search_term = request.args.get("q", "")
    if search_term:
        search_filter = or_(
            MODEL.context_id.like(f"%{search_term}%"),
            MODEL.title.like(f"%{search_term}%"),
            MODEL.content.like(f"%{search_term}%"),
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
async def create():
    form = EDIT_FORM()

    if form.validate_on_submit():
        model = MODEL()
        form.populate_obj(obj=model)
        await db.async_session.add(model)
        await db.async_session.commit()

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
async def detail(id):
    model = MODEL.query.get_or_404(id)

    return render_template(
        f"{TEMPLATE_PATH}/detail.html",
        model=model,
        show_ai_toolbox=True,
    )


@blueprint.route("/<int:id>/edit", methods=["GET", "POST"])
async def edit(id):
    model = MODEL.query.get_or_404(id)

    form = EDIT_FORM(obj=model)

    if form.validate_on_submit():
        form.populate_obj(model)
        await db.async_session.commit()

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
async def delete(id):
    # Retrieve the model by its ID
    model = MODEL.query.get_or_404(id)
    await db.async_session.delete(model)
    await db.async_session.commit()

    flash(f"{MODEL_DESC}, {model.title}, deleted!", "success")

    return redirect(url_for(f"{ROUTE_NAME}.list"))
