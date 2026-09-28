from .db import db, schema_args


class Category(db.Model):
    __tablename__ = 'categories'
    __table_args__ = schema_args()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    dishes = db.relationship("Dish", back_populates="category", lazy=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}
