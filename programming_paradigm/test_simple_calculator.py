# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance for testing."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, 10), 0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))  # Test division by zero

    def test_edge_cases(self):
        """Test edge cases for all methods."""
        # Large numbers
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.subtract(1e10, 1e9), 9e9)
        self.assertEqual(self.calc.multiply(1e5, 1e5), 1e10)
        self.assertEqual(self.calc.divide(1e10, 1e5), 1e5)

        # Small numbers
        self.assertAlmostEqual(self.calc.add(1e-10, 1e-10), 2e-10)
        self.assertAlmostEqual(self.calc.subtract(1e-10, 1e-11), 9e-11)
        self.assertAlmostEqual(self.calc.multiply(1e-5, 1e-5), 1e-10)
        self.assertAlmostEqual(self.calc.divide(1e-10, 1e-5), 1e-5)

if __name__ == "__main__":
    unittest.main()
