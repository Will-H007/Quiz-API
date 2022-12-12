import requests
import json
response = requests.get("http://127.0.0.1:8000/Quiz_API/")
data = response.json()
print(data['question'])


for answer in data['answers']:
    print( answer)

parameters = {
    "id": data['id'],
    "answers": data['answers']
}

user_answer = input("Your answer: ")
# if data['q_type'] == 1:
data['answers'][user_answer] = True
r = requests.put("http://127.0.0.1:8000/Quiz_API/", data = json.dumps(data))
print(r.json()['message'])

   