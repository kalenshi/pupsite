from flask import redirect, url_for, render_template, flash

from pupsite import db
from pupsite.models import Pup
from pupsite.pups.forms.add_pup import AddPupForm
from pupsite.pups.routes import pupsblueprint
from pupsite.utils.save_picture import save_picture_by_dimensions


@pupsblueprint.route("/pup/add", methods=["GET", "POST"])
def add_pup():
    """
    Route for creating a new Pup connection with the owner
    """
    form = AddPupForm()
    if form.validate_on_submit():
        picture = "default.png"
        if form.picture.data:
            picture = save_picture_by_dimensions(form.picture.data)
        pup = Pup(
            name=form.name.data,
            breed=form.breed.data,
            age=form.age.data,
            details=form.details.data,
            owner_id=form.owner.data or 1,
            picture=picture
        )
        db.session.add(pup)
        db.session.commit()
        flash("Pup Added Successfully", category="success")
        return redirect(url_for("pupsblueprint.pups_list"))
    return render_template("add_pup.html", title="add a pup", add_form=form)
