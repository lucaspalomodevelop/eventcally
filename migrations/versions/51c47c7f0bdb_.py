"""empty message

Revision ID: 51c47c7f0bdb
Revises: 7afc40e11791
Create Date: 2020-09-29 15:38:44.033998

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "51c47c7f0bdb"
down_revision = "7afc40e11791"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "featuredevent", sa.Column("admin_unit_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(None, "featuredevent", "adminunit", ["admin_unit_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "featuredevent", type_="foreignkey")
    op.drop_column("featuredevent", "admin_unit_id")
    # ### end Alembic commands ###
