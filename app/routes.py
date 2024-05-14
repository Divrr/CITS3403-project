from flask import render_template, request, redirect, url_for, flash, jsonify
from urllib.parse import urlsplit
from flask_login import current_user, login_user, login_required, logout_user
from app import app, db
from app.models import User, Activity
from app.forms import OfferRequestForm, LoginForm, SignupForm
from urllib.parse import urlsplit
from sqlalchemy.orm import aliased

@app.route("/")
@app.route("/index")
@login_required
def index():
    Acceptor = aliased(User)

    # Fetch activities where the current user is the author
    myitems = db.session.query(
        User.email.label('author_email'),
        User.username.label('author_name'),
        Acceptor.email.label('acceptor_email'),
        Acceptor.username.label('acceptor_name'),
        Activity.description,
        Activity.type,
        Activity.acceptor_id
    ).join(User, User.id == Activity.author_id)\
    .outerjoin(Acceptor, Acceptor.id == Activity.acceptor_id)\
    .filter(Activity.author_id == current_user.id)\
    .all()

    # Fetch activities where the current user is the acceptor
    myaccepts = db.session.query(
        User.email.label('author_email'),
        User.username.label('author_name'),
        Activity.description,
        Activity.type,
        Activity.author_id
    ).join(User, User.id == Activity.author_id)\
    .filter(Activity.acceptor_id == current_user.id)\
    .all()

    return render_template("mainpage.html", title="UWA Community Hub", items=myitems, accepts=myaccepts)

@app.route('/form', methods=['GET', 'POST'])
@login_required
def form():
    form = OfferRequestForm()
    if form.validate_on_submit():
        new_activity = Activity(author_id=current_user.id, type=form.type.data, category=form.category.data, description=form.description.data)
        db.session.add(new_activity)
        db.session.commit()
        flash('Your activity has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('offer_request_form.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
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
        flash('Account successfully created!', 'success')
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/offers", methods=['GET', 'POST'])
@login_required
def offers():
    return render_template("offers.html",title="All Offers")

@app.route("/requests", methods=['GET', 'POST'])
@login_required
def requests():
    return render_template("requests.html",title="All Requests")
    
@app.route('/search')
def search():
    search = request.args.get('search')
    searchtype = request.referrer.split('/')[-1] == 'offers' and 'Offer' or 'Request'
    offerlist = Activity.query.filter_by(type=searchtype).filter(Activity.description.contains(search) | Activity.category.contains(search)).all()
    rendered_results = [render_template('searchboxitem.html', item=item) for item in offerlist]
    return ''.join(rendered_results)