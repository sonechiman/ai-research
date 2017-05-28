"""Add followers to al

Revision ID: f533f61df92c
Revises: 2c6cfd682fb6
Create Date: 2017-05-28 19:54:33.341205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f533f61df92c'
down_revision = '2c6cfd682fb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('angellist_companies', sa.Column('followers', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('angellist_companies', 'followers')
    # ### end Alembic commands ###