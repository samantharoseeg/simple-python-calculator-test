"""
Unit tests for the calculator module.

These tests verify that our calculator functions work correctly
with various inputs including positive, negative, and zero values.
"""

import unittest
from calculator import add, subtract, divide


class TestCalculatorFunctions(unittest.TestCase):
    """Test suite for calculator functions."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Testing basic positive number addition
        result = add(5, 3)
        self.assertEqual(result, 8, "Adding 5 + 3 should equal 8")
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        # Testing with negative numbers
        result = add(-2, -3)
        self.assertEqual(result, -5, "Adding -2 + -3 should equal -5")
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        # Testing mixed positive and negative
        result = add(10, -4)
        self.assertEqual(result, 6, "Adding 10 + (-4) should equal 6")
    
    def test_add_with_zero(self):
        """Test adding with zero."""
        # Testing that adding zero doesn't change the value
        result = add(7, 0)
        self.assertEqual(result, 7, "Adding 7 + 0 should equal 7")
    
    def test_add_decimal_numbers(self):
        """Test adding decimal numbers."""
        # Testing with decimal values
        result = add(3.5, 2.5)
        self.assertEqual(result, 6.0, "Adding 3.5 + 2.5 should equal 6.0")
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        # Testing basic positive number subtraction
        result = subtract(10, 4)
        self.assertEqual(result, 6, "Subtracting 10 - 4 should equal 6")
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        # Subtracting a negative is like adding
        result = subtract(5, -3)
        self.assertEqual(result, 8, "Subtracting 5 - (-3) should equal 8")
    
    def test_subtract_resulting_in_negative(self):
        """Test subtraction that results in a negative number."""
        # Testing when result is negative
        result = subtract(3, 7)
        self.assertEqual(result, -4, "Subtracting 3 - 7 should equal -4")
    
    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        # Testing subtraction with zero
        result = subtract(9, 0)
        self.assertEqual(result, 9, "Subtracting 9 - 0 should equal 9")
    
    def test_subtract_decimal_numbers(self):
        """Test subtracting decimal numbers."""
        # Testing with decimal values
        result = subtract(7.5, 2.5)
        self.assertEqual(result, 5.0, "Subtracting 7.5 - 2.5 should equal 5.0")
    
    def test_add_invalid_input_string(self):
        """Test that add raises TypeError for string inputs."""
        with self.assertRaises(TypeError):
            add("5", 3)
        with self.assertRaises(TypeError):
            add(5, "3")
    
    def test_add_invalid_input_none(self):
        """Test that add raises TypeError for None inputs."""
        with self.assertRaises(TypeError):
            add(None, 3)
        with self.assertRaises(TypeError):
            add(5, None)
    
    def test_subtract_invalid_input_string(self):
        """Test that subtract raises TypeError for string inputs."""
        with self.assertRaises(TypeError):
            subtract("10", 3)
        with self.assertRaises(TypeError):
            subtract(10, "3")
    
    def test_subtract_invalid_input_none(self):
        """Test that subtract raises TypeError for None inputs."""
        with self.assertRaises(TypeError):
            subtract(None, 5)
        with self.assertRaises(TypeError):
            subtract(5, None)
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        result = divide(10, 2)
        self.assertEqual(result, 5.0, "Dividing 10 / 2 should equal 5.0")
    
    def test_divide_decimal_numbers(self):
        """Test dividing decimal numbers."""
        result = divide(7.5, 2.5)
        self.assertEqual(result, 3.0, "Dividing 7.5 / 2.5 should equal 3.0")
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error."""
        # This test will fail because our divide function doesn't handle division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
    
    def test_divide_invalid_input_string(self):
        """Test that divide raises TypeError for string inputs."""
        # This test will fail because our divide function doesn't do type checking
        with self.assertRaises(TypeError):
            divide("10", 2)
        with self.assertRaises(TypeError):
            divide(10, "2")


if __name__ == '__main__':
    # Run the tests with verbose output
    unittest.main(verbosity=2)