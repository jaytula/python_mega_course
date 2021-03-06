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

  def test_remove_item_from_list(self):
    monday_temperatures = [9.1, 8.8, 7.5]
    monday_temperatures.remove(8.8)
    self.assertEqual(monday_temperatures, [9.1, 7.5])

  def test_accessing_list_items(self):
    monday_temperatures = [9.1, 8.8, 7.5]
    self.assertEqual(monday_temperatures.__getitem__(1), 8.8)
    self.assertEqual(monday_temperatures[2], 7.5)

  def test_accessing_list_slices(self):
    monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
    self.assertEqual(monday_temperatures[1:4], [8.8, 7.5, 6.6])
    self.assertEqual(monday_temperatures[:3], [9.1, 8.8, 7.5])

  def test_negative_indexing(self):
    monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
    self.assertEqual(monday_temperatures[-2:], [6.6, 9.9])
    self.assertEqual(monday_temperatures[-2:-1], [6.6])
    self.assertEqual(monday_temperatures[-1], 9.9)

  def test_string_slices_and_indexing(self):
    mystring = 'hello'
    self.assertEqual(mystring[1], 'e')
    self.assertEqual(mystring[-1], 'o')
    self.assertEqual(mystring[:3], 'hel')

  def test_accessing_dictionary_items(self):
    student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
    self.assertEqual(student_grades['Marry'], 9.1)

  def test_convert_between_types(self):
    data = [['name', 'John'], ['surname', 'smith']]
    self.assertEqual(dict(data), {'name': 'John', 'surname': 'smith'})

if __name__ == '__main__':
  unittest.main()