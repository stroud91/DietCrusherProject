from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, Email, NumberRange, Regexp
from .validators import https_url, digits_between, strip


class BusinessForm(FlaskForm):
    name = StringField('Business Name', filters=[strip], validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField('Description', filters=[strip], validators=[Optional(), Length(max=255)])
    address = StringField('Address', filters=[strip], validators=[DataRequired(), Length(max=255)])
    city = StringField('City', filters=[strip], validators=[DataRequired(), Length(max=50)])
    state = StringField('State', filters=[strip], validators=[
        DataRequired(), Regexp(r'^[A-Za-z]{2}$', message='Use a 2-letter state code.')])
    zip_code = StringField('ZIP Code', filters=[strip], validators=[
        DataRequired(), Regexp(r'^\d{5}(-\d{4})?$', message='Enter a valid ZIP code.')])
    phone_number = StringField('Phone Number', filters=[strip], validators=[
        DataRequired(), Length(max=30), digits_between(10, 11, 'Enter a valid 10-digit phone number.')])
    about = StringField('About', filters=[strip], validators=[DataRequired(), Length(max=500)])
    type = StringField('Cuisine', filters=[strip], validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', filters=[strip], validators=[Optional(), Email(check_deliverability=False), Length(max=255)])
    logo_id = StringField('Image', filters=[strip], validators=[DataRequired(), Length(max=1000), https_url])
    delivery_fee = FloatField('Delivery fee', validators=[Optional(), NumberRange(min=0, max=50)])
    prep_time = IntegerField('Prep time', validators=[Optional(), NumberRange(min=5, max=120)])
