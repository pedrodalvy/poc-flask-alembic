"""create_posts_table

Revision ID: 3a3ecd6b4d29
Revises: 43816134b9e8
Create Date: 2024-12-21 10:45:05.600223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a3ecd6b4d29'
down_revision: Union[str, None] = '43816134b9e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.BigInteger(), nullable=False, autoincrement=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.func.current_timestamp()),
        sa.Column("created_by", sa.BigInteger(), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['created_by'], ['users.id'], ondelete='CASCADE')
    )


def downgrade() -> None:
    op.drop_table('posts')
