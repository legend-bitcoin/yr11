import json
import time
import requests
filename1 = time.strftime("%Y%m%d-%H%M%S")
response = requests.get("https://opentdb.com/api.php?amount=10&category=15&type=boolean")
with open(filename1 + ".json", 'w') as json_file:
    json.dump(response.json(), json_file)
Q_str = json.dumps(response.json())
Q = json.loads(Q_str)
Q_list = Q["results"]
print("No cheating in this quiz")
print("open tdb supply the question to this quiz")
print("Answer every question start with capital letter")

question_number =+
for question in Q_list:
    print("Question 1:")
    print(question["question"])
    question_def= input("Answer: ")
    if question_def == question['correct_answer']:
        pt= pt+10
        print("Good job! You are right!")
    else:
        print("Sad! You are wrong!")

# if pt == 100 :
#   pt= str(pt)
#   print("Your mark:" + pt)
#   print("Your did a great job!")
# else:
#   pt= str(pt)
#   print("Your mark:" + pt)
#   print("You can do it better next time!")