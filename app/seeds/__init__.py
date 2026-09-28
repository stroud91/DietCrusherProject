from flask.cli import AppGroup
from sqlalchemy.sql import text
from .users import seed_users, undo_users
from .businesses import seed_businesses, undo_businesses
from .dishes import seed_dishes, undo_dishes
from .reviews import seed_reviews, undo_reviews
from .orders import seed_orders, undo_orders
from .order_details import seed_order_details, undo_order_details
from .categories import seed_categories, undo_categories
from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')


def undo_transient():
    """Clear tables that are not seeded but reference seeded rows."""
    for table in ('favorites', 'cart_items', 'carts'):
        if environment == 'production':
            db.session.execute(text(f"TRUNCATE table {SCHEMA}.{table} RESTART IDENTITY CASCADE;"))
        else:
            db.session.execute(text(f"DELETE FROM {table}"))
    db.session.commit()


def undo_all():
    # Children first so SQLite (no TRUNCATE ... CASCADE) respects foreign keys.
    undo_transient()
    undo_order_details()
    undo_reviews()
    undo_orders()
    undo_dishes()
    undo_categories()
    undo_businesses()
    undo_users()


@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Re-seeding on every deploy: wipe tables first so ids restart at 1.
        undo_all()

    seed_users()
    seed_businesses()
    seed_categories()
    seed_dishes()
    seed_orders()
    seed_order_details()
    seed_reviews()


@seed_commands.command('undo')
def undo():
    undo_all()
