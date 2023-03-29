import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class TestConfig:
    TESTING = True
    SECRET_KEY = "3e3610cedcedead3c80213222c687b59"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
