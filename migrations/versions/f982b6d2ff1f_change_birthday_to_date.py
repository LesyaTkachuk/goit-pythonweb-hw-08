"""Change birthday to date

Revision ID: f982b6d2ff1f
Revises: e56af5c0733d
Create Date: 2024-12-01 21:12:17.850333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f982b6d2ff1f'
down_revision: Union[str, None] = 'e56af5c0733d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
