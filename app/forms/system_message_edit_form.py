# app/forms/system_message_edit_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

SYSTEM_MESSAGE_TYPES = [
    ("instruction", "Instructional"),
    # ... add more types as needed
]

ASSOCIATED_MODULES = [
    ("module1", "Module 1"),
    ("module2", "Module 2"),
    # ... add more modules as needed
]


class SystemMessageEditForm(FlaskForm):
    """Form for editing system messages."""

    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    content = TextAreaField("Content", validators=[DataRequired()])
    type = SelectField("Type", choices=SYSTEM_MESSAGE_TYPES, validators=[Optional()])
    associated_module = SelectField(
        "Associated Module", choices=ASSOCIATED_MODULES, validators=[Optional()]
    )
    tags = StringField("Tags", validators=[Length(max=255), Optional()])
    version = StringField("Version", validators=[Length(max=50), Optional()])
    is_active = BooleanField("Active", default=True)
    created_by = StringField("Created By", validators=[Length(max=100), Optional()])
    updated_by = StringField("Updated By", validators=[Length(max=100), Optional()])
    submit = SubmitField("Submit")
