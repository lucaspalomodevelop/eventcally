"""empty message

Revision ID: ddb85cb1c21e
Revises: b1a6e7630185
Create Date: 2021-02-02 15:17:21.988363

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import dbtypes


# revision identifiers, used by Alembic.
revision = "ddb85cb1c21e"
down_revision = "b1a6e7630185"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "oauth2_client",
        sa.Column("client_id", sa.String(length=48), nullable=True),
        sa.Column("client_secret", sa.String(length=120), nullable=True),
        sa.Column("client_id_issued_at", sa.Integer(), nullable=False),
        sa.Column("client_secret_expires_at", sa.Integer(), nullable=False),
        sa.Column("client_metadata", sa.Text(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_oauth2_client_client_id"), "oauth2_client", ["client_id"], unique=False
    )
    op.create_table(
        "oauth2_code",
        sa.Column("code", sa.String(length=120), nullable=False),
        sa.Column("client_id", sa.String(length=48), nullable=True),
        sa.Column("redirect_uri", sa.Text(), nullable=True),
        sa.Column("response_type", sa.Text(), nullable=True),
        sa.Column("scope", sa.Text(), nullable=True),
        sa.Column("nonce", sa.Text(), nullable=True),
        sa.Column("auth_time", sa.Integer(), nullable=False),
        sa.Column("code_challenge", sa.Text(), nullable=True),
        sa.Column("code_challenge_method", sa.String(length=48), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "oauth2_token",
        sa.Column("client_id", sa.String(length=48), nullable=True),
        sa.Column("token_type", sa.String(length=40), nullable=True),
        sa.Column("access_token", sa.String(length=255), nullable=False),
        sa.Column("refresh_token", sa.String(length=255), nullable=True),
        sa.Column("scope", sa.Text(), nullable=True),
        sa.Column("revoked", sa.Boolean(), nullable=True),
        sa.Column("issued_at", sa.Integer(), nullable=False),
        sa.Column("expires_in", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("access_token"),
    )
    op.create_index(
        op.f("ix_oauth2_token_refresh_token"),
        "oauth2_token",
        ["refresh_token"],
        unique=False,
    )
    op.create_unique_constraint(
        "eventplace_name_admin_unit_id", "eventplace", ["name", "admin_unit_id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("eventplace_name_admin_unit_id", "eventplace", type_="unique")
    op.drop_index(op.f("ix_oauth2_token_refresh_token"), table_name="oauth2_token")
    op.drop_table("oauth2_token")
    op.drop_table("oauth2_code")
    op.drop_index(op.f("ix_oauth2_client_client_id"), table_name="oauth2_client")
    op.drop_table("oauth2_client")
    # ### end Alembic commands ###
