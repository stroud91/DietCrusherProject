from .db import db, schema_args, add_prefix_for_prod, utcnow


class Cart(db.Model):
    __tablename__ = 'carts'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)

    items = db.relationship('CartItem', back_populates='cart', cascade="all, delete-orphan",
                            order_by='CartItem.id')
    order = db.relationship("Order", back_populates="cart", uselist=False)

    @property
    def business(self):
        for item in self.items:
            if item.dish:
                return item.dish.business
        return None

    @property
    def subtotal(self):
        return round(sum(i.dish.price * i.quantity for i in self.items if i.dish), 2)

    def to_dict(self):
        business = self.business
        return {
            'id': self.id,
            'business': business.to_dict() if business else None,
            'items': [item.to_dict() for item in self.items],
            'count': sum(i.quantity for i in self.items),
            'subtotal': self.subtotal,
        }
