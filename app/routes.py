from flask import render_template
from flask import Flask, request, jsonify, redirect, url_for, flash
from urllib.parse import urlsplit
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Activity
from app.forms import OfferRequestForm, LoginForm, SignupForm
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

@login_required
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = OfferRequestForm()
    if form.validate_on_submit():
        # Creating a new Activity instance from the form data
        new_activity = Activity(type=form.type.data, category=form.category.data, description=form.description.data)
        db.session.add(new_activity)
        db.session.commit()
        flash('Your activity has been created!', 'success')
        return redirect(url_for('index'))  # Redirect to the main page
    return render_template('offer_request_form.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Redirect to the index page if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        # Check if the user exists and the password is correct
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
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
    form = SignupForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("signup.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/offers", methods=['GET', 'POST'])
@login_required
def offers():
    if request.method == 'POST':
        search = request.form['search']
        offerlist = Activity.query.filter_by(type='Offer').filter(Activity.description.contains(search) | Activity.category.contains(search)).all()
        offerlist_serializable = [activity.to_dict() for activity in offerlist]
        return jsonify(offerlist_serializable)

    offerlist = Activity.query.filter_by(type='Offer').all()
    return render_template("offers.html",title="All Offers", offers=offerlist)

@app.route("/requests", methods=['GET', 'POST'])
@login_required
def requests():
    if request.method == 'POST':
        search = request.form['search']
        requestlist = Activity.query.filter_by(type='Request').filter(Activity.description.contains(search) | Activity.category.contains(search)).all()
        requestlist_serializable = [activity.to_dict() for activity in requestlist]
        return jsonify(requestlist_serializable)

    requestlist = Activity.query.filter_by(type='Request').all()
    return render_template("requests.html", title="All Requests", requests=requestlist)
