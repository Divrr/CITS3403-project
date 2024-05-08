from flask import render_template
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from app.models import User, Activity
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

from app.forms import OfferRequestForm
@app.route("/form")
def form():
    form_object = OfferRequestForm()
    return render_template("offer_request_form.html", title="Create an Offer or Request", form=form_object)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/offers", methods=['GET', 'POST'])
def offers():
    if request.method == 'POST':
        search = request.form['search']
        offerlist = Activity.query.filter_by(type='Offer').filter(Activity.description.contains(search) | Activity.category.contains(search)).all()
        offerlist_serializable = [activity.to_dict() for activity in offerlist]
        return jsonify(offerlist_serializable)

    offerlist = Activity.query.filter_by(type='Offer').all()
    return render_template("offers.html",title="All Offers", offers=offerlist)

@app.route("/requests", methods=['GET', 'POST'])
def requests():
    if request.method == 'POST':
        search = request.form['search']
        requestlist = Activity.query.filter_by(type='Request').filter(Activity.description.contains(search) | Activity.category.contains(search)).all()
        requestlist_serializable = [activity.to_dict() for activity in requestlist]
        return jsonify(requestlist_serializable)

    requestlist = Activity.query.filter_by(type='Request').all()
    return render_template("requests.html", title="All Requests", requests=requestlist)

auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})