from pupsite.models import Member
from tests.factories.member import MemberFactory


def test_can_create_a_members(db):
    """
    Tests that you can create  members and save them the database
    """
    _ = MemberFactory.create_batch(4)
    members = db.session.execute(db.select(Member)).scalars().all()

    assert len(members) == 4


def test_can_update_a_member(db):
    """
    Test that you can add a member and update some details about them
    Args:
        db: The database instance to use

    """
    member = MemberFactory()

    _ = member.first_name
    member.first_name = "Kalenshi"

    from_db = db.session.execute(db.select(Member)).scalar()

    assert from_db.first_name == "Kalenshi"
