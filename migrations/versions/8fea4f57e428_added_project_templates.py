"""Added project templates

Revision ID: 8fea4f57e428
Revises: aaf23a3614b7
Create Date: 2023-10-16 13:28:35.998823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fea4f57e428'
down_revision = 'aaf23a3614b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('imageref', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('genre', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_genre_name'), ['name'], unique=True)

    op.create_table('project_template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('methodology', sa.Text(), nullable=False),
    sa.Column('length', sa.String(length=255), nullable=False),
    sa.Column('links', sa.Text(), nullable=False),
    sa.Column('structure', sa.Text(), nullable=True),
    sa.Column('imageref', sa.String(length=255), nullable=True),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('modified', sa.TIMESTAMP(), nullable=True),
    sa.Column('usage_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tag_name'), ['name'], unique=True)

    op.create_table('project_template_genres',
    sa.Column('project_template_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['project_template_id'], ['project_template.id'], ),
    sa.PrimaryKeyConstraint('project_template_id', 'genre_id')
    )
    op.create_table('project_template_tags',
    sa.Column('project_template_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_template_id'], ['project_template.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('project_template_id', 'tag_id')
    )
    with op.batch_alter_table('story_part', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imageref', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('story_part', schema=None) as batch_op:
        batch_op.drop_column('imageref')

    op.drop_table('project_template_tags')
    op.drop_table('project_template_genres')
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tag_name'))

    op.drop_table('tag')
    op.drop_table('project_template')
    with op.batch_alter_table('genre', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_genre_name'))

    op.drop_table('genre')
    # ### end Alembic commands ###