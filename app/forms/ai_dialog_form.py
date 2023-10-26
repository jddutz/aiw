# app/forms/ai_dialog_input_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class AIDialogForm(FlaskForm):
    input_field = TextAreaField("Input Text", validators=[DataRequired()])
    submit_button = SubmitField("Submit")
