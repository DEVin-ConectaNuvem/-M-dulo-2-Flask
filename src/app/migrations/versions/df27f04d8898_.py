"""empty message

Revision ID: df27f04d8898
Revises: f62180f8c121
Create Date: 2022-08-04 19:42:34.873951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df27f04d8898'
down_revision = 'f62180f8c121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.Column('language', sa.String(length=84), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('technologies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('states',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.Column('initials', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['countries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=84), nullable=False),
    sa.Column('password', sa.String(length=84), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('developers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('months_experience', sa.Integer(), nullable=True),
    sa.Column('accepted_remote_work', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('developer_technologies',
    sa.Column('developer_id', sa.Integer(), nullable=True),
    sa.Column('technology_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['developer_id'], ['developers.id'], ),
    sa.ForeignKeyConstraint(['technology_id'], ['technologies.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('developer_technologies')
    op.drop_table('developers')
    op.drop_table('users')
    op.drop_table('cities')
    op.drop_table('states')
    op.drop_table('technologies')
    op.drop_table('countries')
    # ### end Alembic commands ###
