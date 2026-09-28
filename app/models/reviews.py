from .db import db, schema_args, add_prefix_for_prod, utcnow, iso


class Review(db.Model):
    __tablename__ = 'reviews'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    dish_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('dishes.id')))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)
    review_date = db.Column(db.DateTime, nullable=False, default=utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)

    user = db.relationship("User", back_populates="reviews", lazy=True)
    dish = db.relationship("Dish", back_populates="reviews", lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_name': self.user.username if self.user else 'Former user',
            'profile_image_id': self.user.avatar if self.user else None,
            'dish_id': self.dish_id,
            'dish_name': self.dish.name if self.dish else None,
            'rating': self.rating,
            'comment': self.comment,
            'review_date': iso(self.review_date),
            'created_at': iso(self.created_at),
            'updated_at': iso(self.updated_at),
        }
