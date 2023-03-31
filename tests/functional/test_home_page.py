"""
This module tests the home page functionality
"""


def test_home_page_routes_correctly(app):
    """
    Given a flask app configured for testing
    When the "/" route is requested (GET)
    Then check that the response is valid
    Args:
        client: test client used to simulate request/response

    Returns:

    """
    response = app.get("/")

    assert response.status_code == 200
    assert b"<h1>Welcome to our Pup Adoption Page</h1>" in response.data
