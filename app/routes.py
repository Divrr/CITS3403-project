from flask import render_template
from flask import Flask, request, jsonify, redirect, url_for
from urllib.parse import urlsplit
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Activity
from app.forms import OfferRequestForm, LoginForm, SigninForm
from app import app, db

@app.route("/")
@app.route("/index")
@login_required
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

@app.route("/form")
@login_required
def form():
    form_object = OfferRequestForm()
    return render_template("offer_request_form.html", title="Create an Offer or Request", form=form_object)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Redirect to the index page if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        # Check if the user exists and the password is correct
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        
        # Redirect to the next page if it exists, otherwise redirect to the index page
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template("login.html", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SigninForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("signup.html", form=form)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/offers")
@login_required
def offers():
    offerlist = Activity.query.filter_by(type='Offer').all()
    print(offerlist)
    return render_template("offers.html", title="All Offers", offers=offerlist)

@app.route("/requests")
@login_required
def requests():
    requestlist = Activity.query.filter_by(type='Request').all()
    print(request)
    return render_template("requests.html", title="All Requests", requests=requestlist)