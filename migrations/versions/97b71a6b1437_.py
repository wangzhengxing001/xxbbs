"""empty message

Revision ID: 97b71a6b1437
Revises: 8a0762103782
Create Date: 2018-03-28 22:46:11.853534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97b71a6b1437'
down_revision = '8a0762103782'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('join_time', sa.DateTime(), nullable=False))
    op.drop_index('email', table_name='cms_user')
    op.drop_column('cms_user', 'create_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('create_time', mysql.DATETIME(), nullable=False))
    op.create_index('email', 'cms_user', ['email'], unique=True)
    op.drop_column('cms_user', 'join_time')
    # ### end Alembic commands ###