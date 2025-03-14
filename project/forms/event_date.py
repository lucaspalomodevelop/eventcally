from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField, SelectField, StringField, SubmitField
from wtforms.validators import Optional

from project.forms.common import distance_choices
from project.forms.widgets import CustomDateField


class FindEventDateBaseForm(FlaskForm):
    class Meta:
        csrf = False

    date_from = CustomDateField(lazy_gettext("From"), validators=[Optional()])
    date_to = CustomDateField(
        lazy_gettext("to"), set_end_of_day=True, validators=[Optional()]
    )
    keyword = StringField(lazy_gettext("Keyword"), validators=[Optional()])
    category_id = SelectField(
        lazy_gettext("Category"), validators=[Optional()], coerce=int
    )


class FindEventDateForm(FindEventDateBaseForm):
    coordinate = HiddenField(validators=[Optional()])
    location = SelectField(lazy_gettext("Location"), validators=[Optional()])
    distance = SelectField(
        lazy_gettext("Distance"),
        validators=[Optional()],
        coerce=int,
        choices=distance_choices,
    )
    event_list_id = HiddenField(validators=[Optional()])
    admin_unit_id = SelectField(
        lazy_gettext("Organization"),
        validators=[Optional()],
        coerce=int,
    )
    organizer_id = SelectField(
        lazy_gettext("Organizer"),
        validators=[Optional()],
        coerce=int,
    )
    not_referenced = BooleanField(
        lazy_gettext("Show unreferenced events only"),
        validators=[Optional()],
    )
    exclude_recurring = BooleanField(
        lazy_gettext("Exclude recurring events"),
        validators=[Optional()],
    )
    postal_code = StringField(lazy_gettext("Postal code"), validators=[Optional()])

    created_at_from = CustomDateField(lazy_gettext("From"), validators=[Optional()])
    created_at_to = CustomDateField(
        lazy_gettext("to"), set_end_of_day=True, validators=[Optional()]
    )
    sort = SelectField(
        lazy_gettext("Sort"),
        choices=[
            (
                "start",
                lazy_gettext("Earliest start first"),
            ),
            (
                "-created_at",
                lazy_gettext("Newest first"),
            ),
        ],
        default="start",
    )

    submit = SubmitField(lazy_gettext("Find events"))


class FindEventDateWidgetForm(FindEventDateBaseForm):
    s_ft = HiddenField(validators=[Optional()])
    s_bg = HiddenField(validators=[Optional()])
    s_pr = HiddenField(validators=[Optional()])
    s_li = HiddenField(validators=[Optional()])

    submit = SubmitField(lazy_gettext("Find"))
