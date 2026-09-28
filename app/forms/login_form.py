from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
from .validators import strip


class LoginForm(FlaskForm):
    email = StringField('email', filters=[strip], validators=[DataRequired(), Length(max=255)])
    password = PasswordField('password', validators=[DataRequired(), Length(max=128)])
