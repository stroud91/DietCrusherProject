from .db import db, schema_args, add_prefix_for_prod, utcnow, iso


class Business(db.Model):
    __tablename__ = 'business'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String(length=50), nullable=False)
    state = db.Column(db.String(length=25), nullable=False)
    zip_code = db.Column(db.String(length=10), nullable=False)
    about = db.Column(db.String(length=500), nullable=False)
    phone_number = db.Column(db.String(length=30), nullable=False)
    type = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String, nullable=True, unique=True)
    logo_id = db.Column(db.String(length=1000), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    delivery_fee = db.Column(db.Float, nullable=False, default=2.99, server_default='2.99')
    prep_time = db.Column(db.Integer, nullable=False, default=25, server_default='25')
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)

    owner = db.relationship("User", back_populates="businesses_owned")
    dishes = db.relationship("Dish", back_populates="business", lazy=True)
    favorites = db.relationship("Favorite", back_populates="business", lazy=True, cascade="all, delete-orphan")

    @property
    def cuisines(self):
        return [c.strip() for c in (self.type or '').split(',') if c.strip()]

    def to_dict(self, rating=None, review_count=0):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone_number,
            'about': self.about,
            'type': self.type,
            'cuisines': self.cuisines,
            'email': self.email,
            'logo_id': self.logo_id,
            'owner_id': self.owner_id,
            'delivery_fee': round(self.delivery_fee if self.delivery_fee is not None else 2.99, 2),
            'prep_time': self.prep_time or 25,
            'rating': round(float(rating), 1) if rating is not None else None,
            'review_count': review_count or 0,
            'created_at': iso(self.created_at),
            'updated_at': iso(self.updated_at),
        }
