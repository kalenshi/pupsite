from flask import flash, render_template, redirect
from flask_login import login_required, current_user
from pupsite.member.routes import memberblueprint


@memberblueprint.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html", member=current_user)
