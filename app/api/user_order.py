from flask import Blueprint
from flask_login import login_required, current_user
from ..extensions import limiter
from ..models import db, Order, OrderDetail, CartItem
from ..models.orders import normalize_status, CANCELLED
from .cart import get_or_create_cart, MAX_QUANTITY
from .utils import error, get_or_404, json_body

order_bp = Blueprint('order', __name__)

TAX_RATE = 0.08
MAX_TIP = 200
PROMO_CODES = {
    # code: (description, percent_off, flat_off, minimum_subtotal)
    'CRUSH10': ('10% off your order', 0.10, 0, 0),
    'WELCOME5': ('$5 off orders over $20', 0, 5, 20),
    'FREEDELIVERY': ('Free delivery', 0, 0, 0),
}


def price_order(subtotal, delivery_fee, tip, promo_code):
    """Server-side pricing. The client's numbers are never trusted."""
    code = (promo_code or '').strip().upper()
    discount = 0.0
    promo = PROMO_CODES.get(code) if code else None
    if code and not promo:
        return None, 'That promo code is not valid.'
    if promo:
        _, percent, flat, minimum = promo
        if subtotal < minimum:
            return None, f'{code} requires a subtotal of at least ${minimum:.2f}.'
        if code == 'FREEDELIVERY':
            delivery_fee = 0.0
        discount = round(subtotal * percent + flat, 2)
        discount = min(discount, subtotal)
    tax = round((subtotal - discount) * TAX_RATE, 2)
    total = round(subtotal - discount + delivery_fee + tax + tip, 2)
    return {
        'subtotal': round(subtotal, 2), 'delivery_fee': round(delivery_fee, 2), 'tax': tax,
        'tip': round(tip, 2), 'discount': discount, 'promo_code': code or None, 'total': total,
    }, None


def _tip(data):
    try:
        tip = float(data.get('tip') or 0)
    except (TypeError, ValueError):
        return 0.0
    return max(0.0, min(MAX_TIP, tip))


@order_bp.route('/quote', methods=['POST'])
@login_required
def quote():
    """Prices the current cart with an optional tip and promo code."""
    data = json_body()
    cart = get_or_create_cart()
    business = cart.business
    if not business:
        return error('Your cart is empty.')
    pricing, problem = price_order(cart.subtotal, business.delivery_fee, _tip(data), data.get('promo_code'))
    if problem:
        return error(problem)
    return pricing


@order_bp.route('/', methods=['POST'])
@login_required
@limiter.limit("10 per minute")
def place_order():
    """Checks out the cart: creates the order, its line items, then empties the cart."""
    data = json_body()
    address = (data.get('delivery_address') or current_user.address or '').strip()
    notes = (data.get('notes') or '').strip()[:300] or None
    if not address or len(address) > 255:
        return error('Add a delivery address.')

    cart = get_or_create_cart()
    items = [i for i in cart.items if i.dish]
    business = cart.business
    if not items or not business:
        return error('Your cart is empty.')
    unavailable = [i.dish.name for i in items if not i.dish.is_available]
    if unavailable:
        return error(f"Sold out: {', '.join(unavailable)}. Remove to continue.", 409)

    pricing, problem = price_order(cart.subtotal, business.delivery_fee, _tip(data), data.get('promo_code'))
    if problem:
        return error(problem)

    order = Order(
        user_id=current_user.id, business_id=business.id, delivery_address=address, notes=notes,
        status='Placed', total_price=pricing['total'], subtotal=pricing['subtotal'],
        delivery_fee=pricing['delivery_fee'], tax=pricing['tax'], tip=pricing['tip'],
        discount=pricing['discount'], promo_code=pricing['promo_code'],
    )
    db.session.add(order)
    db.session.flush()
    for item in items:
        db.session.add(OrderDetail(order_id=order.id, dish_id=item.dish_id, quantity=item.quantity,
                                   subtotal_price=round(item.dish.price * item.quantity, 2)))
    for item in list(cart.items):
        db.session.delete(item)
    if not current_user.address:
        current_user.address = address
    db.session.commit()
    return order.to_dict(include_items=True), 201


@order_bp.route('/', methods=['GET'])
@login_required
def get_user_orders():
    """The current user's orders, newest first."""
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc(), Order.id.desc()).all()
    return {'orders': [o.to_dict() for o in orders]}


@order_bp.route('/<int:order_id>', methods=['GET'])
@login_required
def get_order(order_id):
    """One of your orders with line items (also visible to the restaurant owner)."""
    order = get_or_404(Order, order_id)
    business = order.resolved_business
    if order.user_id != current_user.id and not (business and business.owner_id == current_user.id):
        return error('Order not found.', 404)
    return order.to_dict(include_items=True)


@order_bp.route('/<int:order_id>/cancel', methods=['POST'])
@login_required
def cancel_order(order_id):
    """Cancels your order while the restaurant hasn't started it."""
    order = get_or_404(Order, order_id)
    if order.user_id != current_user.id:
        return error('Order not found.', 404)
    if normalize_status(order.status) != 'Placed':
        return error('This order is already being prepared and can no longer be cancelled.', 409)
    order.status = CANCELLED
    db.session.commit()
    return order.to_dict(include_items=True)


@order_bp.route('/<int:order_id>/reorder', methods=['POST'])
@login_required
def reorder(order_id):
    """Replaces the cart with the available items from a past order."""
    order = get_or_404(Order, order_id)
    if order.user_id != current_user.id:
        return error('Order not found.', 404)
    details = [d for d in order.order_details if d.dish and d.dish.is_available]
    if not details:
        return error('None of the items from this order are available anymore.', 409)
    cart = get_or_create_cart()
    for item in list(cart.items):
        db.session.delete(item)
    db.session.flush()
    for detail in details:
        db.session.add(CartItem(cart_id=cart.id, dish_id=detail.dish_id,
                                quantity=min(MAX_QUANTITY, detail.quantity)))
    db.session.commit()
    db.session.refresh(cart)
    return cart.to_dict()
