import unittest

class basic_operations(unittest.TestCase):
  def test_operations_on_lists(self):
    list_methods = [method for method in dir(list) if not method.startswith('_')]
    self.assertEqual(list_methods, ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'])

    monday_temperatures = [9.1, 8.8, 7.5]

    monday_temperatures.append(8.1)
    self.assertEqual(len(monday_temperatures), 4)

    monday_temperatures.clear()
    self.assertEqual(len(monday_temperatures), 0)

    monday_temperatures = [9.1, 8.8, 7.5]

    self.assertEqual(monday_temperatures.index(8.8), 1)

    with self.assertRaises(ValueError):
      monday_temperatures.index(8.8, 2)

if __name__ == '__main__':
  unittest.main()