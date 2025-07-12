"""create todos table

Revision ID: b8abbba9e6d8
Revises: 
Create Date: 2025-06-24 08:21:47.291251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8abbba9e6d8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)


def downgrade():
    """Downgrade schema."""
    op.execute("drop table todos;")
