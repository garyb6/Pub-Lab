import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink('Whisky', 5.00, True)

    def test_drink_has_name(self):
        self.assertEqual('Whisky', self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)

    def test_drink_has_alco_status(self):
        self.assertEqual(True, self.drink.alco_status)