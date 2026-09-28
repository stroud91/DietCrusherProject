import os
from flask import Flask, request, redirect, jsonify
from flask_migrate import Migrate
from flask_wtf.csrf import generate_csrf, CSRFError
from werkzeug.exceptions import HTTPException
from werkzeug.middleware.proxy_fix import ProxyFix

from .config import Config, IS_PRODUCTION
from .extensions import csrf, login_manager, limiter
from .models import db, User
from .seeds import seed_commands
from .api.auth_routes import auth_routes
from .api.user_routes import user_routes
from .api.bussiness_routes import business_bp
from .api.dishes import dish_bp
from .api.reviews import review_routes
from .api.cart import cart_bp
from .api.user_order import order_bp
from .api.owner_order import owner_bp
from .api.favorites import favorites_bp
from .api.discover import discover_bp

app = Flask(__name__, static_folder='../react-app/build', static_url_path='/')
app.config.from_object(Config)

# Render terminates TLS at its proxy; trust exactly one hop so request.is_secure
# and request.remote_addr (used by the rate limiter) reflect the real client.
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

db.init_app(app)
Migrate(app, db)
csrf.init_app(app)
limiter.init_app(app)
login_manager.init_app(app)
app.cli.add_command(seed_commands)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(errors=['Please log in to continue.']), 401


app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(business_bp, url_prefix='/api/business')
app.register_blueprint(dish_bp, url_prefix='/api/menu')
app.register_blueprint(review_routes, url_prefix='/api/review')
app.register_blueprint(cart_bp, url_prefix='/api/cart')
app.register_blueprint(order_bp, url_prefix='/api/orders')
app.register_blueprint(owner_bp, url_prefix='/api/owner')
app.register_blueprint(favorites_bp, url_prefix='/api/favorites')
app.register_blueprint(discover_bp, url_prefix='/api')


@app.before_request
def https_redirect():
    if IS_PRODUCTION and not request.is_secure:
        return redirect(request.url.replace('http://', 'https://', 1), code=301)


CONTENT_SECURITY_POLICY = "; ".join([
    "default-src 'self'",
    "script-src 'self'",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' data: https://fonts.gstatic.com",
    "img-src 'self' data: blob: https:",
    "connect-src 'self'",
    "frame-ancestors 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "object-src 'none'",
])


@app.after_request
def secure_response(response):
    # Readable by the SPA (double-submit pattern): the client echoes it back
    # in the X-CSRFToken header, which CSRFProtect validates on every write.
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=IS_PRODUCTION,
        samesite='Strict' if IS_PRODUCTION else 'Lax',
        httponly=False,
    )
    headers = response.headers
    headers.setdefault('Content-Security-Policy', CONTENT_SECURITY_POLICY)
    headers.setdefault('X-Content-Type-Options', 'nosniff')
    headers.setdefault('X-Frame-Options', 'DENY')
    headers.setdefault('Referrer-Policy', 'strict-origin-when-cross-origin')
    headers.setdefault('Permissions-Policy', 'camera=(), microphone=(), geolocation=(self), payment=()')
    headers.setdefault('Cross-Origin-Opener-Policy', 'same-origin')
    if IS_PRODUCTION:
        headers.setdefault('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
    if request.path.startswith('/api/'):
        headers['Cache-Control'] = 'no-store'
    return response


if not IS_PRODUCTION:
    @app.route('/api/docs')
    def api_help():
        """Returns all API routes and their doc strings (development only)."""
        methods = {'GET', 'POST', 'PUT', 'PATCH', 'DELETE'}
        return {
            rule.rule: [sorted(m for m in rule.methods if m in methods),
                        app.view_functions[rule.endpoint].__doc__]
            for rule in app.url_map.iter_rules() if rule.endpoint != 'static'
        }


def _is_api():
    return request.path.startswith('/api/')


@app.route('/')
def react_root():
    return app.send_static_file('index.html')


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify(errors=['Your session expired. Please refresh and try again.']), 400


@app.errorhandler(404)
def not_found(e):
    if _is_api():
        return jsonify(errors=['Not found.']), 404
    # Client-side routes (e.g. /business/3) are resolved by React Router.
    return app.send_static_file('index.html')


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    if _is_api():
        return jsonify(errors=[e.description]), e.code
    return e


@app.errorhandler(Exception)
def handle_unexpected(e):
    app.logger.exception('Unhandled error')
    db.session.rollback()
    return jsonify(errors=['Something went wrong. Please try again.']), 500
