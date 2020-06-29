'''
Add order to tag names

Revision ID: 9837fc981ec7
Created at: 2016-08-28 19:03:59.831527
'''

import sqlalchemy as sa
from alembic import op
import sqlalchemy.ext.declarative


revision = '9837fc981ec7'
down_revision = '4a020f1d271a'
branch_labels = None
depends_on = None


Base = sa.ext.declarative.declarative_base()


class TagName(Base):
    __tablename__ = 'tag_name'
    __table_args__ = {'extend_existing': True}

    tag_name_id = sa.Column('tag_name_id', sa.Integer, primary_key=True)
    ord = sa.Column('ord', sa.Integer, nullable=False, index=True)


def upgrade():
    with op.batch_alter_table('tag_name') as batch_op:
        batch_op.add_column(sa.Column('ord', sa.Integer(), nullable=True))
    op.execute(TagName.__table__.update().values(ord=TagName.tag_name_id))
    with op.batch_alter_table('tag_name', recreate='always') as batch_op:
        batch_op.alter_column('ord', nullable=False)
        batch_op.create_index(
            batch_op.f('ix_tag_name_ord'), ['ord'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_tag_name_ord'), table_name='tag_name')
    op.drop_column('tag_name', 'ord')
