from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db import db, schema_args, utcnow, iso

DEFAULT_AVATAR = 'https://robohash.org/dietcrusher?set=set4'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    profile_image_id = db.Column(db.String(length=1000), nullable=True, default=DEFAULT_AVATAR)
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)

    businesses_owned = db.relationship('Business', back_populates="owner")
    orders = db.relationship("Order", back_populates="user", lazy=True)
    reviews = db.relationship("Review", back_populates="user", lazy=True)
    favorites = db.relationship("Favorite", back_populates="user", lazy=True, cascade="all, delete-orphan")

    @property
    def password(self):
        raise AttributeError('Password is write-only.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def avatar(self):
        return self.profile_image_id or DEFAULT_AVATAR

    def to_public_dict(self):
        return {'id': self.id, 'username': self.username, 'profile_image_id': self.avatar}

    def to_dict(self):
        """Private view: only ever returned to the user themselves."""
        return {
            'id': self.id,
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'profile_image_id': self.avatar,
            'created_at': iso(self.created_at),
            'business_ids': [b.id for b in self.businesses_owned],
        }
