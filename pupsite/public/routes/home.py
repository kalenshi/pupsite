from flask import render_template
from pupsite.public.routes import publicblueprint


@publicblueprint.route("/", methods=["GET"])
@publicblueprint.route("/home", methods=["GET"])
def home():
    """
    View for the home page of the pup site
    Returns:
         http response: Returns a http response object
    """
    return render_template("home.html")
