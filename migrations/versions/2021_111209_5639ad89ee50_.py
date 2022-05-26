"""empty message

Revision ID: 5639ad89ee50
Revises: 1076b5795b08
Create Date: 2021-11-12 09:40:58.618886

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5639ad89ee50'
down_revision = '1076b5795b08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('include_website_in_one_click_alias', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'include_website_in_one_click_alias')
    # ### end Alembic commands ###
