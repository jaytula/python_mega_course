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

  def test_for_loop_over_dict(self):
    student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
    keys = ["Marry", "Sim", "John"]
    values = [9.1, 8.8, 7.5]

    for key in student_grades.keys():
      self.assertTrue(key in keys)
    
    for value in student_grades.values():
      self.assertTrue(value in values)

    for item in student_grades.items():
      self.assertTrue(item[0] in keys)
      self.assertTrue(item[1] in values)

  def test_format_string_method(self):
    self.assertEqual("Hello {}".format('foo'), 'Hello foo')

  def test_while_loop(self):
    username = ''
    usernames = ['a', 'b', 'c', 'd', 'pypy', 'f']
    count = 0
    while username != 'pypy':
      username = usernames.pop()
      count = count+1
    self.assertEqual(count, 2)

  def test_while_break(self):
    username = ''
    usernames = ['a', 'b', 'c', 'd', 'pypy', 'f']
    count = 0
    while True:
      if(len(usernames) == 0):
        break
      username = usernames.pop()
      count = count + 1
      if(username != 'pypy'):
        continue
      else:
        break
    self.assertEqual(count, 2)


if __name__ == '__main__':
  unittest.main()
  