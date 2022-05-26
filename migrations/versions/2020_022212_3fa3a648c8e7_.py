"""empty message

Revision ID: 3fa3a648c8e7
Revises: 3c9542fc54e9
Create Date: 2020-02-22 12:53:31.293693

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fa3a648c8e7'
down_revision = '3c9542fc54e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forward_email_log', sa.Column('bounced', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forward_email_log', 'bounced')
    # ### end Alembic commands ###
