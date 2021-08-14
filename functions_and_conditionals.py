from typing import List
import unittest

def mean(numbers: List[int]) -> float:
  return sum(numbers)/len(numbers)

class FunctionsAndConditionals(unittest.TestCase):
  def test_creating_functions(self):
    self.assertAlmostEqual(mean([3, 4, 5, 6]), 4.5)

if __name__ == '__main__':
  unittest.main()