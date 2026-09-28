from flask import Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func
from ..extensions import limiter
from ..forms import LoginForm, SignUpForm, ProfileForm, PasswordForm
from ..models import User, db
from .utils import form_errors, error

auth_routes = Blueprint('auth', __name__)

INVALID_LOGIN = 'Invalid email or password.'


@auth_routes.route('/')
def authenticate():
    """Returns the logged-in user, or null."""
    if current_user.is_authenticated:
        return {'user': current_user.to_dict()}
    return {'user': None}


@auth_routes.route('/login', methods=['POST'])
@limiter.limit("10 per minute; 50 per hour")
def login():
    """Logs a user in. Uses a single generic error to avoid account enumeration."""
    form = LoginForm()
    if not form.validate_on_submit():
        return error(INVALID_LOGIN, 401)
    user = User.query.filter(func.lower(User.email) == form.email.data.lower()).first()
    if not user or not user.check_password(form.password.data):
        return error(INVALID_LOGIN, 401)
    login_user(user, remember=True)
    return {'user': user.to_dict()}


@auth_routes.route('/logout', methods=['POST'])
def logout():
    """Logs a user out."""
    logout_user()
    return {'message': 'Logged out.'}


@auth_routes.route('/signup', methods=['POST'])
@limiter.limit("5 per minute; 30 per hour")
def sign_up():
    """Creates a new user and logs them in."""
    form = SignUpForm()
    if not form.validate_on_submit():
        return error(form_errors(form), 400)
    user = User(
        username=form.username.data,
        email=form.email.data.lower(),
        password=form.password.data,
        address=form.address.data or None,
        phone=form.phone.data or None,
        profile_image_id=form.profile_image_id.data or None,
        first_name=form.first_name.data or None,
        last_name=form.last_name.data or None,
    )
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=True)
    return {'user': user.to_dict()}, 201


@auth_routes.route('/profile', methods=['PATCH'])
@login_required
def update_profile():
    """Updates the current user's profile details."""
    form = ProfileForm()
    if not form.validate_on_submit():
        return error(form_errors(form), 400)
    for field in ('address', 'phone', 'profile_image_id', 'first_name', 'last_name'):
        setattr(current_user, field, getattr(form, field).data or None)
    db.session.commit()
    return {'user': current_user.to_dict()}


@auth_routes.route('/password', methods=['POST'])
@login_required
@limiter.limit("5 per minute")
def change_password():
    """Changes the current user's password after verifying the old one."""
    form = PasswordForm()
    if not form.validate_on_submit():
        return error(form_errors(form), 400)
    if not current_user.check_password(form.current_password.data):
        return error('Current password is incorrect.', 400)
    current_user.password = form.new_password.data
    db.session.commit()
    return {'message': 'Password updated.'}
