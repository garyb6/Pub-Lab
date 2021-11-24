import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = ("Crisps", 1.00, 0.5)