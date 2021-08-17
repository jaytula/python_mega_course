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

if __name__ == '__main__':
  unittest.main()