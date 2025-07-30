import unittest
from app import create_app, db
from app.models.user import User
from app.utils.jwt_handler import generate_token

class AnalyticsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.admin = User(username="admin", email="admin@admin.com", password="123", role="admin")
            db.session.add(self.admin)
            db.session.commit()
            self.token = generate_token(self.admin)

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_get_order_stats(self):
        res = self.client.get("/api/analytics/orders", headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(res.status_code, 200)
