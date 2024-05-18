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

    def test_accept_request(self):
        activity = Activity(author_id=1, type='Request', category='Web Development', description='Build a website for a small business')
        db.session.add(activity)
        db.session.commit()

        retrieved_activity = Activity.query.filter_by(description='Build a website for a small business').first()
        self.assertEqual(retrieved_activity.author_id, 1)
        self.assertEqual(retrieved_activity.type, 'Request')
        self.assertEqual(retrieved_activity.category, 'Web Development')

class TestJQueryConnection(TestCase):
    def setUp(self):
        self.url = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"

    def test_connection(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.content), 0)
        except requests.exceptions.RequestException as e:
            self.fail(f"Connection failed: {e}")

class TestBootstrapConnection(TestCase):
    def setUp(self):
        self.url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"

    def test_connection(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.content), 0)
        except requests.exceptions.RequestException as e:
            self.fail(f"Connection failed: {e}")
    

if __name__ == '__main__':
    unittest.main()