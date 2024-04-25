import unittest
import json
from app import app, carts, purchases, discounts

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_add_to_cart(self):
        # Test adding items to cart
        user_id = 1
        item = 'product1'
        response = self.app.post('/api/add-to-cart', json={'user_id': user_id, 'item': item})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Item added to cart successfully')
        self.assertIn(user_id, carts)
        self.assertEqual(carts[user_id], [item])

    def test_view_empty_cart(self):
        # Test viewing an empty cart
        user_id = 2
        response = self.app.get(f'/api/view-cart?user_id={user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Cart is empty'})

    def test_view_non_empty_cart(self):
        # Test viewing a non-empty cart
        user_id = 1
        expected_cart_items = ['product1', 'product2']
        carts[user_id] = expected_cart_items
        response = self.app.get(f'/api/view-cart?user_id={user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['cart_items'], expected_cart_items)

    def test_checkout_empty_cart(self):
        # Test checking out an empty cart
        user_id = 3
        response = self.app.post('/api/checkout', json={'user_id': user_id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Cart is empty'})

    def test_checkout_non_empty_cart(self):
        # Test checking out a non-empty cart
        user_id = 1
        cart_items = ['product1', 'product2']
        carts[user_id] = cart_items
        response = self.app.post('/api/checkout', json={'user_id': user_id})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Checkout successful')
        self.assertEqual(data['total_amount'], len(cart_items) * 10)
        self.assertIn('DISCOUNT', data['discount_code'])

    def test_purchase_statistics(self):
        # Test purchase statistics API
        purchases.append({'user_id': 1, 'items': ['product1', 'product2'], 'total_amount': 20})
        discounts['DISCOUNT5'] = 2

        response = self.app.get('/api/purchase-statistics')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
