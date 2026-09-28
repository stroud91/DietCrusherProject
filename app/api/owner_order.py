from flask import Blueprint
from flask_login import login_required, current_user
from sqlalchemy import func, or_, select
from ..models import db, Business, Order, OrderDetail, Dish, Review
from ..models.orders import ORDER_STATUSES, CANCELLED, normalize_status
from .utils import error, get_or_404, json_body

owner_bp = Blueprint('owner', __name__)

FINAL_STATUSES = {'Delivered', CANCELLED}


def _owned_business(business_id):
    business = get_or_404(Business, business_id)
    if business.owner_id != current_user.id:
        return None
    return business


def _business_orders(business_id):
    via_dishes = select(OrderDetail.order_id).join(Dish).where(Dish.business_id == business_id)
    return Order.query.filter(or_(Order.business_id == business_id, Order.id.in_(via_dishes)))


def _owner_view(order):
    data = order.to_dict(include_items=True)
    data['customer'] = order.user.username if order.user else 'Former customer'
    return data


@owner_bp.route('/business/<int:business_id>/orders', methods=['GET'])
@login_required
def get_business_orders(business_id):
    """Orders for a restaurant you own."""
    if not _owned_business(business_id):
        return error('Restaurant not found.', 404)
    orders = _business_orders(business_id).order_by(Order.created_at.desc(), Order.id.desc()).all()
    return {'orders': [_owner_view(o) for o in orders]}


@owner_bp.route('/business/<int:business_id>/stats', methods=['GET'])
@login_required
def get_business_stats(business_id):
    """Revenue, order and rating stats for a restaurant you own."""
    business = _owned_business(business_id)
    if not business:
        return error('Restaurant not found.', 404)
    orders = _business_orders(business_id).all()
    active = [o for o in orders if normalize_status(o.status) != CANCELLED]
    by_status = {}
    for order in orders:
        status = normalize_status(order.status)
        by_status[status] = by_status.get(status, 0) + 1
    avg, count = (db.session.query(func.avg(Review.rating), func.count(Review.id))
                  .join(Dish).filter(Dish.business_id == business_id).one())
    total_qty = func.sum(OrderDetail.quantity)
    top = (db.session.query(Dish.id, Dish.name, total_qty)
           .join(OrderDetail).filter(Dish.business_id == business_id)
           .group_by(Dish.id, Dish.name).order_by(total_qty.desc()).limit(5).all())
    return {
        'orders': len(orders),
        'revenue': round(sum(o.total_price for o in active), 2),
        'average_order': round(sum(o.total_price for o in active) / len(active), 2) if active else 0,
        'rating': round(float(avg), 1) if avg is not None else None,
        'review_count': count,
        'by_status': by_status,
        'top_dishes': [{'id': i, 'name': n, 'quantity': int(q or 0)} for i, n, q in top],
    }


@owner_bp.route('/orders/<int:order_id>/status', methods=['PATCH'])
@login_required
def update_order_status(order_id):
    """Moves an order along: Placed → Preparing → On the way → Delivered (or Cancelled)."""
    order = get_or_404(Order, order_id)
    business = order.resolved_business
    if not business or business.owner_id != current_user.id:
        return error('Order not found.', 404)
    status = (json_body().get('status') or '').strip()
    if status not in ORDER_STATUSES and status != CANCELLED:
        return error('Unknown status.')
    if normalize_status(order.status) in FINAL_STATUSES:
        return error('This order is already closed.', 409)
    order.status = status
    db.session.commit()
    return _owner_view(order)
