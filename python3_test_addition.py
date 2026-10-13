import unittest

def add(a, b):
  return a + b

class TestAddition(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(3, 4)

    # Define the expected result
    expected_result = 8
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()