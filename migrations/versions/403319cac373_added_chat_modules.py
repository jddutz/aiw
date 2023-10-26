"""Added chat modules

Revision ID: 403319cac373
Revises: e403a1d4fa82
Create Date: 2023-10-25 14:57:39.776878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "403319cac373"
down_revision = "e403a1d4fa82"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "notifications",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("message", sa.String(length=500), nullable=False),
        sa.Column("notification_type", sa.String(length=120), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("modified_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_histories",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("modified_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_messages",
        sa.Column(
            "role",
            sa.Enum("USER", "ASSISTANT", "SYSTEM", name="roleenum"),
            nullable=True,
        ),
        sa.Column("content", sa.Text(), nullable=True),
        sa.Column("chat_history_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column(
            "visibility",
            sa.Enum(
                "VISIBLE_TO_ALL", "VISIBLE_TO_COLLABORATORS", name="visibilityenum"
            ),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("modified_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["chat_history_id"],
            ["chat_histories.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_system_messages",
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("message_type", sa.String(length=50), nullable=True),
        sa.Column("associated_module", sa.String(length=50), nullable=True),
        sa.Column("tags", sa.String(length=255), nullable=True),
        sa.Column("version", sa.String(length=50), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("modified_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "help_context",
        sa.Column("context_id", sa.String(length=128), nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("modified_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("help_context", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_help_context_context_id"), ["context_id"], unique=True
        )
        batch_op.create_index(
            batch_op.f("ix_help_context_title"), ["title"], unique=True
        )


def downgrade():
    op.drop_table("chat_histories")
    op.drop_table("chat_messages")
    op.drop_table("chat_system_messages")
    with op.batch_alter_table("help_context", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_help_context_title"))
        batch_op.drop_index(batch_op.f("ix_help_context_context_id"))
    op.drop_table("help_context")
    op.drop_table("notifications")
    op.drop_table("activities")
