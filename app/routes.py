from flask import render_template
from flask import Flask, request, jsonify

from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("mainpage.html")

@app.route("/login")
def login():
    return render_template("login.html")

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

auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})