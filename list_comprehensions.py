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

if __name__ == '__main__':
  unittest.main()