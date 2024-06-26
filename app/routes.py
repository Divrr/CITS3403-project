from flask import render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import current_user, login_user, login_required, logout_user
from app import app, db
from app.models import User, Activity
from app.forms import OfferRequestForm, LoginForm, SignupForm, EmptyForm
from sqlalchemy.orm import aliased
from urllib.parse import urlsplit

@app.route("/")
@app.route("/index")
@login_required
def index():
    Acceptor = aliased(User)

    myitems = db.session.query(
        User.email.label('author_email'),
        User.username.label('author_name'),
        Acceptor.email.label('acceptor_email'),
        Acceptor.username.label('acceptor_name'),
        Activity.id,
        Activity.description,
        Activity.type,
        Activity.acceptor_id
    ).join(User, User.id == Activity.author_id)\
    .outerjoin(Acceptor, Acceptor.id == Activity.acceptor_id)\
    .filter(Activity.author_id == current_user.id, Activity.status != 'Closed')\
    .all()

    myaccepts = db.session.query(
        User.email.label('author_email'),
        User.username.label('author_name'),
        Activity.id,
        Activity.description,
        Activity.type,
        Activity.author_id
    ).join(User, User.id == Activity.author_id)\
    .filter(Activity.acceptor_id == current_user.id, Activity.status != 'Closed')\
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
    return render_template('offer_request_form.html', form=form, title="Offer Request Form")

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
        session['show_welcome'] = True
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="UWA Community Hub", form=form)

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
    return render_template("signup.html", title="UWA Community Hub", form=form)

@app.route('/logout')
def logout():
    logout_user()
    session.pop('show_welcome', None)
    return redirect(url_for('index'))

@app.route("/offers", methods=['GET', 'POST'])
@login_required
def offers():
    return render_template("offers.html", title="All Offers")

@app.route("/requests", methods=['GET', 'POST'])
@login_required
def requests():
    return render_template("requests.html", title="All Requests")

@app.route('/search')
def search():
    search = request.args.get('search')
    searchtype = request.referrer.split('/')[-1] == 'offers' and 'Offer' or 'Request'
    itemlist = Activity.query.filter_by(type=searchtype, status="Open").filter(Activity.description.contains(search) | Activity.category.contains(search)).all()

    form = EmptyForm()
    rendered_results = [render_template('searchboxitem.html', item=item, form=form) for item in itemlist]
    return ''.join(rendered_results)

@app.route('/clear_welcome_flag', methods=['POST'])
def clear_welcome_flag():
    session.pop('show_welcome', None)
    return '', 204

@app.route("/accept/<activity_id>", methods=['POST'])
def accept(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    
    if activity is None:
        print("Activity not found")
        return jsonify({'error': 'Activity not found'}), 403
    
    if activity.status != "Open":
        print("Activity not open for acceptance")
        return jsonify({'error': 'Activity not open for acceptance'}), 403
    
    if activity.author_id == current_user.id:
        print("You cannot accept your own activity")
        return jsonify({'error': 'You cannot accept your own activity'}), 403

    if current_user.has_accepted(activity):
        print("You have already accepted this activity'")
        return jsonify({'error': 'You have already accepted this activity'}), 403
        
    # Check if the user has accepted 5 activities already (the maximum number of accepted activities allowed)
    ActivityCount = Activity.query.filter_by(acceptor_id=current_user.id).count()
    if ActivityCount >= 5:
        print("Activity not open for acceptance")
        return jsonify({'error': 'You have already accepted the maximum number of activities allowed (5).'}), 403
        
    current_user.accept(activity)
    db.session.commit()
    return jsonify({'success': 'Accepted activity: ' + Activity.query.get(activity_id).description}), 200

@app.route('/resolve/<int:activity_id>', methods=['POST'])
@login_required
def resolve(activity_id):
    print(f"Attempting to resolve activity with id: {activity_id}")
    activity = Activity.query.get_or_404(activity_id)
    if activity.author_id != current_user.id:
        print("Unauthorized attempt to resolve activity.")
        return jsonify({'error': 'Unauthorized'}), 403
    
    current_user.resolve(activity)
    db.session.commit()
    print(f"Activity with id: {activity_id} marked as resolve.")
    return jsonify({'success': 'Activity marked as resolve'}), 200

@app.route("/cancel/<int:activity_id>", methods=['POST'])
@login_required
def cancel(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    
    if activity.acceptor_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    current_user.cancel(activity)
    db.session.commit()
    return jsonify({'success': 'Activity acceptance canceled'}), 200