import unittest
from app import create_app, db
from app.models.user import User
from app.utils.jwt_handler import generate_token

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.admin = User(username="admin", email="admin@example.com", password="1234", role="admin")
            db.session.add(self.admin)
            db.session.commit()
            self.token = generate_token(self.admin)

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_add_product(self):
        res = self.client.post("/api/products/", json={
            "name": "Test Product",
            "category": "Laptops",
            "description": "Powerful laptop",
            "price": 999.99,
            "image_url": "http://example.com/img.png"
        }, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(res.status_code, 201)

    def test_get_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)

