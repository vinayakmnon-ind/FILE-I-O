import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class MyTestCases (unittest.TestCase):
  def test_get_sqrt(self):
    self.assertEqual(get_sqrt(144), 12)
    with self.assertRaises(ValueError):
        self.assertIn(get_sqrt(-1), ValueError)

    def test_divide(self):
      self.assertEqual(divide(10, 2), 5)
      with self.assertRaises(ZeroDivisionError):
        divide(10, 0)

if __name__ == '__main__':
    unittest.main()