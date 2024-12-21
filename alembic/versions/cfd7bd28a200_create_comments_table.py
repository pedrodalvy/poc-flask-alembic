"""create_comments_table

Revision ID: cfd7bd28a200
Revises: 3a3ecd6b4d29
Create Date: 2024-12-21 10:50:09.421163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfd7bd28a200'
down_revision: Union[str, None] = '3a3ecd6b4d29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with open('alembic/sql/create_comments_table.sql', 'r') as f:
        sql = f.read()
    op.execute(sql)


def downgrade() -> None:
    op.drop_table('comments')
