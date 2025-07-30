import unittest
from app import create_app, db
from flask.testing import FlaskClient

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client: FlaskClient = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_register_and_login(self):
        payload = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        res = self.client.post("/api/auth/register", json=payload)
        self.assertEqual(res.status_code, 201)

        login = self.client.post("/api/auth/login", json={
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(login.status_code, 200)
        self.assertIn("token", login.get_json())
