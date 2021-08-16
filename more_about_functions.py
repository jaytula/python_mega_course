from typing import List
import unittest

class MyTestCase(unittest.TestCase):
  def test_multiple_arguments(self):
    def area(a: int, b: int):
      return a * b

    self.assertEqual(area(4, 3), 12)

if __name__ == '__main__':
  unittest.main()