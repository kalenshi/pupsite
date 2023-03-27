from flask import render_template

from werkzeug.exceptions import Forbidden
from pupsite.error_handlers.routes import error_blueprint


@error_blueprint.app_errorhandler(Forbidden)
def not_allowed(error):
    """
    Registers page not found error
    Args:
        error: error encountered

    Returns:
        response: Http 403 response
    """
    return render_template("not_authorized.html", error=error)
