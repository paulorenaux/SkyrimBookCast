import json

def serialize (contents: dict, path: str):
  with open(path, 'w', encoding='utf-8') as file:
    json.dump(contents, file, ensure_ascii=False, indent=4, separators=(',', ':'))

def parse (path: str) -> dict:
  with open(path, 'r', encoding='utf-8') as file:
    return json.load(file)