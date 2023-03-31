from flask_login import logout_user, login_required
from flask import redirect, url_for

from pupsite.member.routes import memberblueprint


@memberblueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    """
    Logout a user and redirect to the home page
    """
    logout_user()
    return redirect(url_for("publicblueprint.home"))
