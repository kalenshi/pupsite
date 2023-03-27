import os
from flask import Blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

error_blueprint = Blueprint(
    "error_blueprint",
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)
