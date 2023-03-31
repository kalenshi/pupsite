import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class TestConfig:
    TESTING = True
    SECRET_KEY = "testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
