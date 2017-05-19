"""change string length

Revision ID: 0d3c342948ea
Revises: 6ca9f5713ea7
Create Date: 2017-05-20 01:59:14.383135

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d3c342948ea'
down_revision = '6ca9f5713ea7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('role', mysql.VARCHAR(length=256), nullable=True))
    op.alter_column('companies', 'funding',
               existing_type=mysql.VARCHAR(length=32),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('companies', 'name',
               existing_type=mysql.VARCHAR(length=32),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('companies', 'place',
               existing_type=mysql.VARCHAR(length=32),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('companies', 'place',
               existing_type=mysql.VARCHAR(length=256),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('companies', 'name',
               existing_type=mysql.VARCHAR(length=128),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=False)
    op.alter_column('companies', 'funding',
               existing_type=mysql.VARCHAR(length=256),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=True)
    op.drop_column('companies', 'role')
    # ### end Alembic commands ###
