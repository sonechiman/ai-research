"""Add image

Revision ID: 2c6cfd682fb6
Revises: 10407acae105
Create Date: 2017-05-28 19:16:11.907569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2c6cfd682fb6'
down_revision = '10407acae105'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('angellist_id', sa.Integer(), nullable=True),
    sa.Column('crunchbase_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['angellist_id'], ['angellist_companies.id'], ),
    sa.ForeignKeyConstraint(['crunchbase_id'], ['crunchbase_companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_url'), 'images', ['url'], unique=False)
    op.add_column('angellist_companies', sa.Column('employees', sa.String(length=128), nullable=True))
    op.drop_column('angellist_companies', 'employers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('angellist_companies', sa.Column('employers', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('angellist_companies', 'employees')
    op.drop_index(op.f('ix_images_url'), table_name='images')
    op.drop_table('images')
    # ### end Alembic commands ###
