"""empty message

Revision ID: 7bb3720c1969
Revises: 97b71a6b1437
Create Date: 2018-03-28 22:49:42.196274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bb3720c1969'
down_revision = '97b71a6b1437'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('signature', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cms_user', 'signature')
    # ### end Alembic commands ###
