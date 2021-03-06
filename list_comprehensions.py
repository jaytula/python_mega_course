from typing import List, Union
import unittest


class MyTestCase(unittest.TestCase):
  def test_simple_list_comprehensions(self):
    temps = [221, 234, 340, 230]

    result = [temp / 10 for temp in temps]
    self.assertEqual(result, [22.1, 23.4, 34.0, 23.0])

  def test_list_comprehension_with_conditional(self):
    temps = [221, 234, 340, -9999, 230]

    result = [temp / 10 for temp in temps if temp != -9999]
    self.assertEqual(result, [22.1, 23.4, 34.0, 23.0])

  def test_exercise_36(self):
    def foo(items: List[Union[int, str]]):
      return [item for item in items if isinstance(item, int)]

    items = [99, 'no data', 95, 94, 'no data']
    self.assertEqual(foo(items), [99, 95, 94])
  
  def test_exercise_37(self):
    def foo(items: List[int]):
      return [item for item in items if item > 0]

    items = [-5, 3, -1, 101]
    self.assertEqual(foo(items), [3, 101])

  def test_list_comprehensions_if_else(self):
    def foo(temps: List[int]):
      return [temp / 10 if temp > 0 else 0 for temp in temps]

    temps = [221, 234, 240, -9999, 230]
    expected = [22.1, 23.4, 24.0, 0, 23.0]

    self.assertEqual(foo(temps), expected)

if __name__ == '__main__':
  unittest.main()