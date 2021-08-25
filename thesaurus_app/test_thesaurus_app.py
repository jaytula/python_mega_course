from typing import List
import unittest
from difflib import SequenceMatcher, get_close_matches

from thesaurus import translate

class ThesaurusAppTests(unittest.TestCase):
  def test_basic_test(self):
    actual = translate('mountain')
    self.assertTrue(isinstance(actual, List) and actual[0].startswith('A feature of the'))

    actual = translate('mathematics')
    self.assertTrue(isinstance(actual, List) and actual[0].startswith('The science that deals'))

    actual = translate('rainn')
    self.assertTrue(isinstance(actual, str) and actual.startswith("Did you mean"))

    actual = translate('RAIN')
    self.assertTrue(isinstance(actual, List) and actual[0].startswith('Precipitation'))

  def test_spellchecking(self):
    sq = SequenceMatcher(None, 'rainn', 'rain')
    self.assertAlmostEqual(sq.ratio(), 0.889, 3)

  def test_bestmatches(self):
    matches = get_close_matches('rainn', ['help', 'pyramid', 'rain'])
    self.assertEqual(matches, ['rain'])

if __name__ == '__main__':
  unittest.main()