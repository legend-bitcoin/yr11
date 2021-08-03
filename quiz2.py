import requests
import random
from random import choice

def get_valid_input():
  valid_input = ['True', 'False', 'true', 'false' ,'yes' ,'no ']

response=requests.get("https://opentdb.com/api.php?amount=10&category=24&difficulty=easy&type=booleann")

print(response.json())

# save the result of the attempted quiz 
# Q_All=[response.json()["results"][i] for i in range(10)]
#It can save the record after every time after user did the quiz
# point=0
# i=0

# print("NO CHEATING IN THIS QUIZ . OTHERWISE BAD LUCK FOR WHOLE LIFE")
# print(" We get the question from open tdb ")
# print(" Use True and False to input the answer ")

# for i in range (10):
#   print("question "+str(i+1)+":")
#   #As the question user answers , it will increase like (n+1) so user never get repeated questions 
#   print(Q_All[i]["question"])
#   user_resp=input("answer ")
#   if user_resp==Q_All[i]["correct_answer"]:
#     #Identifly the user choice and give the response
#     point= point+10
#     print("Good job! You are right!")
#   else:
#     print("Sad! You are wrong!")
# else:
#     print("Please type True or False!")
#     pass

# point=str(point)
# #let the system calculate up the point
# print("Your mark:"+point   )
# if point > 80 :
#   print("Your did a great job!")                                                                                                                           
# else:
#   print("You can do it better next time!")
