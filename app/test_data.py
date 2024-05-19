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

    activities = [
        Activity(author_id=1, type='Offer', category='Community Gardening', description='Help maintain a community garden and grow fresh produce for local residents!'),
        Activity(author_id=2, type='Request', category='Language Exchange', description='Looking for language partner to practice speaking Spanish'),
        Activity(author_id=3, type='Offer', category='Art', description='Can host a painting workshop for children in the local community center'),
        Activity(author_id=4, type='Request', category='Fitness', description='Looking for a workout partner to motivate each other and achieve fitness goals'),
        Activity(author_id=5, type='Offer', category='Photography', description='Offering professional photography services for events and portraits'),
        Activity(author_id=6, type='Request', category='Music', description='Any music teachers for singing?'),
        Activity(author_id=7, type='Request', category='Animal Shelter', description='Come find opportunities to help at a local animal shelter'),
        Activity(author_id=8, type='Request', category='Community Clean-up', description='Organize a clean-up event to keep the neighborhood clean and beautiful'),
        Activity(author_id=9, type='Offer', category='Meditation', description='I can teach meditation for stress relief and relaxation'),
        Activity(author_id=10, type='Offer', category='Cooking', description='Offering cooking lessons for beginners'),
        Activity(author_id=1, type='Request', category='Sports', description='Looking for a tennis partner to play on weekends'),
        Activity(author_id=2, type='Offer', category='Writing', description='Can provide editing and proofreading services for written documents'),
        Activity(author_id=3, type='Request', category='Technology', description='Seeking help with computer programming assignments'),
        Activity(author_id=4, type='Offer', category='Gardening', description='Can help with landscaping and garden maintenance'),
        Activity(author_id=5, type='Request', category='Dance', description='Looking for a dance instructor for salsa lessons'),
        Activity(author_id=6, type='Offer', category='Volunteering', description='Volunteering at a local charity organization'),
        Activity(author_id=7, type='Request', category='Fitness', description='Seeking a personal trainer for customized workout plans'),
        Activity(author_id=8, type='Offer', category='Photography', description='Offering wedding photography services'),
        Activity(author_id=9, type='Request', category='Music', description='Looking for a guitar teacher for beginners'),
        Activity(author_id=10, type='Offer', category='Art', description='Can create custom artwork and paintings'),
        Activity(author_id=1, type='Request', category='Language Exchange', description='Looking for a language partner to practice speaking French'),
        Activity(author_id=2, type='Offer', category='Cooking', description='Offering catering services for events'),
        Activity(author_id=3, type='Request', category='Fitness', description='Seeking a running buddy for regular jogging sessions'),
        Activity(author_id=4, type='Offer', category='Technology', description='Can provide technical support and troubleshooting for computers'),
        Activity(author_id=5, type='Request', category='Gardening', description='Looking for gardening tips and advice'),
        Activity(author_id=6, type='Offer', category='Writing', description='Offering ghostwriting services for books and articles'),
        Activity(author_id=7, type='Request', category='Art', description='Looking for an art teacher for drawing lessons'),
        Activity(author_id=8, type='Offer', category='Music', description='Can provide piano lessons for beginners'),
        Activity(author_id=9, type='Request', category='Language Exchange', description='Looking for a language partner to practice speaking German'),
        Activity(author_id=10, type='Offer', category='Fitness', description='Offering online fitness coaching and workout plans'),
        Activity(author_id=1, type='Request', category='Technology', description='Seeking help with setting up a home network'),
        Activity(author_id=2, type='Offer', category='Gardening', description='Can help with vegetable gardening and organic farming'),
        Activity(author_id=3, type='Request', category='Dance', description='Looking for a dance partner for ballroom dancing'),
        Activity(author_id=4, type='Offer', category='Volunteering', description='Volunteering at a local homeless shelter'),
        Activity(author_id=5, type='Request', category='Fitness', description='Seeking a yoga instructor for private sessions'),
        Activity(author_id=6, type='Offer', category='Photography', description='Offering portrait photography services'),
        Activity(author_id=7, type='Request', category='Music', description='Looking for a violin teacher for intermediate level'),
        Activity(author_id=8, type='Offer', category='Art', description='Can provide art commissions and custom illustrations')
    ]


    for i in range(10):
        activities[i].acceptor_id = ((i-1) % 5) + 1
        activities[i].status = 'Pending'
    
    db.session.add_all(activities)

    # Commit the changes to the database
    db.session.commit()

initialise_test_database()
print('Test database initialised! You can exit the program now (exit() or Ctrl+D)')