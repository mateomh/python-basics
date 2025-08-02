# to run the tests
# python -m unittest <file_path>

from decimal import Decimal
from unittest import TestCase
from testing.functions import divide, multiply

class TestFunctions(TestCase):
  def test_divide_result(self):
    dividend = Decimal(15)
    divisor = Decimal(3)
    expected_result = Decimal(5.0)
    self.assertEqual(divide(dividend, divisor), expected_result)

  def test_divide_negative(self):
    dividend = Decimal(15)
    divisor = Decimal(-3)
    expected_result = Decimal(-5.0)
    self.assertEqual(divide(dividend, divisor), expected_result)

  def test_divide_dividend_zero(self):
    dividend = Decimal(0)
    divisor = Decimal(3)
    expected_result = Decimal(0)
    self.assertEqual(divide(dividend, divisor), expected_result)

  def test_divide_error_when_divisor_zero(self):
    with self.assertRaises(ValueError):
      dividend = Decimal(5)
      divisor = Decimal(0)
      divide(dividend, divisor)

  def test_multiply_empty(self):
    with self.assertRaises(ValueError):
      multiply()

  def test_multiply_single_value(self):
    expected = 15
    self.assertEqual(multiply(expected), expected)

  def test_multiply_zero(self):
    expected = 0
    self.assertEqual(multiply(expected), expected)
  
  def test_multiply_result(self):
    inputs = (3, 5)
    expected = 15
    self.assertEqual(multiply(*inputs), expected)

  def test_multiply_result_with_zero(self):
    inputs = (3, 5, 0)
    expected = 0
    self.assertEqual(multiply(*inputs), expected)

  def test_multiply_negative(self):
    inputs = (3, -5)
    expected = -15
    self.assertEqual(multiply(*inputs), expected)

  def test_multiply_floats(self):
    inputs = (3, 5.0)
    expected = 15.0
    self.assertEqual(multiply(*inputs), expected)