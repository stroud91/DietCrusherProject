from .db import db, schema_args, add_prefix_for_prod, utcnow, iso


class Dish(db.Model):
    __tablename__ = 'dishes'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('business.id')))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    image_id = db.Column(db.String(length=1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')))
    calories = db.Column(db.Integer, nullable=True)
    is_available = db.Column(db.Boolean, nullable=False, default=True, server_default=db.true())
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)

    business = db.relationship("Business", back_populates="dishes")
    category = db.relationship("Category", back_populates="dishes")
    item = db.relationship('CartItem', back_populates='dish', cascade="all, delete-orphan")
    order_details = db.relationship("OrderDetail", back_populates="dish", lazy=True)
    reviews = db.relationship("Review", back_populates="dish", lazy=True, cascade="all, delete-orphan")

    def to_dict(self, rating=None, review_count=0):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'business_name': self.business.name if self.business else None,
            'name': self.name,
            'description': self.description,
            'image_id': self.image_id,
            'price': round(self.price, 2),
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else None,
            'calories': self.calories,
            'is_available': self.is_available if self.is_available is not None else True,
            'rating': round(float(rating), 1) if rating is not None else None,
            'review_count': review_count or 0,
            'created_at': iso(self.created_at),
            'updated_at': iso(self.updated_at),
        }
