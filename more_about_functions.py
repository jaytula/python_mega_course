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

  def test_arbitrary_number_of_arguments(self):
    def mean(*nums: int):
      return sum(nums) / len(nums)

    self.assertEqual(mean(3,4,5,6), 4.5)

if __name__ == '__main__':
  unittest.main()