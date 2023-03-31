from pupsite.models import Member
from pupsite import db

from tests.factories.member import MemberFactory


def test_can_create_a_members(app,db):
    """
    Tests that you can create  members and save them the database
    """

    # assert member.email == "kalenshi@gmail.com"
    # assert member.password == "verystrongpassword"
    with app.app_context():
        member = Member(
            first_name="Kalenshi",
            last_name="Katebe",
            email="kalenshi@gmail.com",
            password="verystrongpassword"
        )
        db.session.add(member)
        db.session.commit()
        m = db.session.get(Member)
        assert m.password == "verystrongpassword"

# def test_can_update_a_member(app, db):
#     """
#     Test that you can add a member and update some details about them
#     Args:
#         app: The database instance to use
#
#     """
#     with app.app_context():
#         member = MemberFactory()
#
#         _ = member.first_name
#         member.first_name = "Kalenshi"
#
#         from_db = db.session.get(Member, 1)
#
#         assert from_db.first_name == "Kalenshi"
