import unittest
#import pytest
from src.class_cruise import cruise


class Test1 (unittest.TestCase):
    def test_calculateweight(self):
        crucero = cruise(100, 1200, 50)
        assert crucero.calculate_weight() == 900


