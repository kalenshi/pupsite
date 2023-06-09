"""empty message

Revision ID: 34474b0ab9f8
Revises: e25c61daeaeb
Create Date: 2023-03-19 23:53:37.099496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34474b0ab9f8'
down_revision = 'e25c61daeaeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('pup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('breed', sa.String(length=20), nullable=False),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('picture', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pup')
    op.drop_table('member')
    # ### end Alembic commands ###
