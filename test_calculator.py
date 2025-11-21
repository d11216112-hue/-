"""
單元測試模組：測試 safe_division 函式
使用 unittest 框架進行測試
"""

import unittest
from calculator import safe_division


class TestSafeDivision(unittest.TestCase):
    """測試 safe_division 函式的各種情境"""
    
    def test_normal_division(self):
        """測試正常的數值相除"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(9, 3), 3.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_negative_division(self):
        """測試負數相除"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_by_zero(self):
        """測試除以零的情況（最重要的防呆機制）"""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(0, 0))
        self.assertIsNone(safe_division(-10, 0))
    
    def test_boundary_values(self):
        """測試邊界值"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(1, 1), 1.0)
        self.assertAlmostEqual(safe_division(1, 3), 0.333333, places=5)
    
    def test_float_division(self):
        """測試浮點數除法"""
        self.assertEqual(safe_division(5.5, 2.0), 2.75)
        self.assertEqual(safe_division(10.0, 4.0), 2.5)


if __name__ == '__main__':
    unittest.main()
