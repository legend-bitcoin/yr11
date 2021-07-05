import random

the_number = random.randint(1, 100)

user = int(input("What's the number?"))

count = 1
while user != the_number:

    if user > the_number:
     print ("Lower")

    elif user < the_number:
     print ("Higher")

    user = int(input("What's the number?"))
    count += 1
    while user != the_number:
     if count > 10:
        print("you lost ")
        break


print("You guessed it!!, the number is", the_number, "and it only"\
       " took you", count , "tries")

