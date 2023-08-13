import unittest
from src.class_cargo import cargo


class Test1 (unittest.TestCase):
    def test_calculateweight(self):
        Cargo=cargo(1, 0.5, 1200, 500)
        assert Cargo.calculate_weight() == 449.5


