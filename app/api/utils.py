from flask import abort, jsonify, request
from sqlalchemy import func
from ..models import db, Review, Dish


def form_errors(form):
    """Flatten WTForms errors into a list of human-readable messages."""
    messages = []
    for field, errors in form.errors.items():
        label = getattr(form, field).label.text if hasattr(form, field) else field
        for error in errors:
            messages.append(f'{label}: {error}')
    return messages


def error(message, status=400, **extra):
    return jsonify(errors=[message] if isinstance(message, str) else message, **extra), status


def get_or_404(model, ident):
    obj = db.session.get(model, ident)
    if obj is None:
        abort(404, description=f'{model.__name__} not found.')
    return obj


def json_body():
    data = request.get_json(silent=True)
    return data if isinstance(data, dict) else {}


def int_arg(data, key, default=None, minimum=None, maximum=None):
    try:
        value = int(data.get(key, default))
    except (TypeError, ValueError):
        return default
    if minimum is not None:
        value = max(minimum, value)
    if maximum is not None:
        value = min(maximum, value)
    return value


def business_ratings(business_ids=None):
    """{business_id: (avg_rating, review_count)} in a single aggregate query."""
    query = (db.session.query(Dish.business_id, func.avg(Review.rating), func.count(Review.id))
             .join(Review, Review.dish_id == Dish.id)
             .group_by(Dish.business_id))
    if business_ids is not None:
        query = query.filter(Dish.business_id.in_(business_ids))
    return {bid: (avg, count) for bid, avg, count in query.all()}


def dish_ratings(dish_ids=None):
    query = (db.session.query(Review.dish_id, func.avg(Review.rating), func.count(Review.id))
             .group_by(Review.dish_id))
    if dish_ids is not None:
        query = query.filter(Review.dish_id.in_(dish_ids))
    return {did: (avg, count) for did, avg, count in query.all()}


def serialize_businesses(businesses):
    ratings = business_ratings([b.id for b in businesses])
    return [b.to_dict(*ratings.get(b.id, (None, 0))) for b in businesses]


def serialize_dishes(dishes):
    ratings = dish_ratings([d.id for d in dishes])
    return [d.to_dict(*ratings.get(d.id, (None, 0))) for d in dishes]
