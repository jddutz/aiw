"""Initial Setup

Revision ID: e403a1d4fa82
Revises: 
Create Date: 2023-10-25 14:51:41.309288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e403a1d4fa82"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=50), nullable=True),
        sa.Column("username_normalized", sa.String(length=50), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("email_normalized", sa.String(length=255), nullable=True),
        sa.Column("pw_hash", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("modified_at", sa.DateTime(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_email_verified", sa.Boolean(), nullable=True),
        sa.Column("last_login", sa.DateTime(), nullable=True),
        sa.Column("failed_login_count", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_users_email"), ["email"], unique=True)
        batch_op.create_index(
            batch_op.f("ix_users_email_normalized"), ["email_normalized"], unique=False
        )
        batch_op.create_index(
            batch_op.f("ix_users_username"), ["username"], unique=True
        )
        batch_op.create_index(
            batch_op.f("ix_users_username_normalized"),
            ["username_normalized"],
            unique=False,
        )


def downgrade():
    op.drop_table("users")
