import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink('Whisky', 5.00, True)
        self.drink2 = Drink('Whisky', 5.00, True)
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 2.00)
        
    def test_customer_has_name(self):
        self.assertEqual("Stephen O'Reilly", self.customer.name)

    def test_customer_has_stomach(self):
        self.assertEqual(2, len(self.customer.stomach))

    def test_customer_has_wallet(self):
        self.assertEqual(2.00, self.customer.wallet)