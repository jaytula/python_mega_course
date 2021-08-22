import unittest

from thesaurus import translate

class ThesaurusAppTests(unittest.TestCase):
  def test_basic_test(self):
    actual = translate('mountain')
    self.assertTrue(actual.startswith('A feature of the'))

    actual = translate('mathematics')
    self.assertTrue(actual.startswith('The science that deals'))

if __name__ == '__main__':
  unittest.main()