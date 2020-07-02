'''
Rename snapshot columns

Revision ID: 4a020f1d271a
Created at: 2016-08-16 09:25:38.350861
'''

import sqlalchemy as sa
from alembic import op


revision = '4a020f1d271a'
down_revision = '840b460c5613'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('snapshot') as batch_op:
        batch_op.add_column(
            sa.Column('resource_name', sa.Unicode(length=64), nullable=False))
        batch_op.add_column(
            sa.Column('resource_pkey', sa.Integer(), nullable=False))
        batch_op.create_index(
            op.f('ix_snapshot_resource_pkey'),
            ['resource_pkey'],
            unique=False)
        batch_op.drop_index('ix_snapshot_resource_id')
        batch_op.drop_column('resource_id')
        batch_op.drop_column('resource_repr')


def downgrade():
    op.add_column(
        'snapshot',
        sa.Column(
            'resource_repr',
            sa.VARCHAR(length=64),
            autoincrement=False,
            nullable=False))
    op.add_column(
        'snapshot',
        sa.Column(
            'resource_id',
            sa.INTEGER(),
            autoincrement=False,
            nullable=False))
    op.create_index(
        'ix_snapshot_resource_id', 'snapshot', ['resource_id'], unique=False)
    op.drop_index(op.f('ix_snapshot_resource_pkey'), table_name='snapshot')
    op.drop_column('snapshot', 'resource_pkey')
    op.drop_column('snapshot', 'resource_name')
