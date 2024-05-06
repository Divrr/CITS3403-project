from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

from app import app

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


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
    return render_template("mainpage.html")

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
    return render_template("login.html", form=form)

@app.route("/signup")
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("signup.html", form=form)


@app.route("/offers")
def offers():
    offerlist = [
        { "category": "REPAIRS", "description": "I'm happy to help with any plumbing issues."},
        { "category": "REPAIRS", "description": "I'm happy to help with any electrical issues."},
        { "category": "REPAIRS", "description": "I'm happy to help with any carpentry issues."},
        { "category": "SOCIAL", "description": "Always down for a coffee chat!"},
        { "category": "SOCIAL", "description": "Hosting book club! DM me if you want to join."},
        { "category": "SOCIAL", "description": "I'm hosting a board game night this Friday!"},
        { "category": "SCHOOL", "description": "I tutor grade 10 Math."},
        { "category": "SCHOOL", "description": "I tutor grade 10 Science."},
        { "category": "SCHOOL", "description": "I tutor grade 10 Socials."},
        { "category": "UNI", "description": "Happy to peer-review uni essays"},
        { "category": "UNI", "description": "I can help with any coding assignments."}
    ]
    return render_template("offers.html", offers=offerlist)

@app.route("/requests")
def requests():
    requestlist = [
        { "category": "REPAIRS", "description": "I'm happy to help with any plumbing issues."},
        { "category": "REPAIRS", "description": "I'm happy to help with any electrical issues."},
        { "category": "REPAIRS", "description": "I'm happy to help with any carpentry issues."},
        { "category": "SOCIAL", "description": "Always down for a coffee chat!"},
        { "category": "SOCIAL", "description": "Hosting book club! DM me if you want to join."},
        { "category": "SOCIAL", "description": "I'm hosting a board game night this Friday!"},
        { "category": "SCHOOL", "description": "I tutor grade 10 Math."},
        { "category": "SCHOOL", "description": "I tutor grade 10 Science."},
        { "category": "SCHOOL", "description": "I tutor grade 10 Socials."},
        { "category": "UNI", "description": "Happy to peer-review uni essays"},
        { "category": "UNI", "description": "I can help with any coding assignments."}
    ]
    return render_template("requests.html", requests=requestlist)

auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})