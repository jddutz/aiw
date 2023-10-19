# app/routes/www/help_context.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from app import db
from app.models import HelpContext
from app.forms.help_context_edit_form import HelpContextEditForm

help_context_blueprint = Blueprint("help_context", __name__)


@help_context_blueprint.route("/", methods=["GET"])
def index():
    data = HelpContext.query.order_by(HelpContext.context_id).all()
    return render_template(
        "help_context_index.html",
        data=data,
        show_ai_toolbox=True,
    )


@help_context_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = HelpContextEditForm()  # Instantiate the form object

    if form.validate_on_submit():
        # Create a new HelpContext object
        new_help_context = HelpContext(
            context_id=form.context_id.data,
            content=form.content.data,
            created=datetime.utcnow(),
            modified=datetime.utcnow(),
        )

        # Add the new HelpContext object to the database
        db.session.add(new_help_context)
        db.session.commit()

        flash(
            f"Help Context, {new_help_context.context_id}, created successfully!",
            "success",
        )
        return redirect(url_for("help_context.index"))

    return render_template(
        "help_context_edit.html",
        form=form,
        help_context=None,  # No initial HelpContext data for creation
        show_ai_toolbox=True,
    )


@help_context_blueprint.route("/<int:help_context_id>/detail", methods=["GET"])
def detail(help_context_id):
    data = HelpContext.query.get_or_404(
        help_context_id
    )  # Fetch help_context by ID or return 404

    return render_template(
        "help_context_detail.html",
        data=data,
        show_ai_toolbox=True,
    )


@help_context_blueprint.route("/<int:help_context_id>/edit", methods=["GET", "POST"])
def edit(help_context_id):
    # Retrieve the project help_context by its ID
    data = HelpContext.query.get_or_404(help_context_id)

    form = HelpContextEditForm(obj=data)

    if form.validate_on_submit():
        # Update the project help_context's fields based on the form data
        form.populate_obj(data)

        # Save the changes to the database
        db.session.commit()

        flash(f"Help Context, {data.context_id}, updated successfully!", "success")
        return redirect(url_for("help_context.index"))

    return render_template(
        "help_context_edit.html",
        form=form,
        help_context=data,
        show_ai_toolbox=True,
    )


def delete():
    pass


def search():
    pass
