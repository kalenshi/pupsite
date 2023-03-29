import pytest

from pupsite import create_site, db as _db
from pupsite.config.config_for_testing import TestConfig


@pytest.fixture
def app():
    """
    Create the app for testing purposes
    Anything that is set before the yield statement serves as `setup`
    and anything after the yield will serve as the `teardown` for the application

    Returns:
        Flask : flask app

    """
    _app = create_site(config_class=TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="function")
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
