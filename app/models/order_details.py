from .db import db, schema_args, add_prefix_for_prod


class OrderDetail(db.Model):
    __tablename__ = 'orderdetails'
    __table_args__ = schema_args()

    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('orders.id')), primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('dishes.id')), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal_price = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", back_populates="order_details")
    dish = db.relationship("Dish", back_populates="order_details", lazy=True)

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'dish_id': self.dish_id,
            'name': self.dish.name if self.dish else 'Removed item',
            'image_id': self.dish.image_id if self.dish else None,
            'quantity': self.quantity,
            'subtotal_price': round(self.subtotal_price, 2),
        }
