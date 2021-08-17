import unittest

class MyTestCase(unittest.TestCase):
  def test_reading_file(self):
    myfile = open('./fruits.txt')
    contents = myfile.read()
    items = contents.split("\n")
    myfile.close()

    self.assertEqual(items[0], 'pear')
    self.assertEqual(items[-1], 'pomegranate')

  def test_reading_file_using_with(self):
    with open('fruits.txt') as myfile:
      contents = myfile.read()
      items = contents.split("\n")
      
      self.assertEqual(items[0], 'pear')
      self.assertEqual(items[-1], 'pomegranate')

  def test_different_filepaths(self):
    with open('./files/fruits.txt') as myfile:
      contents = myfile.read()
      items = contents.split('\n')

      self.assertEqual(items[0], 'blueberry')
      self.assertEqual(items[-1], 'raspberry')

  def test_writing_text_file(self):
    with open('files/vegetables.txt', 'w') as myfile:
      myfile.write("Tomato\nCucumber\nOnion")

    with open('files/vegetables.txt', 'r') as myfile:
      contents = myfile.read()
      items = contents.split('\n')
      self.assertEqual(items[0], 'Tomato')

  def test_file_appending(self):
    with open('files/morefruits.txt', 'a+') as myfile:
      myfile.write('\nOkra')
      myfile.seek(0)
      content = myfile.read().strip()
      items = content.split('\n')
      self.assertEqual(items[-1], 'Okra');


if __name__ == '__main__':
  unittest.main()