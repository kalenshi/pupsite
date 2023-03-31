"""
This module will test the routing and logic of adding a pup
"""
from pupsite.models import Pup
#from pupsite import db


def test_adding_pup(app,db):
    """
    Given a flask application configured for testing
    When a logged in member requests to create a pup
    Then we must check that the database is populated with the new pup
    and the member is redirected to the pup oage
    Args:
        client: the test client to simulate request/response
        app: the database for persisting pup data

    Returns:

    """
    pup_data = {
        "name": "Marmaduke",
        "breed": "Siberian Huskey",
        "age": 2,
        "details": "This is a test Puppy",
        "owner_id": 1
    }
    response = app.post("/pup/add", data=pup_data)

    assert response.status_code == 302

    with app.app_context():
        pup = db.session.get(Pup, 1)
        assert pup.name == pup_data["name"]
