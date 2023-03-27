from flask import render_template

from werkzeug.exceptions import InternalServerError
from pupsite.error_handlers.routes import error_blueprint


@error_blueprint.app_errorhandler(InternalServerError)
def internal_error(error):
    """
    Registers page not found error
    Args:
        error: error encountered

    Returns:
        response: Http 500 response
    """
    return render_template("internal_error.html", error=error)
