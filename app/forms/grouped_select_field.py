# app/forms/grouped_select_field.py

from wtforms.fields import SelectFieldBase
from markupsafe import escape, Markup
from wtforms.widgets import Select, html_params


class GroupedSelectWidget(Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = ["<select %s>" % html_params(name=field.name, **kwargs)]

        if field.choices is not None:
            for item1, item2 in field.choices:
                if isinstance(item2, (list, tuple)):
                    group_label = item1
                    group_items = item2
                    html.append('<optgroup label="%s">' % escape(str(group_label)))
                    for val, label in group_items:
                        html.append(
                            self.render_option(
                                val, label, field.coerce(val) == field.data
                            )
                        )
                    html.append("</optgroup>")
                else:
                    html.append(
                        self.render_option(
                            item1, item2, field.coerce(item1) == field.data
                        )
                    )
        html.append("</select>")
        return Markup("".join(html))


class GroupedSelectField(SelectFieldBase):
    widget = GroupedSelectWidget()

    def __init__(self, label=None, validators=None, coerce=str, choices=None, **kwargs):
        super(GroupedSelectField, self).__init__(label, validators, **kwargs)
        self.coerce = coerce
        self.choices = choices

    def iter_choices(self):
        for value, label in self.choices:
            yield (
                label,
                [(val, lab, self.coerce(val) == self.data) for val, lab in value],
            )

    def pre_validate(self, form):
        for group, choices in self.choices:
            for choice in choices:
                if choice[0] == self.data:
                    break
            else:
                continue
            break
        else:
            raise ValueError(self.gettext("Not a valid choice"))
