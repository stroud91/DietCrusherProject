
from .db import db, environment, SCHEMA, add_prefix_for_prod

class CartItem(db.Model):
    __tablename__ = 'cart_items'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')))
    dish_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('dishes.id')))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    cart = db.relationship('Cart', back_populates='items', primaryjoin='CartItem.cart_id == Cart.id')
    dish = db.relationship('Dish', back_populates='item')

    def to_dict(self):
        return {
            'id': self.id,
            'cart_id': self.cart_id,
            'dish_id': self.dish_id,
            'quantity': self.quantity,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'dish': self.dish.to_dict() if self.dish else None
        }
