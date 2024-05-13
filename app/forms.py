from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, PasswordField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired, Email, EqualTo
from app.models import User

class OfferRequestForm(FlaskForm):
    type = SelectField('Type', choices=[('', 'Select an item type'), ('Offer', 'Offer'), ('Request', 'Request')], validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(max=15)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is already used. Please choose a different one.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('That email address is already used. Please choose a different one.')
        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')

