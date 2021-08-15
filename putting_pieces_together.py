from typing import List
import unittest

def sentence_maker(phrase: str) -> str:
  phrase = phrase.capitalize()
  ending = '?' if phrase.split(' ')[0] in ['How', 'Why', 'What'] else '.'
  return phrase + ending

def process_sentences(sentences: List[str]) -> str:
  result: List[str] = []

  for sentence in sentences:
    if(sentence == '\\end'):
      break
    result.append(sentence_maker(sentence))
  
  return ' '.join(result)

class MyTest(unittest.TestCase):
  def test_program(self):
    s1 = "it's a good weather today"
    s2 = "how is the weather there"
    s3 = "there's only some clouds here"
    s4 = "\\end"
    s5 = "Should not get here"

    self.assertEqual(sentence_maker(s1), "It's a good weather today.")
    self.assertEqual(sentence_maker(s2), "How is the weather there?")
    self.assertEqual(sentence_maker(s3), "There's only some clouds here.")

    result = process_sentences([s1, s2, s3, s4, s5])
    self.assertEqual(result, "It's a good weather today. How is the weather there? There's only some clouds here.")

if __name__ == '__main__':
  unittest.main()
