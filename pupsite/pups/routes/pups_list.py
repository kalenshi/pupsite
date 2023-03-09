from flask import render_template

from pupsite import db
from pupsite.models import Pup
from pupsite.pups.routes import pupsblueprint


@pupsblueprint.route("/pups", methods=["GET"])
def pups_list():
    """
    Lists all the pupsblueprint in the database

    Returns:
        list :A list of all the pupsblueprint in the database
    """
    pups = db.session.execute(db.select(Pup)).scalars()
    return render_template("pupslist.html", title="Pups", pups=pups)
