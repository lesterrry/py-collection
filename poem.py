import requests
import json

url = "https://www.poemist.com/api/v1/randompoems"
r = requests.get(url)
j = json.loads(r.text)
print(j[0]['content'])
