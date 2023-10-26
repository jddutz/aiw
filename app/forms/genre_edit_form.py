# app/forms/genre_edit_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class GenreEditForm(FlaskForm):
    id = HiddenField()
    name = StringField(
        "Genre Name", validators=[DataRequired(), Length(min=7, max=128)]
    )
    description = TextAreaField("Description", validators=[DataRequired()])
    imageref = StringField(
        "Image Reference", validators=[DataRequired(), Length(min=1, max=255)]
    )

    submit = SubmitField("Save")
