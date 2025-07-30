import unittest
from app import create_app, db
from app.models.user import User
from app.utils.jwt_handler import generate_token

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.user = User(username="test", email="test@test.com", password="pass")
            self.admin = User(username="admin", email="admin@test.com", password="pass", role="admin")
            db.session.add_all([self.user, self.admin])
            db.session.commit()
            self.token = generate_token(self.user)
            self.admin_token = generate_token(self.admin)

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_get_own_profile(self):
        res = self.client.get("/api/users/me", headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(res.status_code, 200)

    def test_get_all_users_admin(self):
        res = self.client.get("/api/users/", headers={"Authorization": f"Bearer {self.admin_token}"})
        self.assertEqual(res.status_code, 200)
