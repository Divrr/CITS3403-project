from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, InputRequired, Email
from app.models import User

class OfferRequestForm(FlaskForm):
    type = SelectField('Type', choices=[('', 'Select an item type'), ('offer', 'Offer'), ('request', 'Request')], validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(max=15)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Submit')

class SigninForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')
        
class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

