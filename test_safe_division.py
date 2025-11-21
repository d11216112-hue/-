"""
Unit tests for the safe_division function.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for safe_division function"""
    
    def test_normal_division(self):
        """Test normal division operations"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(9, 3), 3.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_division_by_zero(self):
        """Test that division by zero returns None"""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(0, 0))
        self.assertIsNone(safe_division(-5, 0))
    
    def test_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_zero_numerator(self):
        """Test division with zero as numerator"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -3), 0.0)
    
    def test_float_numbers(self):
        """Test division with floating point numbers"""
        self.assertAlmostEqual(safe_division(10.5, 2.5), 4.2)
        self.assertAlmostEqual(safe_division(7.7, 2.2), 3.5, places=1)
    
    def test_large_numbers(self):
        """Test division with large numbers"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999, 3), 333333.0)


if __name__ == '__main__':
    unittest.main()
