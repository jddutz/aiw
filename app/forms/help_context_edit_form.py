# app/forms/project_template_edit_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class HelpContextEditForm(FlaskForm):
    context_id = StringField(
        "Help Context ID", validators=[DataRequired(), Length(min=7, max=128)]
    )
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=128)])
    content = TextAreaField("Content", validators=[DataRequired()])

    submit = SubmitField("Save")
