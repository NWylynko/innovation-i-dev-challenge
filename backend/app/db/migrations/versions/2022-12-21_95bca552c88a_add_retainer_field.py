"""Add retainer field

Revision ID: 95bca552c88a
Revises: 2a8d5e94753e
Create Date: 2022-12-21 12:20:57.535200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95bca552c88a'
down_revision = '2a8d5e94753e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Organisation', sa.Column('retainer', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Organisation', 'retainer')
    # ### end Alembic commands ###
