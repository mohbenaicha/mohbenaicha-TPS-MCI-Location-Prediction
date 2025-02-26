"""create LR IO model

Revision ID: 0b4a0b609c0d
Revises: 
Create Date: 2022-07-31 16:16:20.445422

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0b4a0b609c0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('linear_regression_io',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.Column('datetime_captured', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('model_version', sa.String(length=36), nullable=False),
    sa.Column('inputs', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('outputs', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_linear_regression_io_datetime_captured'), 'linear_regression_io', ['datetime_captured'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_linear_regression_io_datetime_captured'), table_name='linear_regression_io')
    op.drop_table('linear_regression_io')
    # ### end Alembic commands ###
