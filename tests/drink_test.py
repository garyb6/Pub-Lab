import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink('Whisky', 5.00, True, 1.00)

    def test_drink_has_name(self):
        self.assertEqual('Whisky', self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)

    def test_drink_has_alco_status(self):
        self.assertEqual(True, self.drink.alco_status)
    
    #def test_drink_has_alcoholic_status__True(self):
        # self.assertEqual(True, self.drink.alco_status)
    
    #def test_drink_has_alcoholic_status__False(self):
        # drink1 = Drink("Irn Bru", 2, False)
        # self.assertEqual(False, self.drink.alco_status)
    
    #should double check each boolean passes - this can be done in one test but give yourself an extra test pass!!
    
    def test_drink_has_units(self):
        self.assertEqual(1.00, self.drink.units)