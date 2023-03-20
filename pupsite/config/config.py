import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "3e3610cedcedead3c80213222c687b59")
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"  # {os.path.join(BASE_DIR, 'pupsite.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
