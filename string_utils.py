import unittest

def reverse_string(s):
  return s[::-1]

def capitalize_string(s):
  return s.capitalize()

def is_capitalized(s):
  return s[0].isupper()

class MyTestCase(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")

    def test_is_capitalized(self):
       self.assertTrue(is_capitalized("Hello"))
       self.assertFalse(is_capitalized("hello"))

if __name__ == '__main__':
    unittest.main()