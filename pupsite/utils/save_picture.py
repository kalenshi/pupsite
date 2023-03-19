"""
Utilities for the pups routes
"""

import secrets
import os
from PIL import Image
from flask import current_app

PICTURE_WIDTH = 200
PICTURE_HEIGHT = 200


def save_picture(form_picture):
    """
    Gives a picture location a random hex filename and saves it in the database

    Args:
        form_picture(str) : The representation of the picture

    Returns:
        str : the location of the photo to be added to the database
    """
    thumbnail_size = (PICTURE_WIDTH, PICTURE_HEIGHT)
    _, ext = os.path.splitext(form_picture.filename)
    filename = f"{secrets.token_hex(8)}{ext.lower()}"
    thumbnail_path = os.path.join(current_app.root_path, "static", "images", filename)
    try:
        image = Image.open(form_picture)
        image.thumbnail(size=thumbnail_size)
        image.save(thumbnail_path)
    except FileNotFoundError:
        filename = "default.png"

    return filename
