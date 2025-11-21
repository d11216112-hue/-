"""
safe_division 函數的單元測試
使用 Python 標準庫 unittest 進行測試
"""

import unittest
from calculator import safe_division


class TestSafeDivision(unittest.TestCase):
    """safe_division 函數的測試類"""
    
    def test_normal_division_positive_numbers(self):
        """測試：正常的正數除法"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(100, 4), 25.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_normal_division_negative_numbers(self):
        """測試：負數除法"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_with_float_numbers(self):
        """測試：浮點數除法"""
        self.assertAlmostEqual(safe_division(10.5, 2.5), 4.2)
        self.assertAlmostEqual(safe_division(7.5, 1.5), 5.0)
        self.assertAlmostEqual(safe_division(3.14, 2), 1.57)
    
    def test_division_resulting_in_decimal(self):
        """測試：結果為小數的除法"""
        self.assertAlmostEqual(safe_division(1, 3), 0.333333, places=5)
        self.assertAlmostEqual(safe_division(2, 3), 0.666666, places=5)
        self.assertAlmostEqual(safe_division(5, 6), 0.833333, places=5)
    
    def test_division_by_one(self):
        """測試：除以1"""
        self.assertEqual(safe_division(42, 1), 42.0)
        self.assertEqual(safe_division(-42, 1), -42.0)
        self.assertEqual(safe_division(0, 1), 0.0)
    
    def test_zero_divided_by_number(self):
        """測試：0除以任意數"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -5), 0.0)
        self.assertEqual(safe_division(0, 100), 0.0)
    
    def test_division_by_zero_raises_value_error(self):
        """測試：除以0應該拋出 ValueError"""
        with self.assertRaises(ValueError) as context:
            safe_division(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
        
        with self.assertRaises(ValueError):
            safe_division(-10, 0)
        
        with self.assertRaises(ValueError):
            safe_division(0, 0)
    
    def test_invalid_dividend_type_raises_type_error(self):
        """測試：被除數類型錯誤應該拋出 TypeError"""
        with self.assertRaises(TypeError) as context:
            safe_division("10", 2)
        self.assertIn("must be numbers", str(context.exception))
        
        with self.assertRaises(TypeError):
            safe_division([10], 2)
        
        with self.assertRaises(TypeError):
            safe_division(None, 2)
    
    def test_invalid_divisor_type_raises_type_error(self):
        """測試：除數類型錯誤應該拋出 TypeError"""
        with self.assertRaises(TypeError) as context:
            safe_division(10, "2")
        self.assertIn("must be numbers", str(context.exception))
        
        with self.assertRaises(TypeError):
            safe_division(10, [2])
        
        with self.assertRaises(TypeError):
            safe_division(10, None)
    
    def test_both_invalid_types_raises_type_error(self):
        """測試：兩個參數都是錯誤類型應該拋出 TypeError"""
        with self.assertRaises(TypeError):
            safe_division("10", "2")
        
        with self.assertRaises(TypeError):
            safe_division(None, None)
    
    def test_large_numbers(self):
        """測試：大數除法"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999999, 3), 333333333.0)
    
    def test_very_small_numbers(self):
        """測試：極小數除法"""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertAlmostEqual(safe_division(0.0001, 0.01), 0.01)
    
    def test_division_precision(self):
        """測試：除法精度"""
        result = safe_division(1, 7)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 0.142857, places=5)


if __name__ == '__main__':
    unittest.main()
