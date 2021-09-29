from flask_babelex import lazy_gettext
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, TextAreaField
from wtforms.validators import Optional

from project.forms.widgets import MultiCheckboxField


class AdminSettingsForm(FlaskForm):
    tos = TextAreaField(lazy_gettext("Terms of service"), validators=[Optional()])
    legal_notice = TextAreaField(lazy_gettext("Legal notice"), validators=[Optional()])
    contact = TextAreaField(lazy_gettext("Contact"), validators=[Optional()])
    privacy = TextAreaField(lazy_gettext("Privacy"), validators=[Optional()])

    submit = SubmitField(lazy_gettext("Save"))


class UpdateUserForm(FlaskForm):
    roles = MultiCheckboxField(lazy_gettext("Roles"))
    submit = SubmitField(lazy_gettext("Update user"))


class UpdateAdminUnitForm(FlaskForm):
    incoming_reference_requests_allowed = BooleanField(
        lazy_gettext("Incoming reference requests allowed"),
        description=lazy_gettext(
            "If set, other organizations can ask this organization to reference their event."
        ),
        validators=[Optional()],
    )
    suggestions_enabled = BooleanField(
        lazy_gettext("Suggestions enabled"),
        description=lazy_gettext("If set, the organization can work with suggestions."),
        validators=[Optional()],
    )
    can_create_other = BooleanField(
        lazy_gettext("Create other organizations"),
        description=lazy_gettext(
            "If set, members of the organization can create other organizations."
        ),
        validators=[Optional()],
    )
    can_verify_other = BooleanField(
        lazy_gettext("Verify other organizations"),
        description=lazy_gettext(
            "If set, members of the organization can verify other organizations."
        ),
        validators=[Optional()],
    )
    submit = SubmitField(lazy_gettext("Update organization"))
