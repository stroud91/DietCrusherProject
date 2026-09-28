from flask import Blueprint, request
from sqlalchemy import or_
from ..models import Business, Dish, Category
from .utils import serialize_businesses, serialize_dishes
from .user_order import PROMO_CODES

discover_bp = Blueprint('discover', __name__)


def _like(term):
    escaped = term.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
    return f'%{escaped}%'


@discover_bp.route('/search', methods=['GET'])
def search():
    """Searches restaurants (name, cuisine, city) and dishes (name, description)."""
    term = (request.args.get('q') or '').strip()[:80]
    if len(term) < 1:
        return {'query': term, 'businesses': [], 'dishes': []}
    pattern = _like(term)
    businesses = (Business.query.filter(or_(
        Business.name.ilike(pattern, escape='\\'),
        Business.type.ilike(pattern, escape='\\'),
        Business.city.ilike(pattern, escape='\\'),
    )).order_by(Business.name).limit(20).all())
    dishes = (Dish.query.filter(or_(
        Dish.name.ilike(pattern, escape='\\'),
        Dish.description.ilike(pattern, escape='\\'),
    )).order_by(Dish.name).limit(40).all())
    return {'query': term, 'businesses': serialize_businesses(businesses), 'dishes': serialize_dishes(dishes)}


@discover_bp.route('/categories', methods=['GET'])
def categories():
    """Dish categories."""
    return {'categories': [c.to_dict() for c in Category.query.order_by(Category.id).all()]}


@discover_bp.route('/promos', methods=['GET'])
def promos():
    """Public promo codes shown on the home page."""
    return {'promos': [{'code': code, 'description': meta[0]} for code, meta in PROMO_CODES.items()]}
