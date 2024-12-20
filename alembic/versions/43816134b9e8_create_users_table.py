"""create_users_table

Revision ID: 43816134b9e8
Revises: 
Create Date: 2024-12-19 23:22:08.364422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43816134b9e8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger(), nullable=False, autoincrement=True),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.func.current_timestamp()),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table('users')
