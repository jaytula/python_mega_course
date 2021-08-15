from typing import List
import unittest

def rounded_values(numbers: List[float]) -> List[int]:
  return [round(num) for num in numbers]


class MyTests(unittest.TestCase):
  def test_for_loop_basics(self):
    monday_temperatures = [9.1, 8.8, 7.6]
    actual = rounded_values(monday_temperatures)
    expected = [9, 9, 8]
    self.assertEqual(actual, expected)

    for a, b in zip(actual, expected):
      self.assertEqual(a, b)

  def test_for_loop_string(self):
    s = 'Hello'
    expected = ['H', 'e', 'l', 'l', 'o']

    for idx, ch in enumerate(s):
      self.assertEqual(ch, expected[idx])

if __name__ == '__main__':
  unittest.main()