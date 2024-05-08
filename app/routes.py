from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Activity
from app import app, db

@app.route("/")
@app.route("/index")
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    myitems = [
        { "email": "zahravink@gmail.com", "content": "Can someone mow my lawn?", "name": "Joe", "type": "Request"},
        { "email": "zahravink@gmail.com", "content": "I can teach you to bake cookies", "name": "Youssef", "type": "Offer"}
    ]
    myaccepts = [
        { "email": "zahravink@gmail.com", "content": "Can someone give a 30min crash course on Flask?", "name": "Zahra", "type": "Request"},
        { "email": "zahravink@gmail.com", "content": "I can fix a garborator", "name": "May", "type": "Offer"}
    ]
    return render_template("mainpage.html", items=myitems, accepts=myaccepts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.')
            return redirect(url_for('signup'))
        new_user = User(username=username, email=email, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully, please login.')
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route("/offers")
def offers():
    offerlist = Activity.query.filter_by(type='Offer').all()
    return render_template("offers.html", offers=offerlist)

@app.route("/requests")
def requests():
    requestlist = Activity.query.filter_by(type='Request').all()
    return render_template("requests.html", requests=requestlist)

@app.route("/form")
def form():
    from app.forms import OfferRequestForm
    form_object = OfferRequestForm()
    return render_template("offer_request_form.html", form=form_object)
