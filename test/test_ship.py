import unittest
from src.class_ship import ship

class Test1 (unittest.TestCase):
    def test_calculateweight(self):
       barco= ship(1200,500)
       assert barco.calculate_weight()== 450

