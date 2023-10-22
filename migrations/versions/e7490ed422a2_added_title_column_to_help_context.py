"""Added title column to help_context

Revision ID: e7490ed422a2
Revises: 7f7a478781fb
Create Date: 2023-10-22 15:34:51.497986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7490ed422a2'
down_revision = '7f7a478781fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('help_context', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=128), nullable=False))
        batch_op.create_index(batch_op.f('ix_help_context_title'), ['title'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('help_context', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_help_context_title'))
        batch_op.drop_column('title')

    # ### end Alembic commands ###