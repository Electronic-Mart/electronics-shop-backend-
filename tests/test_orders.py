import unittest
from app import app
from backend.models.db import db
from backend.models.user import User, Roletype
from backend.models.order import Order

class OrderAPITest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.drop_all()
            db.create_all()

            test_user = User(
                name="Test User",
                email="test@example.com",
                role=Roletype.customer,
                password_hash="hashed_password"
            )
            db.session.add(test_user)
            db.session.commit()
            self.test_user_id = test_user.id

    def test_create_order(self):
        response = self.app.post('/orders', json={
            'user_id': self.test_user_id,
            'total': 250.00,
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order created', response.json['message'])

    def test_get_orders(self):
        with app.app_context():
            order = Order(user_id=self.test_user_id, total=150.00, status='pending')
            db.session.add(order)
            db.session.commit()

        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertIn('orders', response.json)
        self.assertEqual(len(response.json['orders']), 1)

    def test_update_order(self):
        with app.app_context():
            order = Order(user_id=self.test_user_id, total=200.00, status='pending')
            db.session.add(order)
            db.session.commit()
            order_id = order.id

        response = self.app.put(f'/orders/{order_id}', json={
            'status': 'shipped'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Order updated', response.json['message'])

    def test_delete_order(self):
        with app.app_context():
            order = Order(user_id=self.test_user_id, total=300.00, status='cancelled')
            db.session.add(order)
            db.session.commit()
            order_id = order.id

        response = self.app.delete(f'/orders/{order_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Order deleted', response.json['message'])

if __name__ == '__main__':
    unittest.main()
