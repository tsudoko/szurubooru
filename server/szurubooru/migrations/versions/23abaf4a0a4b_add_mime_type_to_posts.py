'''
Add mime type to posts

Revision ID: 23abaf4a0a4b
Created at: 2016-05-02 00:02:33.024885
'''

import sqlalchemy as sa
from alembic import op

revision = '23abaf4a0a4b'
down_revision = 'ed6dd16a30f3'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('post', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('mime-type', sa.Unicode(length=32), nullable=False))


def downgrade():
    op.drop_column('post', 'mime-type')
