"""create purchase table

Revision ID: 81e31e4dd801
Revises: 5e464ae04e59
Create Date: 2024-06-26 18:44:05.942146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81e31e4dd801'
down_revision: Union[str, None] = '5e464ae04e59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchases')
    # ### end Alembic commands ###