import json
from typing import Dict, List

data: Dict[str, List[str]] = json.load(open('./thesaurus_app/data.json', 'r'))

def translate(s: str):
  return '\n'.join(data[s])
