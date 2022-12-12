import requests
import json
# response = requests.get("http://127.0.0.1:8000/Quiz_API/")
data = input("upload lesson1 or lesson2 ?: ") + '.json'
with open(data, 'r') as f:
  data = json.load(f)

for quiz in data:
    response = requests.post("http://127.0.0.1:8000/Quiz_API/", data = json.dumps(quiz))
    print(response.json())
    