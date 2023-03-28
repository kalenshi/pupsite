import pytest

from pupsite import create_site, db
from pupsite.config.config_for_testing import TestConfig


@pytest.fixture()
def app():
    """
    Create the app for testing purposes
    Anything that is set before the yield statement serves as `setup`
    and anything after the yield will serve as the `teardown` for the application

    Returns:
        Flask : flask app

    """
    app = create_site(config_class=TestConfig)

    with app.app_context():
        db.create_all()
    yield app
    db.session.close()
    db.drop_all()
