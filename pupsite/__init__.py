from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

from pupsite.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "memberblueprint.login"
login_manager.login_message_category = "info"
bcrypt = Bcrypt()
mail = Mail()


def register_blueprints(app):
    """
    Registers the blueprints of the app
    Args:
        app(object) : The flask app to associate the blueprints with
    Returns:
        None
    """
    from pupsite.pups.routes import pupsblueprint
    from pupsite.public.routes import publicblueprint
    from pupsite.member.routes import memberblueprint
    app.register_blueprint(pupsblueprint)
    app.register_blueprint(publicblueprint)
    app.register_blueprint(memberblueprint)


def register_extensions(app):
    """
    Registers the extensions needed to run the application
     Args:
        app(Flask) : The flask app to associate the extensions with
    Returns:
        None
    """

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)


def create_site(config_class=Config):
    """
    Creates an instance of the flask application using the provided configuration class
    Args:
        config_class (class) : The configuration object to use for instantiation
    Returns:
        object : returns the flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # register extensions
    register_extensions(app)
    # Add routes through blueprints
    register_blueprints(app)
    return app
