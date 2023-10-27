# app/forms/writing_project_create_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from app.models import ProjectTemplateModel


class WritingProjectCreateForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=120)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=500)])

    # Dropdown of available ProjectTemplates
    project_template = SelectField(
        "Project Template",
        coerce=int,  # This will convert the selected option to integer.
        validators=[Optional()],
    )

    genre_id = SelectField(
        "GenreModel",
        coerce=int,
        validators=[DataRequired()],
    )

    tags = StringField("Tags", validators=[Optional(), Length(max=500)])

    visibility = SelectField(
        "Visibility",
        choices=[("public", "Public"), ("private", "Private")],
        validators=[DataRequired()],
    )

    submit = SubmitField("Save")
