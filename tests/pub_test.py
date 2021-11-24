import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink('Whisky', 5.00, True)
        self.drink2 = Drink('Irn Bru', 1.99, False)
        self.pub = Pub('The Prancing Pony', 100.00, [self.drink1, self.drink2])
       
    def test_pub_has_name(self):
        self.assertEqual('The Prancing Pony', self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))

    def test_pub_finds_drink(self):
        self.assertEqual(self.drink2, self.pub.find_drink_by_name('Irn Bru'))
        self.assertEqual(None, self.pub.find_drink_by_name('Water'))

    def test_pub_can_remove_drink(self):
        self.pub.remove_drink('Whisky')
        self.assertEqual(1, len(self.pub.drinks))
        self.assertEqual(False, self.drink1 in self.pub.drinks)