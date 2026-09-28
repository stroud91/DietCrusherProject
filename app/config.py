import os
from datetime import timedelta

IS_PRODUCTION = os.environ.get('FLASK_ENV') == 'production'


def _database_url():
    url = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')
    # Render and Heroku hand out "postgres://" URLs, which SQLAlchemy no
    # longer accepts. Normalise to the "postgresql://" dialect name.
    if url.startswith('postgres://'):
        url = url.replace('postgres://', 'postgresql://', 1)
    return url


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        if IS_PRODUCTION:
            raise RuntimeError('SECRET_KEY must be set in production.')
        SECRET_KEY = 'dev-only-insecure-key'

    SQLALCHEMY_DATABASE_URI = _database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO') == '1'
    # Render's managed Postgres drops idle connections; pre-ping avoids
    # "server closed the connection unexpectedly" after quiet periods.
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping': True, 'pool_recycle': 280}

    # Session / remember-me cookies
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = IS_PRODUCTION
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_SECURE = IS_PRODUCTION
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # CSRF: validated globally from the X-CSRFToken header
    WTF_CSRF_TIME_LIMIT = None
    WTF_CSRF_SSL_STRICT = False

    # Reject oversized request bodies (JSON API only, no uploads)
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    RATELIMIT_STORAGE_URI = os.environ.get('RATELIMIT_STORAGE_URI', 'memory://')
    RATELIMIT_HEADERS_ENABLED = True
