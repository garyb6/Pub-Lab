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