"""revamp: favorites, order pricing breakdown, dish nutrition, business delivery info

Revision ID: b7e1c2d4a9f0
Revises: ffdc0a98111c
Create Date: 2026-09-28 12:00:00

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

revision = 'b7e1c2d4a9f0'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def _schema():
    return SCHEMA if environment == "production" else None


def _fk(table):
    return f"{SCHEMA}.{table}" if environment == "production" else table


def upgrade():
    schema = _schema()

    with op.batch_alter_table('business', schema=schema) as batch:
        batch.add_column(sa.Column('delivery_fee', sa.Float, nullable=False, server_default='2.99'))
        batch.add_column(sa.Column('prep_time', sa.Integer, nullable=False, server_default='25'))

    with op.batch_alter_table('dishes', schema=schema) as batch:
        batch.add_column(sa.Column('calories', sa.Integer, nullable=True))
        batch.add_column(sa.Column('is_available', sa.Boolean, nullable=False, server_default=sa.true()))

    with op.batch_alter_table('orders', schema=schema) as batch:
        batch.add_column(sa.Column('business_id', sa.Integer, nullable=True))
        batch.add_column(sa.Column('subtotal', sa.Float, nullable=True))
        batch.add_column(sa.Column('delivery_fee', sa.Float, nullable=True))
        batch.add_column(sa.Column('tax', sa.Float, nullable=True))
        batch.add_column(sa.Column('tip', sa.Float, nullable=True))
        batch.add_column(sa.Column('discount', sa.Float, nullable=True))
        batch.add_column(sa.Column('promo_code', sa.String(length=40), nullable=True))
        batch.add_column(sa.Column('notes', sa.String(length=300), nullable=True))
        batch.create_foreign_key('fk_orders_business_id', 'business', ['business_id'], ['id'],
                                 referent_schema=schema)

    op.create_table(
        'favorites',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey(_fk('users.id')), nullable=False),
        sa.Column('business_id', sa.Integer, sa.ForeignKey(_fk('business.id')), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.UniqueConstraint('user_id', 'business_id', name='uq_favorite_user_business'),
        schema=schema,
    )


def downgrade():
    schema = _schema()
    op.drop_table('favorites', schema=schema)

    with op.batch_alter_table('orders', schema=schema) as batch:
        batch.drop_constraint('fk_orders_business_id', type_='foreignkey')
        for col in ('notes', 'promo_code', 'discount', 'tip', 'tax', 'delivery_fee', 'subtotal', 'business_id'):
            batch.drop_column(col)

    with op.batch_alter_table('dishes', schema=schema) as batch:
        batch.drop_column('is_available')
        batch.drop_column('calories')

    with op.batch_alter_table('business', schema=schema) as batch:
        batch.drop_column('prep_time')
        batch.drop_column('delivery_fee')
