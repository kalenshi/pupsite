from flask import render_template

from werkzeug.exceptions import NotFound
from pupsite.error_handlers.routes import error_blueprint


@error_blueprint.app_errorhandler(NotFound)
def page_not_found(error):
    """
    Registers page not found error
    Args:
        error: error encountered

    Returns:
        response: Http 404 response
    """
    return render_template("error_page.html", error=error)
