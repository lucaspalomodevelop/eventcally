from flask import flash, redirect, render_template, url_for
from flask_babel import gettext
from flask_security import auth_required, current_user
from sqlalchemy.exc import SQLAlchemyError

from project import app, db
from project.access import owner_access_or_401
from project.forms.oauth2_token import RevokeOAuth2TokenForm
from project.models import OAuth2Token
from project.views.utils import flash_errors, get_pagination_urls, handleSqlError


@app.route("/oauth2_token/<int:id>/revoke", methods=("GET", "POST"))
@auth_required()
def oauth2_token_revoke(id):
    oauth2_token = OAuth2Token.query.get_or_404(id)
    owner_access_or_401(oauth2_token.user_id)

    if oauth2_token.is_revoked() > 0:
        return redirect(url_for("oauth2_tokens"))

    form = RevokeOAuth2TokenForm()

    if form.validate_on_submit():
        try:
            oauth2_token.revoke_token()
            db.session.commit()
            flash(gettext("OAuth2 token successfully revoked"), "success")
            return redirect(url_for("oauth2_tokens"))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(handleSqlError(e), "danger")
    else:
        flash_errors(form)

    return render_template(
        "oauth2_token/revoke.html", form=form, oauth2_token=oauth2_token
    )


@app.route("/oauth2_tokens")
def oauth2_tokens():
    oauth2_tokens = OAuth2Token.query.filter(
        OAuth2Token.user_id == current_user.id
    ).paginate()

    return render_template(
        "oauth2_token/list.html",
        oauth2_tokens=oauth2_tokens.items,
        pagination=get_pagination_urls(oauth2_tokens),
    )
