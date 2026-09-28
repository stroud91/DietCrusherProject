from flask import Blueprint
from flask_login import login_required, current_user
from ..models import User
from .utils import get_or_404

user_routes = Blueprint('users', __name__)


@user_routes.route('/me')
@login_required
def me():
    """The current user's private profile."""
    return current_user.to_dict()


@user_routes.route('/<int:user_id>')
def user(user_id):
    """Public profile only (no email, phone or address)."""
    return get_or_404(User, user_id).to_public_dict()
