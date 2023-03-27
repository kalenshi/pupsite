from flask import redirect, url_for, request, flash, render_template
from sqlalchemy.exc import NoResultFound

from pupsite import db
from pupsite.member.forms import LoginForm
from pupsite.member.routes import memberblueprint
from flask_login import current_user, login_user

from pupsite.models import Member


@memberblueprint.route("/login", methods=["GET", "POST"])
def login():
    """
    Logs in the user if verified
    """
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("publicblueprint.home"))
    if login_form.validate_on_submit():
        try:
            member = db.session.execute(
                db.select(Member).filter_by(email=login_form.email.data)
            ).scalar_one()
        except NoResultFound:
            flash("Loging unsuccessful Please check your email and or password", category="danger")
        else:
            if member and member.verify_password(password=login_form.password.data):
                login_user(member, remember=login_form.remember)
                next_page = request.args.get("next")
                return redirect(next_page) if next_page else redirect(
                    url_for("publicblueprint.home")
                )
            else:
                flash(
                    "Loging unsuccessful Please check your email and or password", category="danger"
                )
    return render_template("login.html", login_form=login_form)
