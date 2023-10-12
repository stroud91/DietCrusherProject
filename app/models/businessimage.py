from .db import db, environment, SCHEMA, add_prefix_for_prod


class BusinessImage(db.Model):
    __tablename__ = 'businessimages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url = db.Column(db.String, unique=True, nullable=False)
    alt_text = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)

    business = db.relationship("Business", back_populates="logo")

def to_dict(self):
    return {
        'id': self.id,
        'image_url': self.image_url,
        'alt_text': self.alt_text,
        'created_at': self.created_at,
        'uploaded_at': self.uploaded_at,
        'business_id': self.business_id
    }