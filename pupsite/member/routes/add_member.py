from flask import render_template, url_for, redirect, flash
from sqlalchemy.exc import NoResultFound

from pupsite import db
from pupsite.member.forms import MemberForm
from pupsite.member.routes import memberblueprint
from pupsite.models import Member


@memberblueprint.route("/member/add", methods=["GET", "POST"])
def add_member():
    """
    Route for adding  a new member to the database
    """
    form = MemberForm()
    if form.validate_on_submit():
        try:
            _ = db.session.execute(db.select(Member).filter_by(email=form.email.data)).scalar_one()
        except NoResultFound:
            member = Member(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
            )
            # Encrypt the password before adding it to the database

            member.password = member.set_password(form.password.data)
            db.session.add(member)
            db.session.commit()
            flash(f"Member Created with Email `{form.email.data}`", category="success")
            return redirect(url_for("pupsblueprint.pups_list"))
        else:
            flash(f"The email `{form.email.data}` Is already associated with an Account", category="danger")

    return render_template("add_member.html", title="New member", add_form=form)
