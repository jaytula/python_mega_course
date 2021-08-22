import json
from typing import Dict, List

data: Dict[str, List[str]] = json.load(open('./thesaurus_app/data.json', 'r'))

def translate(s: str):
  s = s.lower()
  return data[s] if s in data else "The word doesn't. Please double check it."
