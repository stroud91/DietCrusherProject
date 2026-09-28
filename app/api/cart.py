from flask import Blueprint
from flask_login import login_required, current_user
from ..models import db, Cart, CartItem, Dish
from .utils import error, get_or_404, json_body, int_arg

cart_bp = Blueprint('cart', __name__)

MAX_QUANTITY = 25


def get_or_create_cart():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.flush()
    return cart


def _own_item(item_id):
    item = get_or_404(CartItem, item_id)
    if not item.cart or item.cart.user_id != current_user.id:
        # Don't reveal that another user's cart item exists.
        return None
    return item


@cart_bp.route('/', methods=['GET'])
@login_required
def view_cart():
    """The current user's cart with server-computed subtotal."""
    cart = get_or_create_cart()
    db.session.commit()
    return cart.to_dict()


@cart_bp.route('/items', methods=['POST'])
@login_required
def add_to_cart():
    """Adds a dish. Carts hold one restaurant at a time; pass replace=true to start over."""
    data = json_body()
    dish = get_or_404(Dish, int_arg(data, 'dish_id', 0))
    quantity = int_arg(data, 'quantity', 1, minimum=1, maximum=MAX_QUANTITY)
    if not dish.is_available:
        return error(f'{dish.name} is sold out right now.', 409)
    if dish.business and dish.business.owner_id == current_user.id:
        return error("You can't order from your own restaurant.", 403)

    cart = get_or_create_cart()
    current_business = cart.business
    if current_business and current_business.id != dish.business_id:
        if not data.get('replace'):
            return error(f'Your cart has items from {current_business.name}.', 409,
                         code='DIFFERENT_BUSINESS', business_name=current_business.name)
        for item in list(cart.items):
            db.session.delete(item)
        db.session.flush()
        db.session.expire(cart, ['items'])

    item = CartItem.query.filter_by(cart_id=cart.id, dish_id=dish.id).first()
    if item:
        item.quantity = min(MAX_QUANTITY, item.quantity + quantity)
    else:
        db.session.add(CartItem(cart_id=cart.id, dish_id=dish.id, quantity=quantity))
    db.session.commit()
    db.session.refresh(cart)
    return cart.to_dict()


@cart_bp.route('/items/<int:item_id>', methods=['PATCH'])
@login_required
def update_cart_item(item_id):
    """Sets an item's quantity (0 removes it)."""
    item = _own_item(item_id)
    if item is None:
        return error('Cart item not found.', 404)
    quantity = int_arg(json_body(), 'quantity', item.quantity, minimum=0, maximum=MAX_QUANTITY)
    cart = item.cart
    if quantity == 0:
        db.session.delete(item)
    else:
        item.quantity = quantity
    db.session.commit()
    db.session.refresh(cart)
    return cart.to_dict()


@cart_bp.route('/items/<int:item_id>', methods=['DELETE'])
@login_required
def remove_from_cart(item_id):
    """Removes an item from the cart."""
    item = _own_item(item_id)
    if item is None:
        return error('Cart item not found.', 404)
    cart = item.cart
    db.session.delete(item)
    db.session.commit()
    db.session.refresh(cart)
    return cart.to_dict()


@cart_bp.route('/', methods=['DELETE'])
@login_required
def clear_cart():
    """Empties the cart."""
    cart = get_or_create_cart()
    for item in list(cart.items):
        db.session.delete(item)
    db.session.commit()
    db.session.refresh(cart)
    return cart.to_dict()
