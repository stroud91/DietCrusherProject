import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, ValidationError, Regexp
from sqlalchemy import func
from app.models import User
from .validators import https_url, strip


def email_available(form, field):
    if User.query.filter(func.lower(User.email) == field.data.lower()).first():
        raise ValidationError('Email address is already in use.')


def username_available(form, field):
    if User.query.filter(func.lower(User.username) == field.data.lower()).first():
        raise ValidationError('Username is already in use.')


def strong_password(form, field):
    value = field.data or ''
    if len(value) < 8 or not re.search(r'[A-Za-z]', value) or not re.search(r'\d', value):
        raise ValidationError('Use at least 8 characters with a letter and a number.')


class ProfileFields:
    address = StringField('address', filters=[strip], validators=[Optional(), Length(max=255)])
    phone = StringField('phone', filters=[strip], validators=[Optional(), Length(max=30)])
    profile_image_id = StringField('profile_image_id', filters=[strip],
                                   validators=[Optional(), Length(max=1000), https_url])
    first_name = StringField('first_name', filters=[strip], validators=[Optional(), Length(max=50)])
    last_name = StringField('last_name', filters=[strip], validators=[Optional(), Length(max=50)])


class SignUpForm(FlaskForm, ProfileFields):
    username = StringField('username', filters=[strip], validators=[
        DataRequired(), Length(min=3, max=30),
        Regexp(r'^[A-Za-z0-9_.-]+$', message='Letters, numbers, dots, dashes and underscores only.'),
        username_available])
    email = StringField('email', filters=[strip], validators=[
        DataRequired(), Email(check_deliverability=False), Length(max=255), email_available])
    password = PasswordField('password', validators=[DataRequired(), Length(max=128), strong_password])


class ProfileForm(FlaskForm, ProfileFields):
    pass


class PasswordForm(FlaskForm):
    current_password = PasswordField('current_password', validators=[DataRequired()])
    new_password = PasswordField('new_password', validators=[DataRequired(), Length(max=128), strong_password])
