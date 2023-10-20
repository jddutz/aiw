# app/forms/new_project_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from app.models import ProjectTemplate


class ProjectEditForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=120)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=500)])

    # Dropdown of available ProjectTemplates
    project_template = SelectField(
        "Project Template",
        validators=[Optional()],
    )

    # Assuming 'Public' and 'Private' are the visibility options. Add or modify as needed.
    visibility = SelectField(
        "Visibility",
        choices=[("public", "Public"), ("private", "Private")],
        validators=[DataRequired()],
    )

    tags = StringField(
        "Tags", validators=[Optional(), Length(max=500)]
    )  # Here, tags are input as comma-separated values.

    submit = SubmitField("Create Project")
