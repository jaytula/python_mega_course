from typing import List
import unittest

class MyTestCase(unittest.TestCase):
  def test_more_about_functions(self):
    def subtract(a: int, b: int = 6):
      return a - b

    # positional arguments
    self.assertEqual(subtract(4, 3), 1)

    # keyword arguments
    self.assertEqual(subtract(b=3, a=4), 1)

    # default params
    self.assertEqual(subtract(a=3), -3)

if __name__ == '__main__':
  unittest.main()