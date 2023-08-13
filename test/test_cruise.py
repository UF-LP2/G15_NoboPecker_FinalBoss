import unittest
import pytest
from library import class_ship

class MyTestCase(unittest.TestCase):
    barco=ship(45,5)
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
