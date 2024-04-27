"""re-designed to a user-activity rdb

Revision ID: fd44eee5a05b
Revises: c4b58b6046da
Create Date: 2024-04-25 17:34:19.574801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd44eee5a05b'
down_revision = 'c4b58b6046da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('acceptor_id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.Enum('Request', 'Offer'), nullable=False),
    sa.Column('status', sa.Enum('Open', 'Closed', 'Pending', 'Completed'), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['acceptor_id'], ['user._id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['user._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_activity_updated_at'), ['updated_at'], unique=False)

    with op.batch_alter_table('offer', schema=None) as batch_op:
        batch_op.drop_index('ix_offer_created_at')
        batch_op.drop_index('ix_offer_request_id')
        batch_op.drop_index('ix_offer_updated_at')
        batch_op.drop_index('ix_offer_user_id')

    op.drop_table('offer')
    with op.batch_alter_table('request', schema=None) as batch_op:
        batch_op.drop_index('ix_request_created_at')
        batch_op.drop_index('ix_request_updated_at')
        batch_op.drop_index('ix_request_user_id')

    op.drop_table('request')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_id', sa.Integer(), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=128),
               existing_nullable=False)
        batch_op.drop_index('ix_user_created_at')
        batch_op.drop_index('ix_user_updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), nullable=False))
        batch_op.create_index('ix_user_updated_at', ['updated_at'], unique=False)
        batch_op.create_index('ix_user_created_at', ['created_at'], unique=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('_id')

    op.create_table('request',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), nullable=False),
    sa.Column('description', sa.VARCHAR(length=256), nullable=False),
    sa.Column('status', sa.VARCHAR(length=9), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('request', schema=None) as batch_op:
        batch_op.create_index('ix_request_user_id', ['user_id'], unique=False)
        batch_op.create_index('ix_request_updated_at', ['updated_at'], unique=False)
        batch_op.create_index('ix_request_created_at', ['created_at'], unique=False)

    op.create_table('offer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('request_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('description', sa.VARCHAR(length=256), nullable=False),
    sa.Column('status', sa.VARCHAR(length=9), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['request_id'], ['request.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('offer', schema=None) as batch_op:
        batch_op.create_index('ix_offer_user_id', ['user_id'], unique=False)
        batch_op.create_index('ix_offer_updated_at', ['updated_at'], unique=False)
        batch_op.create_index('ix_offer_request_id', ['request_id'], unique=False)
        batch_op.create_index('ix_offer_created_at', ['created_at'], unique=False)

    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_activity_updated_at'))

    op.drop_table('activity')
    # ### end Alembic commands ###