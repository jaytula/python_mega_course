from typing import Dict, List
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

  def test_process_strings(self):
    def process(*strings: str):
      strings_list = list(strings)
      strings_list.sort()

      return [string.upper() for string in strings_list]

    self.assertEqual(process('snow', 'glacier', 'iceberg'), ["GLACIER", "ICEBERG", "SNOW"])

  def test_indefinite_number_of_keyword_arguments(self):
    def mean(**kwargs: int):
      return kwargs

    self.assertEqual(mean(a=1, b=2, c=4), {"a": 1, "b": 2, "c": 4})

if __name__ == '__main__':
  unittest.main()