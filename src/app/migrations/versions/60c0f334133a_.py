"""empty message

Revision ID: 60c0f334133a
Revises: ebbcf23889ff
Create Date: 2022-08-03 19:40:55.424547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c0f334133a'
down_revision = 'ebbcf23889ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('developers', 'months_experience',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('developers', 'months_experience',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###