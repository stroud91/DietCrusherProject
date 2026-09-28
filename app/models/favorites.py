from .db import db, schema_args, add_prefix_for_prod, utcnow


class Favorite(db.Model):
    __tablename__ = 'favorites'
    __table_args__ = schema_args(db.UniqueConstraint('user_id', 'business_id', name='uq_favorite_user_business'))

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('business.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)

    user = db.relationship("User", back_populates="favorites")
    business = db.relationship("Business", back_populates="favorites")
