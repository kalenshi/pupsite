from flask import render_template, url_for, redirect, flash

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
        member = Member(
            name=form.name.data,
            email=form.email.data
        )
        db.session.add(member)
        db.session.commit()
        flash(f"Member Created with Email{form.email.data}", category="success")
        return redirect(url_for("pupsblueprint.pups_list"))
    return render_template("add_member.html", title="New member", add_form=form)
