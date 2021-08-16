import unittest

temps = [221, 234, 340, 230]

class MyTestCase(unittest.TestCase):
  def test_simple_list_comprehensions(self):
    result = [temp / 10 for temp in temps]
    self.assertEqual(result, [22.1, 23.4, 34.0, 23.0])

if __name__ == '__main__':
  unittest.main()