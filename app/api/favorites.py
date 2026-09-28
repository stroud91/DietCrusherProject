from flask import Blueprint
from flask_login import login_required, current_user
from ..models import db, Business, Favorite
from .utils import get_or_404, serialize_businesses

favorites_bp = Blueprint('favorites', __name__)


@favorites_bp.route('/', methods=['GET'])
@login_required
def list_favorites():
    """Restaurants the current user saved."""
    favorites = Favorite.query.filter_by(user_id=current_user.id).order_by(Favorite.created_at.desc()).all()
    return {'businesses': serialize_businesses([f.business for f in favorites if f.business])}


@favorites_bp.route('/<int:business_id>', methods=['PUT'])
@login_required
def add_favorite(business_id):
    """Saves a restaurant (idempotent)."""
    get_or_404(Business, business_id)
    if not Favorite.query.filter_by(user_id=current_user.id, business_id=business_id).first():
        db.session.add(Favorite(user_id=current_user.id, business_id=business_id))
        db.session.commit()
    return {'business_id': business_id, 'favorite': True}


@favorites_bp.route('/<int:business_id>', methods=['DELETE'])
@login_required
def remove_favorite(business_id):
    """Un-saves a restaurant (idempotent)."""
    Favorite.query.filter_by(user_id=current_user.id, business_id=business_id).delete()
    db.session.commit()
    return {'business_id': business_id, 'favorite': False}
