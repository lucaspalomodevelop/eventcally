"""empty message

Revision ID: b128cc637447
Revises: 41512b20e07c
Create Date: 2020-07-26 15:20:17.685921

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import dbtypes


# revision identifiers, used by Alembic.
revision = 'b128cc637447'
down_revision = '41512b20e07c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adminunit', sa.Column('fax', sa.Unicode(length=255), nullable=True))
    op.add_column('eventorganizer', sa.Column('fax', sa.Unicode(length=255), nullable=True))
    op.add_column('organization', sa.Column('fax', sa.Unicode(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organization', 'fax')
    op.drop_column('eventorganizer', 'fax')
    op.drop_column('adminunit', 'fax')
    # ### end Alembic commands ###
