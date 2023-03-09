from flask import render_template, url_for

from pupsite import db
from pupsite.models import Pup
from pupsite.pups.routes import pupsblueprint


@pupsblueprint.route("/pups/<int:pup_id>", methods=["GET"])
def pup_page(pup_id):
    """
    Show information about a particular pup

    Args:
        pup_id(int) : The primary key of the given Pup
    """
    pup = db.get_or_404(Pup, pup_id)
    return render_template("pup_page.html", title=f"Pup - {pup.id}", pup=pup)
