import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer 

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink('Whisky', 5.00, True)
        self.drink2 = Drink('Irn Bru', 2.00, False)
        self.drink3 = Drink('Beer', 4.00, True)
        self.pub = Pub('The Prancing Pony', 100.00, [self.drink1, self.drink2, self.drink3])
       
    def test_pub_has_name(self):
        self.assertEqual('The Prancing Pony', self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_check_till_amount(self):
        self.assertEqual(100.00, self.pub.check_till())

    def test_pub_has_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))

    def test_pub_drink_list(self):
        self.assertEqual(self.pub.drinks, self.pub.drinks_list())

    def test_pub_finds_drink(self):
        self.assertEqual(self.drink2, self.pub.find_drink_by_name('Irn Bru'))
        self.assertEqual(None, self.pub.find_drink_by_name('Water'))

    def test_pub_can_remove_drink(self):
        self.pub.remove_drink('Whisky')
        self.assertEqual(2, len(self.pub.drinks))
        self.assertEqual(False, self.drink1 in self.pub.drinks)

    def test_get_id(self):
        self.customer_young = Customer("JP O'Reilly", [], 10.00, 17)
        self.customer_old = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27)
        self.assertEqual (False, self.pub.get_id (self.customer_young))
        self.assertEqual (True, self.pub.get_id (self.customer_old))

    def test_pub_can_sell_drink_old_alco(self):
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27)
        self.pub.sell_drink(self.customer, 'Beer')
        self.assertEqual(3, len(self.customer.stomach))
        self.assertEqual(2.00, self.customer.wallet)
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(False, self.drink3 in self.pub.drinks)

    def test_pub_can_sell_drink_old_soft(self):
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27)
        self.pub.sell_drink(self.customer, 'Irn Bru')
        self.assertEqual(3, len(self.customer.stomach))
        self.assertEqual(4.00, self.customer.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(False, self.drink2 in self.pub.drinks)

    def test_pub_can_sell_drink_young_alco(self):
        self.customer = Customer("JP O'Reilly", [], 10.00, 17)
        self.pub.sell_drink(self.customer, 'Beer')
        self.assertEqual(0, len(self.customer.stomach))
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(True, self.drink3 in self.pub.drinks)

    def test_pub_can_sell_drink_young_soft(self):
        self.customer = Customer("JP O'Reilly", [], 10.00, 17)
        self.pub.sell_drink(self.customer, 'Irn Bru')
        self.assertEqual(1, len(self.customer.stomach))
        self.assertEqual(8.00, self.customer.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(False, self.drink2 in self.pub.drinks)

    def test_pub_can_sell_drink_too_poor(self):
        self.customer = Customer("JP O'Reilly", [], 1.00, 30)
        self.pub.sell_drink(self.customer, 'Beer')
        self.assertEqual(0, len(self.customer.stomach))
        self.assertEqual(1.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(True, self.drink3 in self.pub.drinks)
