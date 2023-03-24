from flask import render_template, redirect, flash, abort, url_for, request
from flask_login import login_required, current_user

from pupsite import db
from pupsite.models import Pup
from pupsite.pups.forms.pup_update import UpdatePupForm
from pupsite.pups.routes import pupsblueprint
from pupsite.utils.save_picture import save_picture_by_dimension


@pupsblueprint.route("/pup/<int:pup_id>/update", methods=["GET", "POST"])
@login_required
def update_pup(pup_id):
    """
    Route to update details about a particular pup given by the pup_id
    Ensure Only the owner of the pup can update details about the pup
    Args:
        pup_id (int): The primary key of the pup to be updated

    Returns:
        response : Returns Http response
    """
    update_form = UpdatePupForm()
    pup = db.get_or_404(Pup, pup_id)

    if current_user.id != pup.owner_id:
        flash("Forbidden! You can only update your own Pup", category="danger")
        return abort(403)
    if update_form.validate_on_submit():
        if update_form.picture.data:
            pup.picture = save_picture_by_dimension(update_form.picture.data)
        pup.breed = update_form.breed.data
        pup.details = update_form.details.data
        pup.age = update_form.age.data
        pup.picture = update_form.age.data
        db.session.commit()
        return redirect(url_for("pupsblueprint.pups_list"))
    elif request.method == "GET":
        update_form.breed.data = pup.breed
        update_form.details.data = pup.details
        update_form.age.data = pup.age
    return render_template("update_pup.html", update_form=update_form, pup=pup)
