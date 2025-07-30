import unittest
from app import create_app, db
from app.models.user import User, Product
from app.utils.jwt_handler import generate_token

class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.user = User(username="test", email="user@test.com", password="123")
            db.session.add(self.user)

            product = Product(name="TV", category="Appliances", price=300.00, description="Smart TV", image_url="")
            db.session.add(product)
            db.session.commit()

            self.token = generate_token(self.user)
            self.product_id = product.id

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_place_order(self):
        res = self.client.post("/api/orders/", json={
            "address": "123 Street",
            "billing_info": "Visa",
            "items": [{"product_id": self.product_id, "quantity": 2, "price": 300.00}]
        }, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(res.status_code, 201)
