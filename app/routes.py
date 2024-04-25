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

auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})