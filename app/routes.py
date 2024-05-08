from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from werkzeug.security import generate_password_hash
from config import Config

from app import app, db


app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class SigninForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

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

@app.route("/")
@app.route("/index")
def index():
    myitems = [
        { "email": "zahravink@gmail.com", "content": "Can someone mow my lawn?", "name": "Joe", "type": "Request"},
        { "email": "zahravink@gmail.com", "content": "I can teach you to bake cookies", "name": "Youssef", "type": "Offer"}
    ]
    myaccepts = [
        { "email": "zahravink@gmail.com", "content": "Can someone give a 30min crash course on Flask?", "name": "Zahra", "type": "Request"},
        { "email": "zahravink@gmail.com", "content": "I can fix a garborator", "name": "May", "type": "Offer"}
    ]
    return render_template("mainpage.html", title="UWA Community Hub", items=myitems, accepts=myaccepts)

from app.forms import OfferRequestForm
@app.route("/form")
def form():
    form_object = OfferRequestForm()
    return render_template("offer_request_form.html", title="Create an Offer or Request", form=form_object)

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if generate_password_hash(user.password, form.password.data):
                login_user(user)
    return render_template("login.html", form=form)

@app.route("/signup")
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("signup.html", form=form)


@app.route("/offers")
def offers():
    offerlist = Activity.query.filter_by(type='Offer').all()
    print(offerlist)
    return render_template("offers.html", title="All Offers", offers=offerlist)

@app.route("/requests")
def requests():
    requestlist = Activity.query.filter_by(type='Request').all()
    print(request)
    return render_template("requests.html", title="All Requests", requests=requestlist)

auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})