'''
Add default column to tag categories

Revision ID: 055d0e048fb3
Created at: 2016-05-22 18:12:58.149678
'''

import sqlalchemy as sa
from alembic import op

revision = '055d0e048fb3'
down_revision = '49ab4e1139ef'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('tag_category') as batch_op:
        batch_op.add_column(
            sa.Column('default', sa.Boolean(), nullable=True))
    op.execute(
        sa.table('tag_category', sa.column('default'))
        .update()
        .values(default=False))
    with op.batch_alter_table('tag_category', recreate='always') as batch_op:
        batch_op.alter_column('default', nullable=False)


def downgrade():
    op.drop_column('tag_category', 'default')
