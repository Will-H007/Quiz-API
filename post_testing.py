import requests
import json
# response = requests.get("http://127.0.0.1:8000/Quiz_API/")
with open('data.json', 'r') as f:
  data = json.load(f)

for quiz in data:
    response = requests.post("http://127.0.0.1:8000/Quiz_API/", data = json.dumps(quiz))
    print(response.json())