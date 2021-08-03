import requests
response=requests.get("https://opentdb.com/api.php?amount=10&category=15&type=boolean")
Q_All=[response.json()["results"][0],response.json()["results"][1],response.json()["results"][2],response.json()["results"][3],response.json()["results"][4],response.json()["results"][5],response.json()["results"][6],response.json()["results"][7],response.json()["results"][8],response.json()["results"][9]]
def get_valid_input():
  valid_input = ['True', 'False', 'true', 'false' ,'yes' ,'no ']
point=0
i=0
print("NO CHEATING IN THIS QUIZ . OTHERWISE BAD LUCK FOR WHOLE LIFE")
print(" We get the question from open tdb ")
print(" Use True and False to input the answer ")
while i < 10:
  print("Question "+str(i+1)+":")
  #As the question user answers , it will increase like (n+1) so user never get repeated questions 
  print(Q_All[i]["question"])
  User_Resp=input("Answer: ")
  if User_Resp=="True" or User_Resp=="False":
   if User_Resp==Q_All[i]["correct_answer"]:
    point= point+10
    print("Good job! You are right!")
   else:
    print("Sad! You are wrong!")
   if i==10:
    continue
   i+=1
  else:
    print("Please type True or False!")
    pass
point=str(point)
#let the system calculate up the point
print("Your mark:"+point   )
if point > 80 :
  print("Your did a great job!")                                                                                                                           
else:
  print("You can do it better next time!")