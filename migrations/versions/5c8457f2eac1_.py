"""empty message

Revision ID: 5c8457f2eac1
Revises: ed6bb2084bbd
Create Date: 2020-07-13 19:01:04.770613

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5c8457f2eac1"
down_revision = "ed6bb2084bbd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("event", sa.Column("end", sa.DateTime(timezone=True), nullable=True))
    op.add_column(
        "event", sa.Column("start", sa.DateTime(timezone=True), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("event", "start")
    op.drop_column("event", "end")
    # ### end Alembic commands ###
