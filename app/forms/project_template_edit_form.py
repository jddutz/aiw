# app/forms/project_template_edit_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class ProjectTemplateEditForm(FlaskForm):
    id = HiddenField()
    category = StringField("Category", validators=[DataRequired(), Length(max=50)])
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=255)])
    description = TextAreaField("Description", validators=[DataRequired()])
    methodology = TextAreaField("Methodology", validators=[DataRequired()])
    length = StringField("Length", validators=[DataRequired(), Length(max=255)])
    tags = TextAreaField(
        "Tags (Separated by semicolons)",
        validators=[Optional()],
        description="For example: tag1;tag2;tag3",
    )
    links = TextAreaField(
        "Links (Separated by semicolons)",
        validators=[Optional()],
        description="For example: link1;link2;link3",
    )
    structure = TextAreaField(
        "Structure (JSON format)",
        validators=[Optional()],
        description="Provide a serialized JSON structure.",
    )
    imageref = StringField("Image Reference", validators=[Optional(), Length(max=255)])
    submit = SubmitField("Save")
