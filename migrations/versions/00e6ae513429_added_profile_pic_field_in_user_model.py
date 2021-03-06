"""added profile_pic field in user model

Revision ID: 00e6ae513429
Revises: 2fd5dbf3d7f3
Create Date: 2020-02-24 15:56:56.713724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e6ae513429'
down_revision = '2fd5dbf3d7f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_pic', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_pic')
    # ### end Alembic commands ###
