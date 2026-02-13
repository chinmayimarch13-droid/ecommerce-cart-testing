import unittest
from cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_add_item(self):
        self.assertEqual(self.cart.add_item(500), "Item added")

    def test_invalid_price(self):
        self.assertEqual(self.cart.add_item(-10), "Invalid price")

    def test_calculate_total(self):
        self.cart.add_item(200)
        self.cart.add_item(300)
        self.assertEqual(self.cart.calculate_total(), 500)

    def test_discount(self):
        self.cart.add_item(1000)
        self.assertEqual(self.cart.apply_discount(10), 900)

if __name__ == "__main__":
    unittest.main()
