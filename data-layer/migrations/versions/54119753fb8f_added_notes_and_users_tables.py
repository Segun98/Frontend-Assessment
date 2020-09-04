"""Added notes and users tables

Revision ID: 54119753fb8f
Revises: 0514e3418c6b
Create Date: 2020-09-02 21:46:37.429483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54119753fb8f'
down_revision = '0514e3418c6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('notes', sa.Column('authorId', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'authorId')
    op.drop_table('users')
    # ### end Alembic commands ###