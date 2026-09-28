from flask import Blueprint
from flask_login import login_required, current_user
from sqlalchemy import func
from ..forms import DishForm
from ..models import db, Business, Dish, Category, Review, OrderDetail, CartItem
from .utils import form_errors, error, get_or_404, json_body, serialize_dishes, dish_ratings

dish_bp = Blueprint('dish', __name__)


def _owned_business(business_id):
    business = get_or_404(Business, business_id)
    if business.owner_id != current_user.id:
        return None, error('You can only manage menus for your own restaurants.', 403)
    return business, None


def _apply_form(dish, form):
    if db.session.get(Category, form.category_id.data) is None:
        return error('Category: choose a valid category.')
    dish.name = form.name.data
    dish.description = form.description.data or None
    dish.price = round(form.price.data, 2)
    dish.image_id = form.image_id.data
    dish.category_id = form.category_id.data
    dish.calories = form.calories.data
    return None


@dish_bp.route('/', methods=['GET'])
def get_all_dishes():
    """Every dish with its rating."""
    return {'dishes': serialize_dishes(Dish.query.order_by(Dish.id).all())}


@dish_bp.route('/<int:dish_id>', methods=['GET'])
def get_single_dish(dish_id):
    """One dish with rating summary."""
    dish = get_or_404(Dish, dish_id)
    avg, count = dish_ratings([dish.id]).get(dish.id, (None, 0))
    return dish.to_dict(avg, count)


@dish_bp.route('/business/<int:business_id>', methods=['POST'])
@login_required
def add_dish(business_id):
    """Adds a dish to a restaurant menu (owner only)."""
    business, denied = _owned_business(business_id)
    if denied:
        return denied
    form = DishForm()
    if not form.validate_on_submit():
        return error(form_errors(form))
    dish = Dish(business_id=business.id)
    invalid = _apply_form(dish, form)
    if invalid:
        return invalid
    db.session.add(dish)
    db.session.commit()
    return dish.to_dict(), 201


@dish_bp.route('/<int:dish_id>', methods=['PUT'])
@login_required
def update_dish(dish_id):
    """Updates a dish (owner only)."""
    dish = get_or_404(Dish, dish_id)
    _, denied = _owned_business(dish.business_id)
    if denied:
        return denied
    form = DishForm()
    if not form.validate_on_submit():
        return error(form_errors(form))
    invalid = _apply_form(dish, form)
    if invalid:
        return invalid
    db.session.commit()
    avg, count = dish_ratings([dish.id]).get(dish.id, (None, 0))
    return dish.to_dict(avg, count)


@dish_bp.route('/<int:dish_id>/availability', methods=['PATCH'])
@login_required
def toggle_availability(dish_id):
    """Marks a dish as sold out / available (owner only)."""
    dish = get_or_404(Dish, dish_id)
    _, denied = _owned_business(dish.business_id)
    if denied:
        return denied
    dish.is_available = bool(json_body().get('is_available', not dish.is_available))
    db.session.commit()
    return dish.to_dict()


@dish_bp.route('/<int:dish_id>', methods=['DELETE'])
@login_required
def delete_dish(dish_id):
    """Deletes a dish and its reviews (owner only)."""
    dish = get_or_404(Dish, dish_id)
    _, denied = _owned_business(dish.business_id)
    if denied:
        return denied
    CartItem.query.filter_by(dish_id=dish.id).delete(synchronize_session=False)
    OrderDetail.query.filter_by(dish_id=dish.id).delete(synchronize_session=False)
    Review.query.filter_by(dish_id=dish.id).delete(synchronize_session=False)
    db.session.delete(dish)
    db.session.commit()
    return {'message': 'Dish deleted.'}


@dish_bp.route('/top-rated', methods=['GET'])
def get_top_rated_dishes():
    """Highest average rating (minimum 1 review)."""
    avg = func.avg(Review.rating)
    rows = (db.session.query(Dish, avg, func.count(Review.id))
            .join(Review, Dish.id == Review.dish_id)
            .group_by(Dish.id)
            .order_by(avg.desc(), func.count(Review.id).desc())
            .limit(10).all())
    return {'dishes': [dish.to_dict(rating, count) for dish, rating, count in rows]}


@dish_bp.route('/top-ordered', methods=['GET'])
def get_top_ordered_dishes():
    """Most frequently ordered dishes."""
    total = func.sum(OrderDetail.quantity)
    rows = (db.session.query(Dish, total)
            .join(OrderDetail, Dish.id == OrderDetail.dish_id)
            .group_by(Dish.id)
            .order_by(total.desc())
            .limit(10).all())
    ratings = dish_ratings([d.id for d, _ in rows])
    result = []
    for dish, orders in rows:
        data = dish.to_dict(*ratings.get(dish.id, (None, 0)))
        data['orders'] = int(orders or 0)
        result.append(data)
    return {'dishes': result}
