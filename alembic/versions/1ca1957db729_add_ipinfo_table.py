"""Add IpInfo table

Revision ID: 1ca1957db729
Revises: 
Create Date: 2023-04-26 19:55:16.421047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca1957db729'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ip_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('ip_type_enum', sa.Enum('SOME_TYPE', name='ip_type', create_constraint=True), nullable=False),
    sa.Column('continent_code', sa.String(), nullable=False),
    sa.Column('continent_name', sa.String(), nullable=False),
    sa.Column('country_code', sa.String(), nullable=False),
    sa.Column('country_name', sa.String(), nullable=False),
    sa.Column('region_code', sa.String(), nullable=False),
    sa.Column('region_name', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('zip', sa.String(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('country_flag', sa.String(), nullable=False),
    sa.Column('country_flag_emoji', sa.String(), nullable=False),
    sa.Column('country_flag_emoji_unicode', sa.String(), nullable=False),
    sa.Column('calling_code', sa.Integer(), nullable=False),
    sa.Column('is_eu', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip')
    )
    op.create_index(op.f('ix_ip_info_id'), 'ip_info', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ip_info_id'), table_name='ip_info')
    op.drop_table('ip_info')
    # ### end Alembic commands ###
