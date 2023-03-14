from flask import redirect, url_for, request, flash, render_template
from pupsite import db
from pupsite.member.forms import LoginForm
from pupsite.member.routes import memberblueprint
from flask_login import current_user, login_user

from pupsite.models import Member


@memberblueprint.route("/login", method=["GET"])
def login():
    """
    Logs in the user if verified
    """
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("publicblueprint.home"))
    if login_form.validate_on_submit():
        member = db.session.execute(
            db.session.select(Member, login_form.email.data)
        ).scalar_one()

        if member and Member.verify_password(login_form.password.data):
            login_user(member)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(location=url_for("membersblueprint.home"))

        else:
            flash("Loginf unsuccessful")
    return render_template("login.html", login_form=login_form)
