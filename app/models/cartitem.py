from .db import db, schema_args, add_prefix_for_prod, utcnow


class CartItem(db.Model):
    __tablename__ = 'cart_items'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')))
    dish_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('dishes.id')))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)

    cart = db.relationship('Cart', back_populates='items')
    dish = db.relationship('Dish', back_populates='item')

    def to_dict(self):
        dish = self.dish
        return {
            'id': self.id,
            'dish_id': self.dish_id,
            'quantity': self.quantity,
            'name': dish.name if dish else 'Unavailable item',
            'price': round(dish.price, 2) if dish else 0,
            'image_id': dish.image_id if dish else None,
            'line_total': round(dish.price * self.quantity, 2) if dish else 0,
        }
