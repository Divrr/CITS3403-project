"""removed updated_at from Activity

Revision ID: 3f873e979b8f
Revises: bf1b778528fa
Create Date: 2024-05-16 12:13:51.516637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f873e979b8f'
down_revision = 'bf1b778528fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.drop_index('ix_activity_updated_at')
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=False))
        batch_op.create_index('ix_activity_updated_at', ['updated_at'], unique=False)

    # ### end Alembic commands ###