"""Setup writing projects

Revision ID: 4fc244d5ab24
Revises: 403319cac373
Create Date: 2023-10-26 06:38:51.168085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4fc244d5ab24"
down_revision = "403319cac373"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "genres",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("imageref", sa.String(length=255), nullable=True),
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
    with op.batch_alter_table("genres", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_genres_name"), ["name"], unique=True)
    conn.execute(
        "ALTER TABLE genres ADD FULLTEXT fulltext_genre_index (name,description)"
    )
    conn.execute("ALTER TABLE genres ADD FULLTEXT (name)")

    op.create_table(
        "project_templates",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("category", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("methodology", sa.Text(), nullable=False),
        sa.Column("length", sa.String(length=255), nullable=False),
        sa.Column("tags", sa.Text(), nullable=True),
        sa.Column("links", sa.Text(), nullable=False),
        sa.Column("structure", sa.Text(), nullable=True),
        sa.Column("imageref", sa.String(length=255), nullable=True),
        sa.Column("usage_count", sa.Integer(), nullable=True),
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
        sa.UniqueConstraint("title"),
    )
    conn.execute(
        "ALTER TABLE project_templates ADD FULLTEXT fulltext_index (title,description,methodology,tags)"
    )
    conn.execute("ALTER TABLE project_templates ADD FULLTEXT (title)")
    op.create_table(
        "project_template_genres",
        sa.Column("project_template_id", sa.Integer(), nullable=True),
        sa.Column("genre_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genres.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_template_id"],
            ["project_templates.id"],
        ),
    )
    op.create_table(
        "writing_projects",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("visibility", sa.String(length=120), nullable=False),
        sa.Column("project_template_id", sa.Integer(), nullable=True),
        sa.Column("project_type", sa.String(length=120), nullable=False),
        sa.Column("tags", sa.Text(), nullable=False),
        sa.Column("genre_id", sa.Integer(), nullable=True),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("modified", sa.TIMESTAMP(), nullable=True),
        sa.Column("modified_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genres.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_template_id"],
            ["project_templates.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("writing_projects", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_writing_projects_title"), ["title"], unique=False
        )

    op.create_table(
        "collaborators_link",
        sa.Column("writing_project_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["writing_project_id"],
            ["writing_projects.id"],
        ),
        sa.PrimaryKeyConstraint("writing_project_id", "user_id"),
    )
    op.create_table(
        "reviewers_link",
        sa.Column("writing_project_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["writing_project_id"],
            ["writing_projects.id"],
        ),
        sa.PrimaryKeyConstraint("writing_project_id", "user_id"),
    )
    op.create_table(
        "story_parts",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("writing_project_id", sa.Integer(), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column(
            "part_type",
            sa.Enum("TEXT", "COLLECTION", "IMAGE", "IMAGEREF", name="storyparttype"),
            nullable=False,
        ),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("content", sa.Text(), nullable=True),
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
            ["parent_id"],
            ["story_parts.id"],
        ),
        sa.ForeignKeyConstraint(
            ["writing_project_id"],
            ["writing_projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE genres DROP INDEX fulltext_genre_index")
    conn.execute("ALTER TABLE genres DROP INDEX name")
    conn.execute("ALTER TABLE writing_projects DROP INDEX fulltext_index")
    conn.execute("ALTER TABLE writing_projects DROP INDEX title")
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("story_parts")
    op.drop_table("reviewers_link")
    op.drop_table("collaborators_link")
    with op.batch_alter_table("writing_projects", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_writing_projects_title"))

    op.drop_table("writing_projects")
    op.drop_table("project_template_genres")
    op.drop_table("project_templates")
    with op.batch_alter_table("genres", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_genres_name"))

    op.drop_table("genres")
    # ### end Alembic commands ###
