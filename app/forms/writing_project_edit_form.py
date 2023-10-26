# app/forms/writing_project_edit_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Optional


class WritingProjectEditForm(FlaskForm):
    id = HiddenField()
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

    genre_id = SelectField(
        "GenreModel",
        coerce=int,
        validators=[DataRequired()],
    )

    tags = StringField("Tags", validators=[Optional(), Length(max=500)])

    submit = SubmitField("Save")
