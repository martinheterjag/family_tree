import json
from pprint import pprint

with open("./json/family.json") as f:
    data = json.load(f)

pprint(data)