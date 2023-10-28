# app/forms/writing_project_create_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from app.models import ProjectTemplateModel


class WritingProjectCreateForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=255)])
    description = TextAreaField("Description", validators=[Optional()])

    # Dropdown of available ProjectTemplates
    project_template = SelectField(
        "Project Template",
        coerce=int,
        validators=[Optional()],
    )

    genre_id = SelectField(
        "Genre",
        coerce=int,
        validators=[DataRequired()],
    )

    tags = StringField("Tags", validators=[Optional()])

    visibility = SelectField(
        "Visibility",
        choices=[("public", "Public"), ("private", "Private")],
        validators=[DataRequired()],
    )

    submit = SubmitField("Save")
