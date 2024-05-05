from flask import render_template
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from app.models import User, Activity
from app import app, db

@app.route("/")
@app.route("/index")
def index():
    return render_template("mainpage.html")

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