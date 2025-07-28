import unittest
from app import app

class ProductAPITest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_create_product(self):
        response = self.app.post('/products', json={
            'name': 'Laptop',
            'description': 'Gaming Laptop',
            'price': 1200,
            'category': 'electronics', 
            'image_url': 'https://example.com/laptop.jpg'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product created', response.json['message'])

if __name__ == '__main__':
    unittest.main()
