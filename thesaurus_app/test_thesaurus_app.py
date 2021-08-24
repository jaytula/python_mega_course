from typing import List
import unittest
from difflib import SequenceMatcher

from thesaurus import translate

class ThesaurusAppTests(unittest.TestCase):
  def test_basic_test(self):
    actual = translate('mountain')
    self.assertTrue(isinstance(actual, List) and actual[0].startswith('A feature of the'))

    actual = translate('mathematics')
    self.assertTrue(isinstance(actual, List) and actual[0].startswith('The science that deals'))

    actual = translate('rainn')
    self.assertEqual(actual, "The word doesn't. Please double check it.")

    actual = translate('RAIN')
    self.assertTrue(isinstance(actual, List) and actual[0].startswith('Precipitation'))

  def test_spellchecking(self):
    sq = SequenceMatcher(None, 'rainn', 'rain')
    self.assertAlmostEqual(sq.ratio(), 0.889, 3)

if __name__ == '__main__':
  unittest.main()