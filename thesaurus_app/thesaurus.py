import json
from typing import Dict, List
from difflib import get_close_matches

data: Dict[str, List[str]] = json.load(open('./thesaurus_app/data.json', 'r'))

def translate(s: str):
  s = s.lower()
  if s in data:
    return data[s]
  else:
    close_matches = get_close_matches(s, data.keys())
    if len(close_matches) > 0:
      return ('suggestion', close_matches[0])
  
  return "The word doesn't. Please double check it."

if __name__ == '__main__':
  word = input('Enter word: ')
  if isinstance(word, str):
    result = translate(word)
    if isinstance(result, str):
      print(result)
    elif isinstance(result, tuple):
      (type, word_suggestion) = result
      yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % word_suggestion)
      if yn == 'Y':
        print(translate(word_suggestion))
      elif yn == 'N':
        print("The word doesn't exist Please double check it")
      else:
        print("We didn't understand your entry")


