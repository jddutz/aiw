# app/routes/www/model_template.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from app import db

# from app.models import Model
# from app.forms.model_edit_form import ModelEditForm

model_blueprint = Blueprint("model", __name__)


@model_blueprint.route("/", methods=["GET"])
def index():
    search_terms = request.args.get("search_terms", default=None)

    if search_terms:
        # Handle the search terms as needed.
        return render_template("model_search_results.html")

    return render_template("model_list.html")


@model_blueprint.route("/create", methods=["GET", "POST"])
async def create():
    # form = ModelEditForm

    # The edit template will render differently depending on whether or not a model is provided
    return render_template(
        "model_edit.html",
        # form=form,
        model=None,
        show_ai_toolbox=True,
    )


@model_blueprint.route("/<int:model_id>/detail", methods=["GET"])
async def detail(model_id):
    # model = Model.query.get_or_404(model_id)

    return render_template(
        "model_detail.html",
        # data=model,
        show_ai_toolbox=True,
    )


@model_blueprint.route("/<int:model_id>/edit", methods=["GET", "POST"])
async def edit(model_id):
    # form = ModelEditForm

    return render_template(
        "model_edit.html",
        # form=form,
        model=None,
        show_ai_toolbox=True,
    )


@model_blueprint.route("/<int:model_id>/delete", methods=["GET", "POST"])
async def delete(model_id):
    return render_template("model_delete.html")
