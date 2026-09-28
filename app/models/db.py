import os
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

db = SQLAlchemy()


def add_prefix_for_prod(attr):
    """Prefix foreign key targets with the Postgres schema in production."""
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    return attr


def schema_args(*constraints):
    """__table_args__ helper that keeps the production schema while allowing constraints."""
    if environment == "production":
        return (*constraints, {'schema': SCHEMA})
    return constraints if constraints else {}


def utcnow():
    """Naive UTC timestamp (columns are timezone-less)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def iso(value):
    """Serialise a naive UTC datetime so browsers parse it as UTC."""
    return value.isoformat() + 'Z' if value else None
