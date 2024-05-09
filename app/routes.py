from flask import render_template
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Activity
from app.forms import OfferRequestForm, LoginForm, SigninForm
from app import app, db

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

@app.route("/form")
def form():
    form_object = OfferRequestForm()
    return render_template("offer_request_form.html", title="Create an Offer or Request", form=form_object)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                render_template("mainpage.html") #this leads after login #### this used to be login_user(user) #### it doesn't make difference
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