from flask import render_template, flash, redirect, url_for
from flask_login import current_user

from pupsite import db
from pupsite.member.forms.reset_password import ResetPasswordForm
from pupsite.member.routes import memberblueprint
from pupsite.models import Member


@memberblueprint.route("/reset-password/<string:token>", methods=["GET", "POST"])
def reset_password(token):
    reset_form = ResetPasswordForm()
    if current_user.is_authenticated:
        return redirect(url_for("publicblueprint.home"))
    member = Member.verify_reset_token(token)
    if not member:
        flash("The reset Token is Invalid or expired", category="warning")
        return redirect(url_for("memberblueprint.request_reset"))
    if reset_form.validate_on_submit():
        member.password = Member.set_password(reset_form.password.data)
        db.session.commit()
        flash("Password Reset Successful. Login with your New password", category="success")
        return redirect(url_for("memberblueprint.login"))
    return render_template("reset_password.html", reset_form=reset_form)
