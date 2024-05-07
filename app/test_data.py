
from app import db, app
from app.models import *

# Hello! This is a script to generate test data for the database.
# It will create 10 users and 20 activities.
# Each user will have 2 activities, one authored and one accepted.
# The activities are be randomly distributed between requests and offers.

# To run this script, execute the following commands in the terminal:
# (assuming you have flask, flask-migrate and flask-sqlalchemy installed in your virtual environment)
# $ flask db upgrade
# flask shell
# >>> exec(open('app/test_data.py').read())

# --- Test Data Generation ---
# drop all tables and recreate them

def initialise_test_database():
    app.app_context().push()
    db.drop_all()
    db.create_all()

    db.session.add_all([
        User(username='user1', email='user1@example.com', password_hash='password1'),
        User(username='user2', email='user2@example.com', password_hash='password2'),
        User(username='user3', email='user3@example.com', password_hash='password3'),
        User(username='user4', email='user4@example.com', password_hash='password4'),
        User(username='user5', email='user5@example.com', password_hash='password5'),
        User(username='user6', email='user6@example.com', password_hash='password6'),
        User(username='user7', email='user7@example.com', password_hash='password7'),
        User(username='user8', email='user8@example.com', password_hash='password8'),
        User(username='user9', email='user9@example.com', password_hash='password9'),
        User(username='user10', email='user10@example.com', password_hash='password10')
    ])

    db.session.add_all([
        Activity(author_id=1, type='Offer', category='Category1', description='Description1'),
        Activity(author_id=2, type='Request', category='Category2', description='Description2'),
        Activity(author_id=3, type='Offer', category='Category3', description='Description3'),
        Activity(author_id=4, type='Request', category='Category4', description='Description4'),
        Activity(author_id=5, type='Offer', category='Category5', description='Description5'),
        Activity(author_id=6, type='Request', category='Category6', description='Description6'),
        Activity(author_id=7, type='Offer', category='Category7', description='Description7'),
        Activity(author_id=8, type='Request', category='Category8', description='Description8'),
        Activity(author_id=9, type='Request', category='Category9', description='Description9'),
        Activity(author_id=10, type='Offer', category='Category10', description='Description10')
    ])

    db.session.add_all([
        Activity(author_id=1, acceptor_id=2, type='Request', category='Category11', description='Description11'),
        Activity(author_id=2, acceptor_id=3, type='Request', category='Category12', description='Description12'),
        Activity(author_id=3, acceptor_id=4, type='Request', category='Category13', description='Description13'),
        Activity(author_id=4, acceptor_id=5, type='Request', category='Category14', description='Description14'),
        Activity(author_id=5, acceptor_id=6, type='Request', category='Category15', description='Description15'),
        Activity(author_id=6, acceptor_id=7, type='Request', category='Category16', description='Description16'),
        Activity(author_id=7, acceptor_id=8, type='Request', category='Category17', description='Description17'),
        Activity(author_id=8, acceptor_id=9, type='Request', category='Category18', description='Description18'),
        Activity(author_id=9, acceptor_id=10, type='Request', category='Category19', description='Description19'),
        Activity(author_id=10, acceptor_id=1, type='Request', category='Category20', description='Description20')
    ])

    db.session.commit()

    # retrieve data
    users = User.query.all()
    activities = Activity.query.all()

    # print data
    print('Users (id, username, email, password_hash):')
    for user in users:
        print(user.id , user.username, user.email, user.password_hash)

    print('\nActivities (id, author_id, acceptor_id, type, category, description):')
    for activity in activities:
        print(activity.id, activity.author_id, activity.acceptor_id, activity.type, activity.category, activity.description)

    print('\nDone! Test data has been generated. You can now run the app now!')