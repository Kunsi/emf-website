"""Add index to FavouriteProposal

Revision ID: e9c68e8f78c2
Revises: e27e0646278c
Create Date: 2024-05-31 21:43:02.680838

"""

# revision identifiers, used by Alembic.
revision = 'e9c68e8f78c2'
down_revision = 'e27e0646278c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_favourite_proposal_proposal_id'), 'favourite_proposal', ['proposal_id'], unique=False)
    op.alter_column('feature_flag_version', 'enabled',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               autoincrement=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feature_flag_version', 'enabled',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               autoincrement=False)
    op.drop_index(op.f('ix_favourite_proposal_proposal_id'), table_name='favourite_proposal')
    # ### end Alembic commands ###