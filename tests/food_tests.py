import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Crisps", 1.00, 0.5)
    
    def test_food_has_name(self):
        self.assertEqual('Crisps', self.food.name)

    def test_food_has_price(self):
        self.assertEqual(1.00, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(0.5, self.food.rejuvenation_level) 
    
    