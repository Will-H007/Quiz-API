import requests
import json
response = requests.get("http://127.0.0.1:8000/Quiz_API/")
data = response.json()
print(data['question'])
# choice = ['A', 'B', 'C', 'D']
i = 0
for answer in data['answers']:
    print( answer)
    i += 1


user_answer = input("Your answer: ")
if data['answers'][user_answer] == True:    
    print("You are right!")
    data['validation'] = True
    r = requests.put("http://127.0.0.1:8000/Quiz_API/", data = json.dumps(data))
    print(r.content)
while data['answers'][user_answer] == False:
    print('Wrong :(, try again')
    user_answer = input("Your answer: ")
    if data['answers'][user_answer] == True:
        print("You are right!")
        data['validation'] = True
        r = requests.put("http://127.0.0.1:8000/Quiz_API/", data = json.dumps(data))

    else:
        print('Wrong :(, try again')