"""
Unit tests for the Calculator module
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation"""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction operation"""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(5, 5), 0)
    
    def test_multiply(self):
        """Test multiplication operation"""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division operation"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_modulo(self):
        """Test modulo operation"""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 5), 0)
        self.assertEqual(self.calc.modulo(7, 2), 1)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
    
    def test_power(self):
        """Test power operation"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_square_root(self):
        """Test square root operation"""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertAlmostEqual(self.calc.square_root(2), 1.41421, places=5)
    
    def test_square_root_negative(self):
        """Test square root of negative number raises error"""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
    
    def test_clear(self):
        """Test clear operation"""
        self.calc.add(5, 3)
        self.assertEqual(self.calc.clear(), 0)
        self.assertEqual(self.calc.get_result(), 0)
    
    def test_get_result(self):
        """Test get result"""
        self.calc.add(10, 20)
        self.assertEqual(self.calc.get_result(), 30)


if __name__ == '__main__':
    unittest.main()
