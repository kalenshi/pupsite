from flask import redirect, render_template

from pupsite.public.routes import publicblueprint


@publicblueprint.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
