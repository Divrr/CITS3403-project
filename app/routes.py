from flask import render_template, redirect, url_for, flash
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from app.models import User, Activity
from app.forms import OfferRequestForm
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
    return render_template("mainpage.html", items=myitems, accepts=myaccepts)

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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/offers")
def offers():
    offerlist = Activity.query.filter_by(type='Offer').all()
    print(offerlist)
    return render_template("offers.html", offers=offerlist)

@app.route("/requests")
def requests():
    requestlist = Activity.query.filter_by(type='Request').all()
    print(request)
    return render_template("requests.html", requests=requestlist)

auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})