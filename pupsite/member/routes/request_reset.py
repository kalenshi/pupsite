from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from sqlalchemy.exc import NoResultFound

from pupsite.member.forms.request_reset_form import RequestResetForm
from pupsite.member.routes import memberblueprint
from pupsite import db
from pupsite.member.utils.send_mail import SendMail
from pupsite.models import Member


@memberblueprint.route("/request-reset-password", methods=["GET", "POST"])
def request_reset():
    request_form = RequestResetForm()
    if current_user.is_authenticated:
        return redirect(url_for("publicblueprint.home"))
    if request_form.validate_on_submit():
        try:
            member = db.session.execute(
                db.select(Member).filter_by(email=request_form.email.data)
            ).scalar_one()

        except NoResultFound:
            flash("Email does not exist", category="warning")
            return redirect(url_for("memberblueprint.add_member"))
        else:
            recipients = [member.email, ]
            mailer = SendMail(
                subject="Change your password",
                recipients=recipients
            )
            mailer.send_mail(token=member.get_reset_token())
            flash("Check your email for a reset link", category="success")
            return redirect(url_for("memberblueprint.login"))
    return render_template("request_reset.html", request_form=request_form)
