import unittest
from app import create_app, db, app
from app.models import User, Activity
from config import TestConfig

class BootstrapUnitTest(unittest.TestCase):

    def setUp(self):
        app = create_app(TestConfig)
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_test_data(self):
        # Add test users
        users = [
            User(username='user1', email='user1@example.com'),
            User(username='user2', email='user2@example.com'),
            User(username='user3', email='user3@example.com')
        ]
        for user in users:
            user.set_password('password')
            db.session.add(user)

        # Add test activities
        activities = [
            Activity(author_id=1, type='Offer', category='Programming', description='Python programming task'),
            Activity(author_id=2, type='Request', category='Web Development', description='Build a website'),
            Activity(author_id=3, type='Offer', category='Data Analysis', description='Analyze sales data')
        ]
        db.session.add_all(activities)

        db.session.commit()

    def test_user_creation(self):
        user = User.query.filter_by(username='user1').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'user1@example.com')

    def test_activity_creation(self):
        activity = Activity.query.filter_by(description='Python programming task').first()
        self.assertIsNotNone(activity)
        self.assertEqual(activity.author_id, 1)
        self.assertEqual(activity.type, 'Offer')
        self.assertEqual(activity.category, 'Programming')

if __name__ == '__main__':
    unittest.main()