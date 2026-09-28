from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, InputRequired
from .validators import https_url, strip


class DishForm(FlaskForm):
    name = StringField('Name', filters=[strip], validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Description', filters=[strip], validators=[Optional(), Length(max=500)])
    price = FloatField('Price', validators=[InputRequired(), NumberRange(min=0.5, max=1000)])
    image_id = StringField('Image', filters=[strip], validators=[DataRequired(), Length(max=1000), https_url])
    category_id = IntegerField('Category', validators=[DataRequired()])
    calories = IntegerField('Calories', validators=[Optional(), NumberRange(min=0, max=5000)])
