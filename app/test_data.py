
from app import db, app
from app.models import *

def initialise_test_database():
    app.app_context().push()

    # drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # add test data
    users = [
        User(username='user1', email='user1@example.com'),
        User(username='user2', email='user2@example.com'),
        User(username='user3', email='user3@example.com'),
        User(username='user4', email='user4@example.com'),
        User(username='user5', email='user5@example.com'),
        User(username='user6', email='user6@example.com'),
        User(username='user7', email='user7@example.com'),
        User(username='user8', email='user8@example.com'),
        User(username='user9', email='user9@example.com'),
        User(username='user10', email='user10@example.com')
    ]

    for user in users:
        user.set_password('password')

    db.session.add_all(users)



    db.session.add_all([
        Activity(author_id=1, type='Offer', category='Programming', description='Python programming task'),
        Activity(author_id=2, type='Request', category='Web Development', description='Build a website'),
        Activity(author_id=3, type='Offer', category='Data Analysis', description='Analyze sales data'),
        Activity(author_id=4, type='Request', category='Machine Learning', description='Train a model'),
        Activity(author_id=5, type='Offer', category='Mobile App Development', description='Develop an Android app'),
        Activity(author_id=6, type='Request', category='Database Management', description='Optimize database queries'),
        Activity(author_id=7, type='Offer', category='UI/UX Design', description='Design a user-friendly interface'),
        Activity(author_id=8, type='Request', category='Software Testing', description='Write test cases'),
        Activity(author_id=9, type='Request', category='Cybersecurity', description='Perform a security audit'),
        Activity(author_id=10, type='Offer', category='Cloud Computing', description='Deploy an application on AWS')
    ])

    db.session.add_all([
        Activity(author_id=1, acceptor_id=2, type='Request', category='Web Development', description='Build a website for a small business', status='Pending'),
        Activity(author_id=2, acceptor_id=3, type='Request', category='Data Analysis', description='Perform statistical analysis on sales data', status='Pending'),
        Activity(author_id=3, acceptor_id=4, type='Request', category='Machine Learning', description='Train a model to predict customer churn', status='Pending'),
        Activity(author_id=4, acceptor_id=5, type='Request', category='Mobile App Development', description='Develop an iOS app for a startup', status='Pending'),
        Activity(author_id=5, acceptor_id=6, type='Request', category='Database Management', description='Optimize database queries for a large-scale application', status='Pending'),
        Activity(author_id=6, acceptor_id=7, type='Offer', category='UI/UX Design', description='Design a user-friendly interface for a mobile app', status='Pending'),
        Activity(author_id=7, acceptor_id=8, type='Offer', category='Software Testing', description='Write test cases for a web application', status='Pending'),
        Activity(author_id=8, acceptor_id=9, type='Offer', category='Cybersecurity', description='Perform a security audit on a network infrastructure', status='Pending'),
        Activity(author_id=9, acceptor_id=10, type='Offer', category='Cloud Computing', description='Deploy a scalable web application on AWS', status='Pending'),
        Activity(author_id=10, acceptor_id=1, type='Offer', category='Artificial Intelligence', description='Implement a natural language processing algorithm', status='Pending')
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