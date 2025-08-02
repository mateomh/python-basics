from unittest import TestCase
from testing.printer import Printer, PrinterError


class TestPrinter(TestCase):
  def setUp(self) -> None: # runs before every test
    self.printer = Printer(2, 300)

  def test_within_capacity(self):
    self.printer.print(25) # doesn't throw an error

  def test_returns_correct_message(self):
    message = self.printer.print(25)

    self.assertEqual('Printed 25 pages in 12.50 seconds', message)

  def test_print_outside_capacity(self):
    with self.assertRaises(PrinterError):
      self.printer.print(3000)

  def test_print_exact_capacity(self):
    self.printer.print(self.printer.capacity) # doesn't throw an error

  def test_printer_speed(self):
    pages = 10
    expected = 'Printed 10 pages in 5.00 seconds'
    result = self.printer.print(pages)

    self.assertEqual(result, expected)

  def test_speed_always_two_decimals(self):
    fast_printer = Printer(3, 300)
    pages = 11
    expected = 'Printed 11 pages in 3.67 seconds'
    result = fast_printer.print(pages)

    self.assertEqual(result, expected)

  def test_multiple_print_runs(self):
    self.printer.print(25)
    self.printer.print(50)
    self.printer.print(225)

  def test_multiple_print_exceed_capacity(self):
    self.printer.print(25)
    self.printer.print(50)
    self.printer.print(225)

    with self.assertRaises(PrinterError):
      self.printer.print(1)
  