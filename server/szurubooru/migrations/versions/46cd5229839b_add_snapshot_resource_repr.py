'''
Add snapshot resource_repr column

Revision ID: 46cd5229839b
Created at: 2016-04-21 19:00:48.087069
'''

import sqlalchemy as sa
from alembic import op

revision = '46cd5229839b'
down_revision = '565e01e3cf6d'
branch_labels = None
depends_on = None


def upgrade():
    # sqlite3 complains the column is NOT NULL with a default value of NULL despite there being no rows, recreate='always' fixes it
    with op.batch_alter_table('snapshot', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('resource_repr', sa.Unicode(length=64), nullable=False))


def downgrade():
    op.drop_column('snapshot', 'resource_repr')
