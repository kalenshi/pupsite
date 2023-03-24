from flask import redirect, url_for, flash, abort
from flask_login import current_user, login_required

from pupsite import db
from pupsite.models import Pup
from pupsite.pups.routes import pupsblueprint


@pupsblueprint.route("/pup/<int:pup_id>/delete", methods=["GET", "POST"])
@login_required
def delete_pup(pup_id):
    """
    Route for Deleting a Pup from the database
    """

    pup = db.get_or_404(Pup, pup_id)
    if pup.owner_id != current_user.id:
        flash("Action forbidden. You can't delete someone else's pup. ")
        return abort(403)
    db.session.delete(pup)
    db.session.commit()
    flash(f"You Successfully Deleted the Pup called {pup.name}", category="success")
    return redirect(url_for("pupsblueprint.pups_list"))
