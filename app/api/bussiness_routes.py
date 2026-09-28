from flask import Blueprint
from flask_login import login_required, current_user
from sqlalchemy import func
from ..forms import BusinessForm
from ..models import db, Business, Dish, Review, Order, OrderDetail, CartItem
from .utils import form_errors, error, get_or_404, serialize_businesses, serialize_dishes, business_ratings

business_bp = Blueprint('business', __name__)

EDITABLE_FIELDS = ('name', 'description', 'address', 'city', 'state', 'zip_code',
                   'phone_number', 'about', 'type', 'email', 'logo_id')


def _apply_form(business, form):
    for field in EDITABLE_FIELDS:
        value = getattr(form, field).data
        setattr(business, field, value or None if field in ('description', 'email') else value)
    business.state = business.state.upper()
    if form.delivery_fee.data is not None:
        business.delivery_fee = round(form.delivery_fee.data, 2)
    if form.prep_time.data is not None:
        business.prep_time = form.prep_time.data


def _email_taken(email, exclude_id=None):
    if not email:
        return False
    query = Business.query.filter(func.lower(Business.email) == email.lower())
    if exclude_id:
        query = query.filter(Business.id != exclude_id)
    return query.first() is not None


@business_bp.route('/', methods=['GET'])
def get_all_businesses():
    """All restaurants with average rating and review count."""
    return {'businesses': serialize_businesses(Business.query.order_by(Business.id).all())}


@business_bp.route('/mine', methods=['GET'])
@login_required
def get_my_businesses():
    """Restaurants owned by the current user."""
    businesses = Business.query.filter_by(owner_id=current_user.id).order_by(Business.id).all()
    return {'businesses': serialize_businesses(businesses)}


@business_bp.route('/<int:business_id>', methods=['GET'])
def get_single_business(business_id):
    """One restaurant with its menu."""
    business = get_or_404(Business, business_id)
    avg, count = business_ratings([business.id]).get(business.id, (None, 0))
    data = business.to_dict(avg, count)
    dishes = sorted(business.dishes, key=lambda d: (d.category.name if d.category else '', d.id))
    data['dishes'] = serialize_dishes(dishes)
    return data


@business_bp.route('/', methods=['POST'])
@login_required
def add_business():
    """Creates a restaurant owned by the current user."""
    form = BusinessForm()
    if not form.validate_on_submit():
        return error(form_errors(form))
    if _email_taken(form.email.data):
        return error('Email: another restaurant already uses this email.')
    business = Business(owner_id=current_user.id)
    _apply_form(business, form)
    db.session.add(business)
    db.session.commit()
    return business.to_dict(), 201


@business_bp.route('/<int:business_id>', methods=['PUT'])
@login_required
def edit_business(business_id):
    """Updates a restaurant (owner only)."""
    business = get_or_404(Business, business_id)
    if business.owner_id != current_user.id:
        return error('You can only edit your own restaurants.', 403)
    form = BusinessForm()
    if not form.validate_on_submit():
        return error(form_errors(form))
    if _email_taken(form.email.data, exclude_id=business.id):
        return error('Email: another restaurant already uses this email.')
    _apply_form(business, form)
    db.session.commit()
    avg, count = business_ratings([business.id]).get(business.id, (None, 0))
    return business.to_dict(avg, count)


@business_bp.route('/<int:business_id>', methods=['DELETE'])
@login_required
def delete_business(business_id):
    """Deletes a restaurant and its menu (owner only). Past orders keep their totals."""
    business = get_or_404(Business, business_id)
    if business.owner_id != current_user.id:
        return error('You can only delete your own restaurants.', 403)

    dish_ids = [d.id for d in business.dishes]
    if dish_ids:
        CartItem.query.filter(CartItem.dish_id.in_(dish_ids)).delete(synchronize_session=False)
        Review.query.filter(Review.dish_id.in_(dish_ids)).delete(synchronize_session=False)
        OrderDetail.query.filter(OrderDetail.dish_id.in_(dish_ids)).delete(synchronize_session=False)
        Dish.query.filter(Dish.id.in_(dish_ids)).delete(synchronize_session=False)
    Order.query.filter_by(business_id=business.id).update({'business_id': None}, synchronize_session=False)
    db.session.delete(business)
    db.session.commit()
    return {'message': 'Restaurant deleted.'}
