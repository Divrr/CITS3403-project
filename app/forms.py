from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class OfferRequestForm(FlaskForm):
    type = SelectField('Type', choices=[('', 'Select an item type'), ('offer', 'Offer'), ('request', 'Request')], validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(max=15)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Submit')