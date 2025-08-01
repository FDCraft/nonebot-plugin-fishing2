"""add achievements

迁移 ID: c5ab992c9af3
父迁移: e9015df43907
创建时间: 2024-09-22 16:44:24.934270

"""
from __future__ import annotations

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = 'c5ab992c9af3'
down_revision: str | Sequence[str] | None = 'e9015df43907'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nonebot_plugin_fishing_fishingrecord', schema=None) as batch_op:
        batch_op.add_column(sa.Column('achievements', sa.TEXT(), nullable=False))

    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nonebot_plugin_fishing_fishingrecord', schema=None) as batch_op:
        batch_op.drop_column('achievements')

    # ### end Alembic commands ###