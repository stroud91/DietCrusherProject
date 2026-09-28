from flask import Blueprint
from flask_login import login_required, current_user
from ..forms import ReviewForm
from ..models import db, Review, Dish
from ..models.db import utcnow
from .utils import form_errors, error, get_or_404, json_body, int_arg

review_routes = Blueprint('reviews', __name__)


def _summary(reviews):
    counts = {star: 0 for star in range(1, 6)}
    for review in reviews:
        counts[review.rating] = counts.get(review.rating, 0) + 1
    total = len(reviews)
    average = round(sum(r.rating for r in reviews) / total, 1) if total else None
    return {'average': average, 'count': total, 'distribution': counts}


@review_routes.route('/dish/<int:dish_id>', methods=['GET'])
def get_reviews_for_dish(dish_id):
    """Reviews for one dish, newest first, with a rating breakdown."""
    get_or_404(Dish, dish_id)
    reviews = Review.query.filter_by(dish_id=dish_id).order_by(Review.created_at.desc()).all()
    return {'reviews': [r.to_dict() for r in reviews], 'summary': _summary(reviews)}


@review_routes.route('/business/<int:business_id>', methods=['GET'])
def get_reviews_for_business(business_id):
    """Recent reviews across a restaurant's dishes."""
    reviews = (Review.query.join(Dish).filter(Dish.business_id == business_id)
               .order_by(Review.created_at.desc()).all())
    return {'reviews': [r.to_dict() for r in reviews[:20]], 'summary': _summary(reviews)}


@review_routes.route('/user', methods=['GET'])
@login_required
def get_user_reviews():
    """The current user's reviews."""
    reviews = Review.query.filter_by(user_id=current_user.id).order_by(Review.created_at.desc()).all()
    return {'reviews': [r.to_dict() for r in reviews]}


@review_routes.route('/', methods=['POST'])
@login_required
def create_review():
    """Creates a review. One per user per dish; owners cannot review their own dishes."""
    dish = get_or_404(Dish, int_arg(json_body(), 'dish_id', 0))
    if dish.business and dish.business.owner_id == current_user.id:
        return error("You can't review dishes from your own restaurant.", 403)
    if Review.query.filter_by(dish_id=dish.id, user_id=current_user.id).first():
        return error("You've already reviewed this dish. Edit your existing review instead.", 409)
    form = ReviewForm()
    if not form.validate_on_submit():
        return error(form_errors(form))
    review = Review(user_id=current_user.id, dish_id=dish.id,
                    comment=form.comment.data, rating=form.rating.data)
    db.session.add(review)
    db.session.commit()
    return review.to_dict(), 201


@review_routes.route('/<int:review_id>', methods=['PUT'])
@login_required
def update_review(review_id):
    """Updates your own review."""
    review = get_or_404(Review, review_id)
    if review.user_id != current_user.id:
        return error('You can only edit your own reviews.', 403)
    form = ReviewForm()
    if not form.validate_on_submit():
        return error(form_errors(form))
    review.comment = form.comment.data
    review.rating = form.rating.data
    review.review_date = utcnow()
    db.session.commit()
    return review.to_dict()


@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    """Deletes your own review."""
    review = get_or_404(Review, review_id)
    if review.user_id != current_user.id:
        return error('You can only delete your own reviews.', 403)
    db.session.delete(review)
    db.session.commit()
    return {'message': 'Review deleted.'}
