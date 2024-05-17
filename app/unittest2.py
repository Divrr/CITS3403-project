from unittest import TestCase

from app import create_app, db
from config import TestConfig
from app.models import User, Activity

class DatabaseUnitTest(TestCase):

    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username='test_user', email='test_user@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(username='test_user').first()
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.email, 'test_user@example.com')

    def test_activity_creation(self):
        activity = Activity(author_id=1, type='Offer', category='Programming', description='Python programming task')
        db.session.add(activity)
        db.session.commit()

        retrieved_activity = Activity.query.filter_by(description='Python programming task').first()
        self.assertEqual(retrieved_activity.author_id, 1)
        self.assertEqual(retrieved_activity.type, 'Offer')
        self.assertEqual(retrieved_activity.category, 'Programming')

if __name__ == '__main__':
    unittest.main()