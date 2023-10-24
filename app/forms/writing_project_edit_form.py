# app/forms/writing_project_edit_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from app.models import ProjectTemplate


class WritingProjectEditForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=120)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=500)])

    visibility = SelectField(
        "Visibility",
        choices=[("public", "Public"), ("private", "Private")],
        validators=[DataRequired()],
    )

    project_type = StringField(
        "Project Type", validators=[DataRequired(), Length(min=1, max=120)]
    )

    # Dropdown for genre. Coercion to integer is used to save the ID of the genre in the model.
    genre = SelectField(
        "Genre",
        coerce=int,  # This will convert the selected option to integer.
        validators=[DataRequired()],
    )

    tags = StringField(
        "Tags", validators=[Optional(), Length(max=500)]
    )  # This can be further improved with better tag handling.

    submit = SubmitField("Save")
