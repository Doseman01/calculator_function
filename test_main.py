# test_main.py

import unittest
from main import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()

