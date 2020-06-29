'''
Fix ForeignKey constraint definitions

Revision ID: 840b460c5613
Created at: 2016-08-15 18:39:30.909867
'''

import sqlalchemy as sa
from alembic import op


revision = '840b460c5613'
down_revision = '7f6baf38c27c'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('post') as batch_op:
        batch_op.drop_constraint('post_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'post_user_id_fkey', 'user', ['user_id'], ['id'], ondelete='SET NULL')
    with op.batch_alter_table('snapshot') as batch_op:
        batch_op.drop_constraint('snapshot_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            'snapshot_user_id_fkey', 'user', ['user_id'], ['id'], ondelete='set null')


def downgrade():
    op.drop_constraint(None, 'snapshot', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key(
        'snapshot_user_id_fkey', 'snapshot', 'user', ['user_id'], ['id'])
    op.create_foreign_key(
        'post_user_id_fkey', 'post', 'user', ['user_id'], ['id'])
