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
      return 'Did you mean %s instead?' % close_matches[0]
  
  return "The word doesn't. Please double check it."

if __name__ == '__main__':
  word = input('Enter word: ')
  print(translate(word))
