"""empty message

Revision ID: b1c05324cc13
Revises: cce1284874fa
Create Date: 2020-07-26 16:08:39.066127

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import db


# revision identifiers, used by Alembic.
revision = 'b1c05324cc13'
down_revision = 'cce1284874fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'adminunit', ['short_name'])
    op.create_unique_constraint(None, 'organization', ['short_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'organization', type_='unique')
    op.drop_constraint(None, 'adminunit', type_='unique')
    # ### end Alembic commands ###
