"""Add logo

Revision ID: fd6dbf0f4177
Revises: f533f61df92c
Create Date: 2017-05-28 22:52:56.173104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6dbf0f4177'
down_revision = 'f533f61df92c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('angellist_companies', sa.Column('logo', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('angellist_companies', 'logo')
    # ### end Alembic commands ###
