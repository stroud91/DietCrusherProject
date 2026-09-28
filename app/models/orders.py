from .db import db, schema_args, add_prefix_for_prod, utcnow, iso

ORDER_STATUSES = ['Placed', 'Preparing', 'On the way', 'Delivered']
CANCELLED = 'Cancelled'
# Statuses used by the original seed data
LEGACY_STATUSES = {'Processing': 'Preparing', 'Shipped': 'On the way'}


def normalize_status(status):
    return LEGACY_STATUSES.get(status, status)


class Order(db.Model):
    __tablename__ = 'orders'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    business_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('business.id')), nullable=True)
    total_price = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=True)
    delivery_fee = db.Column(db.Float, nullable=True)
    tax = db.Column(db.Float, nullable=True)
    tip = db.Column(db.Float, nullable=True)
    discount = db.Column(db.Float, nullable=True)
    promo_code = db.Column(db.String(length=40), nullable=True)
    notes = db.Column(db.String(length=300), nullable=True)
    order_date = db.Column(db.DateTime, nullable=False, default=utcnow)
    delivery_address = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False, default='Placed')
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')))

    user = db.relationship("User", back_populates="orders")
    business = db.relationship("Business")
    order_details = db.relationship("OrderDetail", back_populates="order", lazy=True,
                                    cascade="all, delete-orphan")
    cart = db.relationship("Cart", back_populates="order", uselist=False)

    @property
    def resolved_business(self):
        if self.business:
            return self.business
        for detail in self.order_details:
            if detail.dish and detail.dish.business:
                return detail.dish.business
        return None

    def to_dict(self, include_items=False):
        business = self.resolved_business
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'business_id': business.id if business else None,
            'business_name': business.name if business else None,
            'business_logo': business.logo_id if business else None,
            'total_price': round(self.total_price, 2),
            'subtotal': round(self.subtotal, 2) if self.subtotal is not None else None,
            'delivery_fee': self.delivery_fee,
            'tax': self.tax,
            'tip': self.tip,
            'discount': self.discount,
            'promo_code': self.promo_code,
            'notes': self.notes,
            'order_date': iso(self.order_date),
            'delivery_address': self.delivery_address,
            'status': normalize_status(self.status),
            'item_count': sum(d.quantity for d in self.order_details),
            'created_at': iso(self.created_at),
            'updated_at': iso(self.updated_at),
        }
        if include_items:
            data['items'] = [d.to_dict() for d in self.order_details]
        return data
