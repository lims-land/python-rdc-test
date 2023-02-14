"""empty message

Revision ID: 3858deac53f0
Revises: c85a206cd0a8
Create Date: 2023-02-14 16:18:36.529982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3858deac53f0'
down_revision = 'c85a206cd0a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###