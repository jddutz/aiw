# app/routes/www/system_message_template.py

from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from app import db

from app.models import ChatSystemMessage
from app.forms.system_message_edit_form import SystemMessageEditForm

system_message_blueprint = Blueprint("system_message", __name__)


@system_message_blueprint.route("/", methods=["GET"])
def index():
    search_terms = request.args.get("search_terms", default=None)

    if search_terms:
        # Handle the search terms as needed.
        return render_template("system_message_search_results.html")

    data = ChatSystemMessage.query.order_by(ChatSystemMessage.title).all()
    return render_template(
        "admin/system_message/index.html",
        data=data,
        show_ai_toolbox=True,
    )


@system_message_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = SystemMessageEditForm()

    if form.validate_on_submit():
        # Create a new ChatSystemMessage object with all the provided fields
        new_system_message = ChatSystemMessage(
            title=form.title.data,
            content=form.content.data,
            type=form.type.data or None,
            associated_module=form.associated_module.data or None,
            tags=form.tags.data or None,
            version=form.version.data or None,
            is_active=form.is_active.data,
            created_by=form.created_by.data or None,
            updated_by=form.updated_by.data or None,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        # Add the new ChatSystemMessage object to the database
        db.session.add(new_system_message)
        db.session.commit()

        flash(
            f"System Message, {new_system_message.title}, created successfully!",
            "success",
        )
        return redirect(url_for("system_message.index"))

    # The edit template will render differently depending on whether or not a model is provided
    return render_template(
        "admin/system_message/edit.html",
        form=form,
        system_message=None,
        show_ai_toolbox=True,
    )


@system_message_blueprint.route("/<int:system_message_id>/detail", methods=["GET"])
def detail(system_message_id):
    system_message = ChatSystemMessage.query.get_or_404(system_message_id)

    return render_template(
        "admin/system_message/detail.html",
        data=system_message,
        show_ai_toolbox=True,
    )


@system_message_blueprint.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    model = ChatSystemMessage.query.get_or_404(id)

    form = SystemMessageEditForm(obj=model)

    if form.validate_on_submit():
        # Update  fields based on the form data
        form.populate_obj(model)

        # Save the changes to the database
        db.session.commit()

        flash(f"System Message, {model.title}, updated successfully!", "success")
        return redirect(url_for("system_message.index"))

    return render_template(
        "admin/system_message/edit.html",
        form=form,
        model=model,
        show_ai_toolbox=True,
    )


@system_message_blueprint.route(
    "/<int:system_message_id>/delete", methods=["GET", "POST"]
)
def delete(system_message_id):
    return render_template("admin/system_message/delete.html")
