import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class TestConfig:
    SECRET_KEY = "3e3610cedcedead3c80213222c687b59"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
