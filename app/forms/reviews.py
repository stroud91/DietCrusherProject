from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length
from .validators import strip


class ReviewForm(FlaskForm):
    comment = StringField('Review', filters=[strip], validators=[
        DataRequired(), Length(min=10, max=500, message="Reviews must be 10–500 characters.")])
    rating = IntegerField('Rating', validators=[
        DataRequired(), NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")])
