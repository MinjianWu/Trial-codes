import requests
import json

r = requests.get('https://formulae.brew.sh/api/formula.json').text
packages_json = json.loads(r)

# print(packages_json)

packages_str = json.dumps(packages_json, indent=4)
print(packages_str)
